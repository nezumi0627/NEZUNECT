import logging

from NEZUNECT import NEZUNECT
from NEZUNECT.utils.exceptions import APIError

logging.basicConfig(level=logging.WARNING)


class ProfileExamples:
    def __init__(self):
        self.api = NEZUNECT(cookie="your_cookie_here", debug=True)

    def format_profile(self, profile):
        return f"""ユーザー名: {profile.get('username', '')}
ニックネーム: {profile.get('nickname', '')}
プロフィールID: {profile.get('profileId', '')}
自己紹介: {profile.get('bio', '未設定')}
アイコン: {profile.get('icon', {}).get('assetUrl', '未設定')}
公式アカウント: {'はい' if profile.get('official', False) else 'いいえ'}
作成日時: {profile.get('createdAt', '')}
"""

    def example_change_profile_name(self):
        try:
            new_nickname = input("新しいニックネームを入力してください: ")
            result = self.api.profile.change_profile_name(new_nickname)
            if result["success"]:
                print("ニックネームが正常に変更されました。")
                print(self.format_profile(result["data"]))
            else:
                print("ニックネームの変更に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_change_profile_bio(self):
        try:
            new_bio = input("新しい自己紹介を入力してください: ")
            result = self.api.profile.change_profile_bio(new_bio)
            if result["success"]:
                print("自己紹介が正常に変更されました。")
                print(self.format_profile(result["data"]))
            else:
                print("自己紹介の変更に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_change_profile_email(self):
        try:
            new_email = input("新しいメールアドレスを入力してください: ")
            result = self.api.profile.change_profile_email(new_email)
            if result["success"]:
                print("メールアドレスが正常に変更されました。")
                print("確認メールが送信されました。確認コードを入力してください。")
                verification_code = input("確認コード: ")
                verify_result = self.api.profile.verify_email(
                    new_email, verification_code
                )
                if verify_result["success"]:
                    print("メールアドレスの確認が完了しました。")
                else:
                    print("メールアドレスの確認に失敗しました。")
            else:
                print("メールアドレスの変更に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_change_profile_id(self):
        try:
            new_username = input("新しいユーザーIDを入力してください: ")
            result = self.api.profile.change_profile_id(new_username)
            if result["success"]:
                print("ユーザーIDが正常に変更されました。")
                print(self.format_profile(result["data"]))
            else:
                print("ユーザーIDの変更に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_change_profile_name_bio(self):
        try:
            new_nickname = input("新しいニックネームを入力してください: ")
            new_bio = input("新しい自己紹介を入力してください: ")
            result = self.api.profile.change_profile_name_bio(new_nickname, new_bio)
            if result["success"]:
                print("ニックネームと自己紹介が正常に変更されました。")
                print(self.format_profile(result["data"]))
            else:
                print("ニックネームと自己紹介の変更に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_post_profile_pin(self):
        try:
            post_id = input("ピン留めする投稿のIDを入力してください: ")
            result = self.api.profile.post_profile_pin(post_id)
            if result["success"]:
                print("投稿が正常にピン留めされました。")
                print(f"ピン留めされた投稿ID: {result['data'].get('postId', '')}")
            else:
                print("投稿のピン留めに失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")


def main():
    examples = ProfileExamples()
    print("1. プロフィール名の変更")
    print("2. 自己紹介の変更")
    print("3. メールアドレスの変更")
    print("4. ユーザーIDの変更")
    print("5. プロフィール名と自己紹介の変更")
    print("6. プロフィールピンの投稿")

    choice = input("実行する例を選択してください (1-6): ")

    if choice == "1":
        examples.example_change_profile_name()
    elif choice == "2":
        examples.example_change_profile_bio()
    elif choice == "3":
        examples.example_change_profile_email()
    elif choice == "4":
        examples.example_change_profile_id()
    elif choice == "5":
        examples.example_change_profile_name_bio()
    elif choice == "6":
        examples.example_post_profile_pin()
    else:
        print("無効な選択です。")


if __name__ == "__main__":
    main()
