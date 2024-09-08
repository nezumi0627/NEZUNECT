import logging

from NEZUNECT import NEZUNECT
from NEZUNECT.utils.exceptions import APIError

logging.basicConfig(level=logging.WARNING)


class NotifyExamples:
    def __init__(self):
        self.api = NEZUNECT(cookie="your_cookie_here", debug=True)

    def format_notification(self, notification):
        formatted = f"タイプ: {notification.get('type', 'unknown')}\n"
        formatted += f"作成日時: {notification.get('createdAt', '')}\n"
        formatted += (
            f"既読: {'はい' if notification.get('read', False) else 'いいえ'}\n"
        )

        profiles = notification.get("profiles", [])
        if profiles:
            formatted += "プロフィール:\n"
            for profile in profiles:
                formatted += self.format_profile(profile) + "\n"

        post = notification.get("post", {})
        if post:
            formatted += "投稿:\n"
            formatted += self.format_post(post) + "\n"

        return formatted

    def format_profile(self, profile):
        return f"""  ユーザー名: {profile.get('username', '')}
  ニックネーム: {profile.get('nickname', '')}
  プロフィールID: {profile.get('profileId', '')}
  自己紹介: {profile.get('bio', '未設定')}
  アイコン: {profile.get('icon', {}).get('assetUrl', '未設定')}
  公式アカウント: {'はい' if profile.get('official', False) else 'いいえ'}
  作成日時: {profile.get('createdAt', '')}"""

    def format_post(self, post):
        reactions = ", ".join(
            [f"{r['emoji']}({r['count']})" for r in post.get("reactions", [])]
        )
        return f"""  投稿ID: {post.get('postId', '')}
  テキスト: {post.get('text', '')}
  作成日時: {post.get('createdAt', '')}
  リポスト: {'はい' if post.get('repost', False) else 'いいえ'}
  編集済み: {'はい' if post.get('edited', False) else 'いいえ'}
  返信数: {post.get('repliesCount', 0)}
  引用数: {post.get('quoteCount', 0)}
  リポスト数: {post.get('repostCount', 0)}
  リアクション数: {post.get('reactionCount', 0)}
  いいね数: {post.get('likeCount', 0)}
  スコープ: {post.get('scope', '')}
  リアクション: {reactions}
  ユーザーのリアクション: {post.get('userReaction', '未設定')}
  いいね済み: {'はい' if post.get('isLiked', False) else 'いいえ'}
  リポスト済み: {'はい' if post.get('isReposted', False) else 'いいえ'}"""

    def example_get_notifications(self):
        try:
            result = self.api.notify.get_notifications()
            if result["success"]:
                print("通知一覧:")
                for notification in result["data"]:
                    print(self.format_notification(notification))
                    print("-" * 50)
            else:
                print("通知の取得に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")


def main():
    examples = NotifyExamples()
    examples.example_get_notifications()


if __name__ == "__main__":
    main()
