import os
import uuid
from werkzeug.utils import secure_filename

def read_file(path:str):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    
def write_file(path:str, content:str):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def normalize_filename(original_filename: str) -> str:
    filename = secure_filename(original_filename)
    name, ext = os.path.splitext(filename)

    unique_name = f"{name}_{uuid.uuid4().hex}{ext}"
    return unique_name.lower()