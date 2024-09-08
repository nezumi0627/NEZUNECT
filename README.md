# NEZUNECT

NEZUNECT は、ソーシャルネットワーキングプラットフォームである [Subnect](https://subnect.com/) の非公式 API ラッパーです。
このライブラリは、Subnect の機能をCookie🍪で操作するための使いやすいインターフェースを提供します。

[English](README-en.md)

## 機能

- プロフィール情報の取得
- 投稿の作成と検索
- いいねとフォロー機能
- プロフィールの更新
- トップ投稿の取得
- セッションの取得
- 通知の取得
- 通知音の変更
- ブックマークの取得
- ブックマークの追加
- テーマの変更
- 言語の変更
- 通知設定の変更
- メールアドレスの変更
- ユーザー名の変更

## インストール

NEZUNECT は以下の git コマンドを使用してインストールできます：

```
git clone https://github.com/nezumi0627/Nezu-nect-unofficial-api.git
```

## 使用方法

以下は NEZUNECT の使用例です：

```python
from nezunect import NEZUNECT

# NEZUNECTクライアントの初期化
bot = NEZUNECT(cookie="your_cookie_here", debug=True)
bot.initialize()

# プロフィール情報の取得
profile = bot.get_profile("username")
print(f"ニックネーム: {profile['nickname']}")

# 投稿の作成
post_result = bot.create_post("Hello Nezunect-Unofficial-API!")
print(f"投稿が作成されました。投稿ID: {post_result['postId']}")

# セッションの終了
bot.close()
```

より詳細な使用方法については、ドキュメンテーションを参照してください。

## 貢献

貢献は歓迎します！お気軽にプルリクエストを提出してください。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。

## 免責事項

これは非公式の API ラッパーであり、Subnect とは提携しておらず、Subnect によって承認されているものでもありません。自己責任で使用してください。
