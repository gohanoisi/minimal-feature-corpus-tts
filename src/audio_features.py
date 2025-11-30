"""
音声特徴量抽出モジュール

メルスペクトログラム、F0、その他の音声特徴量を抽出する関数群
"""

import numpy as np
from pathlib import Path
from typing import Tuple, Optional


def extract_mel_spectrogram(
    audio_path: str,
    sample_rate: int = 24000,
    n_mels: int = 80,
    hop_length: int = 256,
    win_length: int = 1024,
) -> np.ndarray:
    """
    メルスペクトログラムを抽出
    
    Args:
        audio_path: 音声ファイルのパス
        sample_rate: サンプリングレート
        n_mels: メルフィルタバンクの数
        hop_length: ホップ長
        win_length: ウィンドウ長
    
    Returns:
        メルスペクトログラム (n_mels, T)
    """
    # TODO: 実装
    pass


def extract_f0(
    audio_path: str,
    sample_rate: int = 24000,
    method: str = "pyworld",
) -> Tuple[np.ndarray, np.ndarray]:
    """
    F0（基本周波数）を抽出
    
    Args:
        audio_path: 音声ファイルのパス
        sample_rate: サンプリングレート
        method: 抽出方法 ("pyworld", "praat", etc.)
    
    Returns:
        (f0, voiced_flag): F0配列と有声/無声フラグ
    """
    # TODO: 実装
    pass


def extract_phonemes(
    lab_path: str,
    label_type: str = "mon",
) -> list:
    """
    音素ラベルファイルから音素列を抽出
    
    Args:
        lab_path: ラベルファイルのパス
        label_type: ラベルタイプ ("mon" or "ful")
    
    Returns:
        音素列のリスト
    """
    # TODO: 実装
    pass


def extract_all_features(
    audio_path: str,
    lab_path: Optional[str] = None,
) -> dict:
    """
    すべての特徴量を一度に抽出
    
    Args:
        audio_path: 音声ファイルのパス
        lab_path: ラベルファイルのパス（オプション）
    
    Returns:
        特徴量の辞書
    """
    # TODO: 実装
    pass

