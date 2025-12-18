# Analysis Notebooks

コーパスや特徴量の分析に関するノートブックです。

## ノートブック一覧

- **`02_feature_extraction.ipynb`** - 音声特徴量の抽出
  - メルスペクトログラムの抽出
  - F0（基本周波数）の抽出
  - 特徴量の保存

- **`03_corpus_analysis.ipynb`** - コーパス分析
  - 音素カバレッジの分析
  - 音素統計情報の可視化
  - 効率的な文セットの探索

- **`04_feature_density.ipynb`** - 特徴量密度分析
  - 特徴量密度の計算
  - 高密度文の選定
  - 可視化

- **`05_attention_analysis.ipynb`** - Attention機構の分析
  - Attention Mapの可視化
  - 重要特徴量の分析

## 実行順序の推奨

1. `02_feature_extraction.ipynb` - 特徴量を抽出
2. `03_corpus_analysis.ipynb` - コーパスを分析
3. `04_feature_density.ipynb` - 特徴量密度を分析
4. `05_attention_analysis.ipynb` - Attentionを分析（モデル学習後）

