import logging

from NEZUNECT import NEZUNECT
from NEZUNECT.utils.exceptions import APIError

logging.basicConfig(level=logging.WARNING)


class SessionsExamples:
    def __init__(self):
        self.api = NEZUNECT(cookie="your_cookie_here", debug=True)

    def format_session(self, session):
        return f"""セッションID: {session.get('sessionId', '')}
現在のセッション: {'はい' if session.get('current', False) else 'いいえ'}
IP: {session.get('ip', '')}
デバイス: {session.get('device', '')}
ブラウザ: {session.get('browser', '')}
国: {session.get('country', '')}
地域: {session.get('region', '')}
都市: {session.get('city', '')}
緯度: {session.get('latitude', '')}
経度: {session.get('longitude', '')}
作成日時: {session.get('createdAt', '')}
"""

    def example_get_sessions(self):
        try:
            result = self.api.sessions.get_sessions()
            if result["success"]:
                print("セッション情報:")
                for session in result["data"]:
                    print(self.format_session(session))
                    print("-" * 50)
            else:
                print("セッション情報の取得に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")


def main():
    examples = SessionsExamples()
    examples.example_get_sessions()


if __name__ == "__main__":
    main()
