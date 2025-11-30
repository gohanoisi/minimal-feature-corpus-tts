from pathlib import Path
from typing import List

def list_wav_files(root: str) -> List[Path]:
    root_path = Path(root)
    return sorted(root_path.rglob("*.wav"))

wav_files = list_wav_files("data/jvs_ver1")
for wav in wav_files:
    print(wav)