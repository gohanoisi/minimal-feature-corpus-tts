#!/usr/bin/env python3
"""
ノートブックファイルのPROJECT_ROOT取得ロジックを修正するスクリプト

使用方法:
    python scripts/fix_project_root_in_notebooks.py
"""

import json
from pathlib import Path
import sys

def fix_project_root_logic(notebook_path: Path) -> bool:
    """
    ノートブックファイルのPROJECT_ROOT取得ロジックを修正
    
    Args:
        notebook_path: ノートブックファイルのパス
    
    Returns:
        更新が成功した場合はTrue
    """
    try:
        # ノートブックファイルを読み込む
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        updated = False
        old_pattern = 'PROJECT_ROOT = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()'
        new_code = '''# プロジェクトルートを取得
# notebooks/styletts2/ から実行される場合: 2階層上がる
# notebooks/ から実行される場合: 1階層上がる
current_dir = Path.cwd()
if current_dir.name == "styletts2":
    PROJECT_ROOT = current_dir.parent.parent  # notebooks/styletts2 -> notebooks -> project_root
elif current_dir.name == "notebooks":
    PROJECT_ROOT = current_dir.parent  # notebooks -> project_root
else:
    PROJECT_ROOT = current_dir  # プロジェクトルートから直接実行'''
        
        # 各セルを確認
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'code':
                source_lines = cell.get('source', [])
                source_text = ''.join(source_lines)
                
                # 古いパターンを探す
                if old_pattern in source_text:
                    # 古い行を新しいコードに置き換え
                    new_source_lines = []
                    for line in source_lines:
                        if old_pattern.strip() in line:
                            # 古い行を新しいコードで置き換え
                            indent = len(line) - len(line.lstrip())
                            new_lines = new_code.split('\n')
                            for i, new_line in enumerate(new_lines):
                                if i == 0:
                                    new_source_lines.append(line.rstrip().replace(old_pattern.strip(), new_line) + '\n')
                                else:
                                    new_source_lines.append(' ' * indent + new_line + '\n')
                            updated = True
                        else:
                            new_source_lines.append(line)
                    
                    if updated:
                        cell['source'] = new_source_lines
                        break
        
        if updated:
            # ファイルを保存
            with open(notebook_path, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, indent=1, ensure_ascii=False)
        
        return updated
    except Exception as e:
        print(f"エラー: {notebook_path}: {e}", file=sys.stderr)
        return False

def main():
    """メイン関数"""
    # プロジェクトルート
    project_root = Path(__file__).parent.parent
    
    # StyleTTS2ノートブックディレクトリ
    notebooks_dir = project_root / 'notebooks' / 'styletts2'
    
    if not notebooks_dir.exists():
        print(f"エラー: ノートブックディレクトリが見つかりません: {notebooks_dir}")
        sys.exit(1)
    
    # すべての.ipynbファイルを検索
    notebook_files = [
        notebooks_dir / '01_prepare_datasets.ipynb',
        notebooks_dir / '02_generate_configs.ipynb',
        notebooks_dir / '03_train_models.ipynb',
        notebooks_dir / '04_tts_training.ipynb',
        notebooks_dir / '04_generate_evaluation_audio.ipynb',
    ]
    
    print(f"ノートブックファイルを確認します...\n")
    
    # 各ノートブックファイルを更新
    updated_count = 0
    skipped_count = 0
    
    for nb_file in notebook_files:
        if not nb_file.exists():
            print(f"⚠ {nb_file.name} が見つかりません")
            skipped_count += 1
            continue
        
        relative_path = nb_file.relative_to(project_root)
        if fix_project_root_logic(nb_file):
            print(f"✓ {relative_path}")
            updated_count += 1
        else:
            print(f"- {relative_path} (既に修正済みか、パターンが見つかりませんでした)")
            skipped_count += 1
    
    print(f"\n更新完了: {updated_count}個更新, {skipped_count}個スキップ")

if __name__ == '__main__':
    main()

