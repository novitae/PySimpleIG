import requests
from random import choice, randint
from re import findall
from time import sleep
from datetime import datetime
from typing import Any

from .syntaxes import is_sessionid_syntax_correct, is_username_syntax_correct
from .exceptions import InvalidSessionIdError, InvalidCredentialsError, NotConnectedAccount, LoginError, RateLimitError, NotLoggedInError, MissingArgumentsError
from .library import DEFAULT_HEADERS, self_infos_endpoints, URL
from .conversions import sessionid_to_cookies

class Login:
    def check_login(self, session_id: str=None, cookies: dict=None) -> Any:
        """Pass or raise NotLoggedInError
        - choose between session_id or cookies"""
        if not session_id and not cookies:
            raise MissingArgumentsError("session_id or cookies must be filled")
        cookies = sessionid_to_cookies(session_id=session_id) if session_id else cookies

        is_connected = requests.get(
            URL+choice(list(self_infos_endpoints.values())),
            headers=DEFAULT_HEADERS,
            cookies=cookies,
            allow_redirects=False
        ).status_code

        return (True if is_connected == 200 else False)

    def session_id(self, session_id: str) -> None:
        """Login to instagram via sessionid."""
        if not is_sessionid_syntax_correct(session_id=session_id):
            raise InvalidSessionIdError(f'"{session_id}" is not respecting instagram sessionid syntax')

        if not self.check_login(session_id=session_id):
            raise NotConnectedAccount(f'"{session_id} is not connected to any acount"')

        return sessionid_to_cookies(session_id=session_id)

    def credentials_login(self, username: str, password: str) -> None:
        """Login to instagram via credentials. Not supporting 2FA."""
        if not is_username_syntax_correct(username=username):
            raise InvalidCredentialsError(f'"{username}" is not respecting instagram usernames syntaxes')
        
        session = requests.Session(headers={
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Host": "www.instagram.com",
            "Origin": "https://www.instagram.com",
            "Referer": URL,
            "X-Instagram-AJAX": "7a3a3e64fa87",
            "X-Requested-With": "XMLHttpRequest"
            })
        session.headers.update(DEFAULT_HEADERS)

        csrf = findall(r"csrf_token\":\"(.*?)\"", session.get(URL).text)[0]
        if not csrf:
            raise RateLimitError("no csrf found during login, wait a bit or change of account")
        
        session.headers.update({"x-csrftoken": csrf})
        sleep(randint(1, 2))

        postResp = session.post(
            f"{URL}accounts/login/ajax/",
            data={
                "username": username,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(int(
                    datetime.now().timestamp()), password
                    )
                },
            allow_redirects=True
            )
        response_data = postResp.json()

        if "two_factor_required" in response_data:
            raise LoginError("Disable 2-factor authentication to login.")
        elif "message" in response_data and response_data.get("message") == "checkpoint_required":
            raise LoginError("Check Instagram app for a security confirmation.")
        try:
            if not response_data["authenticated"]:
                raise LoginError("invalid credentials.")
        except KeyError:
            if response_data.get("spam"):
                raise RateLimitError("login failed. Wait a bit before try again, or use sessionid.")
        else:
            raise LoginError("unknown error")

        return self.session_id(session_id=postResp.cookies["sessionid"])