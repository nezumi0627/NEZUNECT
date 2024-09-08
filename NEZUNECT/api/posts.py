from typing import Any, Dict, List

import requests

from ..config import Config
from ..utils.agent import Headers
from ..utils.cookies import load_cookies
from ..utils.exceptions import APIError


class PostsAPI:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.headers = Headers.get_json("home")
        self.cookies = load_cookies()

    def create_post(
        self, text: str, assets: List[str] = [], scope: str = "public"
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.POSTS}"
        data = {"text": text, "assets": assets, "scope": scope}

        try:
            response = requests.post(
                url, headers=self.headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("post", {})}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"投稿の作成に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def like_post(self, post_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.LIKE_POST.format(post_id=post_id)}"

        try:
            response = requests.post(url, headers=self.headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"投稿へのいいねに失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def post_quote(
        self, text: str, quote_id: str, assets: List[str] = [], scope: str = "public"
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.POSTS}"
        headers = Headers.get_plain_text(f"posts/{quote_id}")
        data = {"text": text, "assets": assets, "quoteId": quote_id, "scope": scope}

        try:
            response = requests.post(
                url, headers=headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("post", {})}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"引用投稿の作成に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def post_reaction(self, post_id: str, emoji: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.REACTIONS.format(post_id=post_id, emoji=emoji)}"
        headers = Headers.get_plain_text(f"posts/{post_id}")
        data = {"emoji": emoji}

        try:
            response = requests.post(
                url, headers=headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"リアクションの追加に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def post_reply(
        self, text: str, reply_to_id: str, assets: List[str] = [], scope: str = "public"
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.POSTS}"
        headers = Headers.get_plain_text("home")
        data = {
            "text": text,
            "assets": assets,
            "replyToId": reply_to_id,
            "scope": scope,
        }

        try:
            response = requests.post(
                url, headers=headers, cookies=self.cookies, json=data
            )
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("post", {})}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"返信の作成に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def post_repost(self, post_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.REPOST.format(post_id=post_id)}"
        headers = Headers.get("home")

        try:
            response = requests.post(url, headers=headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"リポストの作成に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def search_post(
        self, query: str, skip: int = 0, hours: int = 168
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.SEARCH_POSTS}?query={query}&skip={skip}&hours={hours}"
        headers = Headers.get_json("search")

        try:
            response = requests.get(url, headers=headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("posts", [])}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"投稿の検索に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )

    def get_top_posts(self, skip: int = 0, hours: int = 48) -> Dict[str, Any]:
        url = f"{self.base_url}{Config.Endpoints.TOP_POSTS}?skip={skip}&hours={hours}"
        headers = Headers.get_json("search")

        try:
            response = requests.get(url, headers=headers, cookies=self.cookies)
            response.raise_for_status()
            result = response.json()
            return {"success": True, "data": result.get("posts", [])}
        except requests.exceptions.RequestException as e:
            raise APIError(
                f"トップ投稿の取得に失敗しました: {str(e)}",
                status_code=response.status_code if hasattr(e, "response") else None,
            )
