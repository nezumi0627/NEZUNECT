import logging

from nnezunect import NNEZUNECT
from nnezunect.utils.exceptions import APIError

logging.basicConfig(level=logging.WARNING)


class SettingsExamples:
    def __init__(self):
        self.api = NNEZUNECT()

    def example_change_dark_mode(self):
        try:
            print("ダークモードを設定しますか？")
            print("1. はい（ダークモード）")
            print("2. いいえ（ライトモード）")
            choice = input("選択肢の番号を入力してください (1/2): ")

            dark_mode = choice == "1"
            result = self.api.settings.change_dark_mode(dark_mode)
            if result["success"]:
                print(
                    f"テーマが{'ダークモード' if dark_mode else 'ライトモード'}に正常に変更されました。"
                )
            else:
                print("テーマの変更に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_change_language(self):
        try:
            print("言語を選択してください:")
            print("1. 自動")
            print("2. 日本語")
            print("3. 英語")
            choice = input("選択肢の番号を入力してください (1/2/3): ")

            language = "auto" if choice == "1" else "ja" if choice == "2" else "en"
            result = self.api.settings.change_language(language)
            if result["success"]:
                print(f"言語設定が {language} に正常に更新されました。")
            else:
                print("言語設定の変更に失敗しました。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_change_notification_setting(self):
        try:
            print("変更する通知設定を選択してください：")
            print("1. アプリ内フォロー通知")
            print("2. アプリ内引用通知")
            print("3. アプリ内リポスト通知")
            choice = input("選択肢の番号を入力してください: ")
            value = (
                input(
                    "通知をONにする場合は'on'、OFFにする場合は'off'を入力してください: "
                ).lower()
                == "on"
            )

            settings = ["appFollows", "appQuotes", "appReposts"]
            if choice.isdigit() and 1 <= int(choice) <= len(settings):
                result = self.api.settings.change_notification_setting(
                    settings[int(choice) - 1], value
                )
                if result["success"]:
                    print(
                        f"{settings[int(choice) - 1]}の通知設定が{'ON' if value else 'OFF'}に変更されました。"
                    )
                else:
                    print("通知設定の変更に失敗しました。")
            else:
                print("無効な選択です。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")

    def example_custom_color(self):
        try:
            print("変更するカスタムカラーの種類を選択してください：")
            print("1. 背景色")
            print("2. ボーダー色")
            print("3. アクセント色")
            print("4. フォント色")
            choice = input("選択肢の番号を入力してください (1/2/3/4): ")

            color = input("設定する色のHEXコードを入力してください（例: e6e6e6）: ")

            color_types = ["backColor", "borderColor", "accentColor", "fontColor"]
            if choice.isdigit() and 1 <= int(choice) <= len(color_types):
                result = self.api.settings.custom_color(
                    color_types[int(choice) - 1], color
                )
                if result["success"]:
                    print(
                        f"{color_types[int(choice) - 1]}が{color}に正常に変更されました。"
                    )
                else:
                    print("カスタムカラーの変更に失敗しました。")
            else:
                print("無効な選択です。")
        except APIError as e:
            print(f"エラーが発生しました: {str(e)}")


def main():
    examples = SettingsExamples()
    print("1. ダークモードの変更")
    print("2. 言語設定の変更")
    print("3. 通知設定の変更")
    print("4. カスタムカラーの設定")

    choice = input("実行する例を選択してください (1-4): ")

    if choice == "1":
        examples.example_change_dark_mode()
    elif choice == "2":
        examples.example_change_language()
    elif choice == "3":
        examples.example_change_notification_setting()
    elif choice == "4":
        examples.example_custom_color()
    else:
        print("無効な選択です。")


if __name__ == "__main__":
    main()
