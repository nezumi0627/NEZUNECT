class UserAgent:
    @staticmethod
    def get():
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"


class Referer:
    @staticmethod
    def get(page: str) -> str:
        return f"https://subnect.com/{page}"


class Headers:
    @staticmethod
    def get(page: str, content_type: str = "application/json") -> dict:
        headers = {
            "User-Agent": UserAgent.get(),
            "Referer": Referer.get(page),
            "Content-Type": content_type,
            "Origin": "https://subnect.com",
            "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
        }
        return headers

    @staticmethod
    def get_json(page: str) -> dict:
        return Headers.get(page, "application/json")

    @staticmethod
    def get_plain_text(page: str) -> dict:
        return Headers.get(page, "text/plain;charset=UTF-8")
