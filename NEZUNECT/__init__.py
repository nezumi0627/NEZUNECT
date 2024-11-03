from typing import Any, Dict, List, Optional

from requests import Session

from .api.bookmarks import BookmarksAPI
from .api.messages import MessagesAPI
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
        self.session = Session()
        self._initialize_apis()

    def _initialize_apis(self):
        """Initialize all API instances with shared session"""
        load_cookies(self.cookie)
        self.notify_api = NotifyAPI(session=self.session)
        self.bookmarks_api = BookmarksAPI(session=self.session)
        self.posts_api = PostsAPI(session=self.session)
        self.profile_api = ProfileAPI(session=self.session)
        self.sessions_api = SessionsAPI(session=self.session)
        self.settings_api = SettingsAPI(session=self.session)
        self.verify_api = VerifyAPI(session=self.session)
        self.messages_api = MessagesAPI(session=self.session)

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

    def change_custom_color(self, theme: str) -> Dict[str, Any]:
        return self.settings_api.change_custom_color(theme)

    def change_notification_sound(self, notification_sound: bool) -> Dict[str, Any]:
        return self.settings_api.change_notification_sound(notification_sound)

    def verify_email(self, email: str, code: str) -> Dict[str, Any]:
        return self.verify_api.verify_email(email, code)

    def get_top_posts(self, skip: int = 0) -> Dict[str, Any]:
        return self.posts_api.get_top_posts(skip)

    def change_messages_following_only(self, following_only: bool) -> Dict[str, Any]:
        return self.settings_api.change_messages_following_only(following_only)

    def send_message(
        self, receiver_id: str, text: str, assets: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        return self.messages_api.send_message(receiver_id, text, assets)

    def get_messages(self, receiver_id: str, skip: int = 0) -> Dict[str, Any]:
        return self.messages_api.get_messages(receiver_id, skip)

    def close(self):
        if hasattr(self, "session") and self.session:
            self.session.close()

    def __enter__(self):
        self._initialize_apis()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
