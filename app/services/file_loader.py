from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


def load_text(filename: str) -> str:
    file_path = KNOWLEDGE_DIR / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return "Knowledge file not found."