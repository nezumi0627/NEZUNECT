class APIError(Exception):
    """APIリクエストに関連するエラーを表す例外クラス。"""

    def __init__(self, message: str, status_code: int = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
