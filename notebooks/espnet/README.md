# ESPNet Notebooks

ESPNet-VITSモデルに関するノートブックです。

## ノートブック一覧

- **`05_espnet_training.ipynb`** - ESPNet-VITSモデルの学習
  - 3つのデータセット条件（full100, phone_min4, feat_top10）での学習
  - JSUTで事前学習済みモデルからFine-tuning
  - 評価音声の生成

## データセット

- **full100**: 全100文
- **phone_min4**: 音素カバレッジ最小4文
- **feat_top10**: 特徴量密度トップ10文

