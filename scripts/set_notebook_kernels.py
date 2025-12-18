#!/usr/bin/env python3
"""
ノートブックファイルのカーネルを.venvに設定するスクリプト

使用方法:
    python scripts/set_notebook_kernels.py
"""

import json
from pathlib import Path
import sys

def update_notebook_kernel(notebook_path: Path, kernel_name: str = "python3") -> bool:
    """
    ノートブックファイルのカーネル情報を更新
    
    Args:
        notebook_path: ノートブックファイルのパス
        kernel_name: カーネル名（デフォルト: python3）
    
    Returns:
        更新が成功した場合はTrue
    """
    try:
        # ノートブックファイルを読み込む
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # メタデータを更新
        if 'metadata' not in notebook:
            notebook['metadata'] = {}
        
        if 'kernelspec' not in notebook['metadata']:
            notebook['metadata']['kernelspec'] = {}
        
        notebook['metadata']['kernelspec']['name'] = kernel_name
        notebook['metadata']['kernelspec']['display_name'] = f"Python 3.12.9 ('.venv': venv)"
        
        # 既存のlanguage_infoを維持（存在する場合）
        if 'language_info' not in notebook['metadata']:
            notebook['metadata']['language_info'] = {}
        
        notebook['metadata']['language_info']['name'] = "python"
        
        # ファイルを保存
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        return True
    except Exception as e:
        print(f"エラー: {notebook_path}: {e}", file=sys.stderr)
        return False

def main():
    """メイン関数"""
    # プロジェクトルート
    project_root = Path(__file__).parent.parent
    
    # ノートブックディレクトリ
    notebooks_dir = project_root / 'notebooks'
    
    if not notebooks_dir.exists():
        print(f"エラー: ノートブックディレクトリが見つかりません: {notebooks_dir}")
        sys.exit(1)
    
    # すべての.ipynbファイルを検索
    notebook_files = list(notebooks_dir.rglob('*.ipynb'))
    
    if not notebook_files:
        print("ノートブックファイルが見つかりませんでした。")
        sys.exit(0)
    
    print(f"見つかったノートブックファイル: {len(notebook_files)}個\n")
    
    # 各ノートブックファイルを更新
    updated_count = 0
    failed_count = 0
    
    for nb_file in notebook_files:
        relative_path = nb_file.relative_to(project_root)
        if update_notebook_kernel(nb_file):
            print(f"✓ {relative_path}")
            updated_count += 1
        else:
            print(f"✗ {relative_path}")
            failed_count += 1
    
    print(f"\n更新完了: {updated_count}個成功, {failed_count}個失敗")

if __name__ == '__main__':
    main()

