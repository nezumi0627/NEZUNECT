from bookmarks_examples import BookmarksExamples
from messages_examples import MessagesExamples
from notify_examples import NotifyExamples
from posts_examples import PostsExamples
from profile_examples import ProfileExamples
from sessions_examples import SessionsExamples
from settings_examples import SettingsExamples


class MainExamples:
    def __init__(self):
        self.bookmarks = BookmarksExamples()
        self.messages = MessagesExamples()
        self.notify = NotifyExamples()
        self.posts = PostsExamples()
        self.profile = ProfileExamples()
        self.sessions = SessionsExamples()
        self.settings = SettingsExamples()

    def show_menu(self):
        print("\nNEZUNECT API Examples")
        print("=" * 50)
        print("1. ブックマーク関連")
        print("2. メッセージ関連")
        print("3. 通知関連")
        print("4. 投稿関連")
        print("5. プロフィール関連")
        print("6. セッション関連")
        print("7. 設定関連")
        print("0. 終了")
        print("=" * 50)

    def run(self):
        while True:
            self.show_menu()
            choice = input("\n実行するカテゴリを選択してください (0-7): ")

            if choice == "0":
                print("プログラムを終了します。")
                break
            elif choice == "1":
                self.run_bookmarks_examples()
            elif choice == "2":
                self.run_messages_examples()
            elif choice == "3":
                self.run_notify_examples()
            elif choice == "4":
                self.run_posts_examples()
            elif choice == "5":
                self.run_profile_examples()
            elif choice == "6":
                self.run_sessions_examples()
            elif choice == "7":
                self.run_settings_examples()
            else:
                print("無効な選択です。")

    def run_bookmarks_examples(self):
        print("\nブックマーク機能の例")
        print("1. ブックマークフォルダの取得")
        print("2. ブックマークの追加")
        print("3. ブックマークフォルダの作成")

        choice = input("実行する機能を選択してください (1-3): ")
        if choice == "1":
            self.bookmarks.example_get_bookmarks()
        elif choice == "2":
            self.bookmarks.example_add_bookmark()
        elif choice == "3":
            self.bookmarks.example_create_bookmark()

    def run_messages_examples(self):
        print("\nメッセージ機能の例")
        print("1. メッセージの送信")

        choice = input("実行する機能を選択してください (1): ")
        if choice == "1":
            self.messages.example_send_message()

    def run_notify_examples(self):
        print("\n通知機能の例")
        print("1. 通知一覧の取得")

        choice = input("実行する機能を選択してください (1): ")
        if choice == "1":
            self.notify.example_get_notifications()

    def run_posts_examples(self):
        print("\n投稿機能の例")
        print("1. 投稿の作成")
        print("2. 投稿にいいね")
        print("3. 引用投稿")
        print("4. リアクションの追加")
        print("5. 返信の投稿")
        print("6. リポスト")
        print("7. 投稿の検索")

        choice = input("実行する機能を選択してください (1-7): ")
        if choice == "1":
            self.posts.example_create_post()
        elif choice == "2":
            self.posts.example_like_post()
        elif choice == "3":
            self.posts.example_post_quote()
        elif choice == "4":
            self.posts.example_post_reaction()
        elif choice == "5":
            self.posts.example_post_reply()
        elif choice == "6":
            self.posts.example_post_repost()
        elif choice == "7":
            self.posts.example_search_post()

    def run_profile_examples(self):
        print("\nプロフィール機能の例")
        print("1. プロフィール名の変更")
        print("2. 自己紹介の変更")
        print("3. メールアドレスの変更")
        print("4. ユーザーIDの変更")
        print("5. プロフィール名と自己紹介の変更")
        print("6. プロフィールピンの投稿")

        choice = input("実行する機能を選択してください (1-6): ")
        if choice == "1":
            self.profile.example_change_profile_name()
        elif choice == "2":
            self.profile.example_change_profile_bio()
        elif choice == "3":
            self.profile.example_change_profile_email()
        elif choice == "4":
            self.profile.example_change_profile_id()
        elif choice == "5":
            self.profile.example_change_profile_name_bio()
        elif choice == "6":
            self.profile.example_post_profile_pin()

    def run_sessions_examples(self):
        print("\nセッション機能の例")
        print("1. セッション情報の取得")

        choice = input("実行する機能を選択してください (1): ")
        if choice == "1":
            self.sessions.example_get_sessions()

    def run_settings_examples(self):
        print("\n設定機能の例")
        print("1. ダークモードの変更")
        print("2. 言語設定の変更")
        print("3. 通知設定の変更")
        print("4. カスタムカラーの設定")

        choice = input("実行する機能を選択してください (1-4): ")
        if choice == "1":
            self.settings.example_change_dark_mode()
        elif choice == "2":
            self.settings.example_change_language()
        elif choice == "3":
            self.settings.example_change_notification_setting()
        elif choice == "4":
            self.settings.example_custom_color()


def main():
    examples = MainExamples()
    examples.run()


if __name__ == "__main__":
    main()
