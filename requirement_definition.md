# RSSリーダー開発 要件定義書

## 1. プロジェクト概要
### 目的
複数のRSSフィードから記事を取得し、整理・表示するRSSリーダーを作成する。ユーザーが一つの画面で全フィードの最新情報を効率的に確認できることを目指す。

### 目標
- **シンプルで使いやすいUI**
- **未読・既読管理とお気に入り管理**
- **フィードの効率的な管理**
- **Inoreaderのようなカード型UIの実現**

---

## 2. 主要要件

### 2.1 フィード管理機能
- フィードの**登録・削除**が可能。
- フィードごとに記事が表示される画面と、**全フィードをまとめて表示する画面**を提供。
- フィードごとに**未読記事の数**を表示する。

### 2.2 記事の表示機能
- 各記事の表示内容：
  - **サムネイル画像**
  - **記事タイトル**
  - **公開日時**
  - **記事概要（省略可能）**
  - **RSSソース名**
- **クリック**で記事の詳細表示またはブラウザで開くリンクを提供。
- **未読・既読の状態**を視覚的に管理（未読は太字など）。
- **重複記事のフィルタリング**（タイトルやリンクの一致を検出）。

### 2.3 記事管理機能
- **既読した記事を手動で削除**する機能。
- 一括で既読記事を削除するオプションを提供。
- **お気に入り機能**で保存した記事の管理が可能。

### 2.4 自動更新機能
- 定期的に新しい記事を取得し、更新する。
- 更新間隔の設定（例：5分、10分、30分）を提供。

---

## 3. 画面設計

### 3.1 サイドバー
- **フィード一覧**：フィードごとに未読記事数を表示。
- **全フィード表示**と**お気に入り記事の表示**をメニューに追加。
- **設定**、**検索**、**通知**ボタンをアイコンで配置。

### 3.2 記事一覧画面
- **カード型レイアウト**で記事を表示。
- 各記事の内容：
  - **サムネイル画像**
  - **タイトル**
  - **公開日時**
  - **RSSソース名**
- **ツールバーのフィルタ機能**：
  - 「全記事」「未読記事のみ」「既読記事を含む」などのフィルタリング。
  - 並び替えオプション：最新順、古い順、フィード名順。
  - **検索バー**を右上に配置。

---

## 4. 技術選定
- **Python + PyQt**：  
  - シンプルなデスクトップアプリでGUIを実装し、カード型UIを再現する。

後にほかの言語を用いてGUIなどをアップデートする可能性あり

---