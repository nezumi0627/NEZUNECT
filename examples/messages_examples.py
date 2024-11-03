import logging

from NEZUNECT import NEZUNECT
from NEZUNECT.utils.exceptions import APIError

logging.basicConfig(level=logging.WARNING)


class MessagesExamples:
    def __init__(self):
        self.api = NEZUNECT(cookie="cookie.json", debug=True)

    def format_message(self, message_data):
        return f"""メッセージID: {message_data.get('messageId', '')}
テキスト: {message_data.get('text', '')}
作成日時: {message_data.get('createdAt', '')}
送信者: {self.format_profile(message_data.get('profile', {}))}
受信者: {self.format_profile(message_data.get('receiver', {}))}
アセット: {', '.join(message_data.get('assets', []))}
リアクション: {', '.join(str(r) for r in message_data.get('reactions', []))}
"""

    def format_profile(self, profile):
        return f"""
  ユーザー名: {profile.get('username', '')}
  ニックネーム: {profile.get('nickname', '')}
  プロフィールID: {profile.get('profileId', '')}
  Bio: {profile.get('bio', '未設定')}"""

    def example_send_message(self):
        try:
            receiver_id = input(
                "メッセージを送信する相手のプロフィールIDを入力してください: "
            )
            text = input("メッセージの内容を入力してください: ")
            result = self.api.send_message(receiver_id, text)

            if result["success"]:
                print("メッセージが正常に送信されました。")
                print(self.format_message(result["data"]["messageData"]))
            else:
                print("メッセージの送信に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")


def main():
    examples = MessagesExamples()
    examples.example_send_message()


if __name__ == "__main__":
    main()
