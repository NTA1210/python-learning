from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from src.schemas import PostCreate
from src.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from src.images import imagekit
import shutil
import os
import uuid
import tempfile

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/upload")
async def upload_file(
                      file: UploadFile = File(...),
                      caption: str = Form(""),
                      session: AsyncSession = Depends(get_async_session)):

    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        with open(temp_file_path, "rb") as f:
            file_bytes = f.read()

        upload_result = imagekit.upload(
            file=file_bytes,
            file_name=file.filename,
            options={
                "use_unique_file_name": True,
                "tags": ["backend_upload"]
            }
        )

        if upload_result.get("http_status") == 200 or upload_result.get("status_code") == 200:
            post = Post(caption=caption,
                        url=upload_result.get("url"),
                        file_type="video" if file.content_type.startswith("video/") else "image",
                        file_name=upload_result.get("file_name"))
            session.add(post)
            await session.commit()
            await session.refresh(post)
            return post
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

@app.get("/feed")
async def get_feed(session: AsyncSession = Depends(get_async_session)):
    results = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in results.all()]

    posts_data = []
    for post in posts:
        post_data = {
            "id": str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        }
        posts_data.append(post_data)
    return {"posts": posts_data}
