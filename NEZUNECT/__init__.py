from typing import Any, Dict, Optional

from .api.bookmarks import BookmarksAPI
from .api.notify import NotifyAPI
from .api.posts import PostsAPI
from .api.profile import ProfileAPI
from .api.sessions import SessionsAPI
from .api.settings import SettingsAPI
from .api.verify import VerifyAPI
from .utils.cookies import load_cookies


class NEZUNECT:
    def __init__(self, cookie: str, debug: bool = False):
        self.cookie = cookie
        self.debug = debug
        self.notify_api = None
        self.bookmarks_api = None
        self.posts_api = None
        self.profile_api = None
        self.sessions_api = None
        self.settings_api = None
        self.verify_api = None

    def initialize(self):
        load_cookies(self.cookie)
        self.notify_api = NotifyAPI()
        self.bookmarks_api = BookmarksAPI()
        self.posts_api = PostsAPI()
        self.profile_api = ProfileAPI()
        self.sessions_api = SessionsAPI()
        self.settings_api = SettingsAPI()
        self.verify_api = VerifyAPI()

    def get_profile(self, username: str) -> Dict[str, Any]:
        return self.profile_api.get_profile(username)

    def create_post(
        self, text: str, assets: Optional[list] = None, scope: str = "public"
    ) -> Dict[str, Any]:
        if assets is None:
            assets = []
        return self.posts_api.create_post(text, assets, scope)

    def get_notifications(self, skip: int = 0) -> Dict[str, Any]:
        return self.notify_api.get_notifications(skip)

    def get_bookmarks(self) -> Dict[str, Any]:
        return self.bookmarks_api.get_bookmarks()

    def add_bookmark(self, folder_id: str, post_id: str) -> Dict[str, Any]:
        return self.bookmarks_api.add_bookmark(folder_id, post_id)

    def create_bookmark_folder(self, name: str) -> Dict[str, Any]:
        return self.bookmarks_api.create_bookmark_folder(name)

    def like_post(self, post_id: str) -> Dict[str, Any]:
        return self.posts_api.like_post(post_id)

    def post_quote(
        self,
        text: str,
        quote_id: str,
        assets: Optional[list] = None,
        scope: str = "public",
    ) -> Dict[str, Any]:
        if assets is None:
            assets = []
        return self.posts_api.post_quote(text, quote_id, assets, scope)

    def post_reaction(self, post_id: str, emoji: str) -> Dict[str, Any]:
        return self.posts_api.post_reaction(post_id, emoji)

    def post_reply(
        self,
        text: str,
        reply_to_id: str,
        assets: Optional[list] = None,
        scope: str = "public",
    ) -> Dict[str, Any]:
        if assets is None:
            assets = []
        return self.posts_api.post_reply(text, reply_to_id, assets, scope)

    def post_repost(self, post_id: str) -> Dict[str, Any]:
        return self.posts_api.post_repost(post_id)

    def search_post(
        self, query: str, skip: int = 0, hours: int = 168
    ) -> Dict[str, Any]:
        return self.posts_api.search_post(query, skip, hours)

    def change_profile_name(self, nickname: str) -> Dict[str, Any]:
        return self.profile_api.change_profile_name(nickname)

    def change_profile_bio(self, bio: str) -> Dict[str, Any]:
        return self.profile_api.change_profile_bio(bio)

    def change_profile_email(self, email: str) -> Dict[str, Any]:
        return self.profile_api.change_profile_email(email)

    def change_profile_id(self, new_username: str) -> Dict[str, Any]:
        return self.profile_api.change_profile_id(new_username)

    def change_profile_name_bio(self, nickname: str, bio: str) -> Dict[str, Any]:
        return self.profile_api.change_profile_name_bio(nickname, bio)

    def post_profile_pin(self, post_id: str) -> Dict[str, Any]:
        return self.profile_api.post_profile_pin(post_id)

    def get_sessions(self, skip: int = 0) -> Dict[str, Any]:
        return self.sessions_api.get_sessions(skip)

    def change_dark_mode(self, dark_mode: bool) -> Dict[str, Any]:
        return self.settings_api.change_dark_mode(dark_mode)

    def change_language(self, language: str) -> Dict[str, Any]:
        return self.settings_api.change_language(language)

    def change_theme(self, theme: str) -> Dict[str, Any]:
        return self.settings_api.change_theme(theme)

    def change_notification_sound(self, notification_sound: bool) -> Dict[str, Any]:
        return self.settings_api.change_notification_sound(notification_sound)

    def verify_email(self, email: str, code: str) -> Dict[str, Any]:
        return self.verify_api.verify_email(email, code)

    def close(self):
        # セッションをクローズする処理があれば、ここに実装します
        pass

    def __enter__(self):
        self.initialize()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
