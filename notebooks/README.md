# Notebooks ディレクトリ

このディレクトリには、研究プロジェクトで使用するJupyter Notebookが目的別に分類されています。

## ディレクトリ構成

### `data_preparation/` - データ準備
データセットのダウンロードと準備に関するノートブック

- `01_download_jvs.ipynb` - JVSコーパスのダウンロード

### `analysis/` - 分析
コーパスや特徴量の分析に関するノートブック

- `02_feature_extraction.ipynb` - 音声特徴量の抽出（メルスペクトログラム、F0等）
- `03_corpus_analysis.ipynb` - コーパス分析（音素カバレッジ等）
- `04_feature_density.ipynb` - 特徴量密度分析
- `05_attention_analysis.ipynb` - Attention機構の可視化・分析

### `styletts2/` - StyleTTS2
StyleTTS2モデルに関するノートブック（ゼロからの学習パイプライン）

#### 学習パイプライン（順番に実行）
1. `00_setup_environment.ipynb` - 環境セットアップ
2. `01_prepare_datasets.ipynb` - データセット準備
3. `02_generate_configs.ipynb` - 設定ファイル生成
4. `03_train_models.ipynb` - モデル学習（Stage 1, Stage 2）
5. `04_generate_evaluation_audio.ipynb` - 評価音声生成

#### その他
- `04_tts_training.ipynb` - StyleTTS2学習（既存版）

### `espnet/` - ESPNet
ESPNetモデルに関するノートブック

- `05_espnet_training.ipynb` - ESPNet-VITSモデルの学習

### `evaluation/` - 評価
モデルの評価に関するノートブック

- `06_evaluation.ipynb` - 音声品質評価（MOS、MCD、F0誤差等）

### `utils/` - ユーティリティ
汎用的なユーティリティノートブック

- `00_env_check.ipynb` - 環境チェック（CUDA、GPU確認等）

## 実行順序の推奨

### StyleTTS2ゼロからの学習（新規実装）
1. `styletts2/00_setup_environment.ipynb`
2. `styletts2/01_prepare_datasets.ipynb`
3. `styletts2/02_generate_configs.ipynb`
4. `styletts2/03_train_models.ipynb`
5. `styletts2/04_generate_evaluation_audio.ipynb`

### 一般的な分析フロー
1. `data_preparation/01_download_jvs.ipynb`
2. `analysis/02_feature_extraction.ipynb`
3. `analysis/03_corpus_analysis.ipynb`
4. `analysis/04_feature_density.ipynb`
5. `analysis/05_attention_analysis.ipynb`

