from pathlib import Path
from typing import List

def list_wav_files(root: str) -> List[Path]:
    root_path = Path(root)
    return sorted(root_path.rglob("*.wav"))
