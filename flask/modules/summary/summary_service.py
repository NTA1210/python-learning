from database import SessionLocal
from modules.summary.summary_repository import SummaryRepository
from integrations.openai_client import OpenAIClient
from modules.summary.summary_model import Summary
from modules.summary.summary_helpers import chunk_text, count_tokens
from utils.file import write_file
from werkzeug.datastructures import FileStorage

SYSTEM_PROMPT = (
    "You are a highly skilled text summarization assistant. "
    "Your task is to read the input text and produce a clear, concise, and accurate summary. "
    "Focus on capturing the main ideas, key facts, and important details, while omitting unnecessary repetition or minor details. "
    "Use natural, easy-to-read language. "
    "If the text is very long, create a summary that retains the core meaning without losing context. "
    "Keep the summary brief, coherent, and self-contained."
)


class SummaryService:

    def __init__(self):
        self.ai_client = OpenAIClient()
        self.db = SessionLocal()

    def _build_prompt(self, text: str):
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]

    def summarize(self, file: FileStorage) -> Summary:
        content = file.read().decode('utf-8', errors="ignore")
        print("TOTAL WORDS: ",len(content))
        filename = file.filename
        summary_filename = f"uploads/summary_{filename}"

        try:
            chunks = chunk_text(content)
            summary_text = ""

            while len(chunks) != 1:
                summaries = []
                for chunk in chunks:
                    summaries.append(self._summarize_once(chunk))
                content = "\n".join(summaries)
                chunks = chunk_text(content) 

            summary_text = self._summarize_once(content) 

            # write file    
            write_file(summary_filename, summary_text)

            summary = SummaryRepository(self.db).summarize(summary_filename)
            print('SUMMARY',summary.to_dict())
            print("FINAL TOTAL WORDS: ",len(summary_text))
            return summary
        finally:
            self.db.close()

    def _summarize_once(self, text: str):
        messages = self._build_prompt(text)
        response = self.ai_client.summarize(messages)
        return response.choices[0].message.content