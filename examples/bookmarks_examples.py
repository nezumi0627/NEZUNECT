import logging

from NEZUNECT import NEZUNECT
from NEZUNECT.utils.exceptions import APIError

logging.basicConfig(level=logging.WARNING)


class BookmarksExamples:
    def __init__(self):
        self.api = NEZUNECT(cookie="your_cookie_here", debug=True)

    def format_bookmark_folder(self, folder):
        return f"""フォルダID: {folder.get('folderId', '')}
名前: {folder.get('name', '')}
ブックマーク数: {folder.get('bookmarksCount', 0)}
"""

    def example_get_bookmarks(self):
        try:
            result = self.api.bookmarks.get_bookmarks()
            if result["success"]:
                print("ブックマークフォルダ:")
                for folder in result["data"]:
                    print(self.format_bookmark_folder(folder))
                    print("-" * 30)
            else:
                print("ブックマークの取得に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_add_bookmark(self):
        try:
            folder_id = input("ブックマークを追加するフォルダIDを入力してください: ")
            post_id = input("ブックマークに追加する投稿IDを入力してください: ")
            result = self.api.bookmarks.add_bookmark(folder_id, post_id)
            if result["success"]:
                print("ブックマークが正常に追加されました。")
                print("追加されたブックマーク情報:")
                print(result["data"])
            else:
                print("ブックマークの追加に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_create_bookmark(self):
        try:
            name = input("作成するブックマークフォルダの名前を入力してください: ")
            result = self.api.bookmarks.create_bookmark(name)
            if result["success"]:
                print("ブックマークフォルダが正常に作成されました。")
                print("作成されたフォルダ情報:")
                print(self.format_bookmark_folder(result["data"]))
            else:
                print("ブックマークフォルダの作成に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")


def main():
    examples = BookmarksExamples()
    print("1. ブックマークフォルダの取得")
    print("2. ブックマークの追加")
    print("3. ブックマークフォルダの作成")

    choice = input("実行する例を選択してください (1-3): ")

    if choice == "1":
        examples.example_get_bookmarks()
    elif choice == "2":
        examples.example_add_bookmark()
    elif choice == "3":
        examples.example_create_bookmark()
    else:
        print("無効な選択です。")


if __name__ == "__main__":
    main()
