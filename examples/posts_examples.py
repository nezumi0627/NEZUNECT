import logging

from nnezunect import NNEZUNECT
from nnezunect.utils.exceptions import APIError

logging.basicConfig(level=logging.WARNING)


class PostsExamples:
    def __init__(self):
        self.api = NNEZUNECT()

    def format_post(self, post):
        return f"""投稿ID: {post.get('postId', '')}
テキスト: {post.get('text', '')}
作成日時: {post.get('createdAt', '')}
いいね数: {post.get('likeCount', 0)}
リポスト数: {post.get('repostCount', 0)}
"""

    def example_create_post(self):
        try:
            text = input("投稿内容を入力してください: ")
            result = self.api.posts.create_post(text)
            if result["success"]:
                print("投稿が正常に作成されました。")
                print(self.format_post(result["data"]))
            else:
                print("投稿の作成に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_like_post(self):
        try:
            post_id = input("いいねする投稿のIDを入力してください: ")
            result = self.api.posts.like_post(post_id)
            if result["success"]:
                print("投稿にいいねしました。")
            else:
                print("いいねに失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_post_quote(self):
        try:
            quote_id = input("引用する投稿のIDを入力してください: ")
            text = input("引用投稿の内容を入力してください: ")
            result = self.api.posts.post_quote(text, quote_id)
            if result["success"]:
                print("引用投稿が正常に作成されました。")
                print(self.format_post(result["data"]))
            else:
                print("引用投稿の作成に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_post_reaction(self):
        try:
            post_id = input("リアクションを追加する投稿のIDを入力してください: ")
            emoji = input("追加するリアクション（絵文字）を入力してください: ")
            result = self.api.posts.post_reaction(post_id, emoji)
            if result["success"]:
                print("リアクションが正常に追加されました。")
            else:
                print("リアクションの追加に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_post_reply(self):
        try:
            reply_to_id = input("返信先の投稿IDを入力してください: ")
            text = input("返信内容を入力してください: ")
            result = self.api.posts.post_reply(text, reply_to_id)
            if result["success"]:
                print("返信が正常に投稿されました。")
                print(self.format_post(result["data"]))
            else:
                print("返信の投稿に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_post_repost(self):
        try:
            post_id = input("リポストする投稿のIDを入力してください: ")
            result = self.api.posts.post_repost(post_id)
            if result["success"]:
                print("投稿が正常にリポストされました。")
            else:
                print("リポストに失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_search_post(self):
        try:
            query = input("検索クエリを入力してください: ")
            result = self.api.posts.search_post(query)
            if result["success"]:
                print("検索結果:")
                for post in result["data"]:
                    print(self.format_post(post))
                    print("-" * 30)
            else:
                print("投稿の検索に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")


def main():
    examples = PostsExamples()
    print("1. 投稿の作成")
    print("2. 投稿にいいね")
    print("3. 引用投稿")
    print("4. リアクションの追加")
    print("5. 返信の投稿")
    print("6. リポスト")
    print("7. 投稿の検索")

    choice = input("実行する例を選択してください (1-7): ")

    if choice == "1":
        examples.example_create_post()
    elif choice == "2":
        examples.example_like_post()
    elif choice == "3":
        examples.example_post_quote()
    elif choice == "4":
        examples.example_post_reaction()
    elif choice == "5":
        examples.example_post_reply()
    elif choice == "6":
        examples.example_post_repost()
    elif choice == "7":
        examples.example_search_post()
    else:
        print("無効な選択です。")


if __name__ == "__main__":
    main()
