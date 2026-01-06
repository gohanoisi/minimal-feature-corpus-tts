# StyleTTS2 Notebooks

StyleTTS2モデルのゼロからの学習パイプラインに関するノートブックです。

## 学習パイプライン

RTX 4070ti (VRAM 12GB) 環境でのStyleTTS2ゼロからの学習を想定しています。

### 実行順序

1. **`00_setup_environment.ipynb`** - 環境セットアップ
   - StyleTTS2リポジトリの確認
   - 依存パッケージの確認
   - CUDA/PyTorchの確認
   - phonemizerの確認

2. **`01_prepare_datasets.ipynb`** - データセット準備
   - 3つのデータセット（phone_min4, feat_top10, full100）の準備
   - 音声ファイルのコピー
   - 日本語テキストの音素化（eSpeak-NG）
   - train_list.txt, val_list.txtの生成

3. **`02_generate_configs.ipynb`** - 設定ファイル生成
   - RTX 4070ti最適化パラメータ（batch_size=6, max_len=300, fp16）
   - 各データセット用のconfig.ymlを生成

4. **`03_train_models.ipynb`** - モデル学習
   - Stage 1学習コマンドの生成・実行
   - Stage 2学習コマンドの生成・実行
   - 学習済みモデルの確認

5. **`04_generate_evaluation_audio.ipynb`** - 評価音声生成
   - 学習済みモデルで評価文の音声を生成
   - 各データセット条件での音声品質比較

## その他

- **`04_tts_training.ipynb`** - StyleTTS2学習（既存版）

## データセット定義

- **phone_min4**: 4文（音素カバレッジ最小4文）
- **feat_top10**: 10文（特徴量密度トップ10文）
- **full100**: 100文（全100文）

## 注意事項

- 学習には長時間かかります（数時間〜数日）
- VRAMエラーが発生した場合は、設定ファイルのbatch_sizeやmax_lenを削減してください
- TensorBoardで学習の進捗を確認できます

