import requests
from json import dumps
from base64 import urlsafe_b64encode

from .exceptions import RateLimitError
from .library import IOS_UA, URL

def cookies_to_sessionid(cookies: dict) -> str:
    """Returns the sessionid cookie value inside the cookies"""
    return cookies["sessionid"]

def sessionid_to_cookies(session_id: str) -> dict:
    """Turns session_id strings to cookies dict for requests"""
    return {"sessionid": session_id}

def id_to_username(session_id: str, user_id: str) -> str:
    """Returns the username of an instagram userid"""
    api = requests.get(
        f'{URL}api/v1/users/{user_id}/info/',
        headers={"User-Agent": IOS_UA},
        cookies={"sessionid":session_id},
        allow_redirects=False
    )
    if api.status_code != 200:
        raise RateLimitError(f"id_to_username api responded {api.status_code}")
    return api.json()['user']['username']

def sessionid_to_id(session_id: str) -> str:
    """Returns the id of the sessionid"""
    return session_id.split("%3A")[0]

def sessionid_to_username(session_id: str) -> str:
    """Returns the username behind the sessionid"""
    return id_to_username(user_id=sessionid_to_id(session_id=session_id))

def sessionid_to_ios_auth(session_id: str) -> dict:
    """Returns iOS instagram auth"""
    auth = urlsafe_b64encode(
        bytes(dumps(
            {"ds_user_id":sessionid_to_id(session_id=session_id),"sessionid":session_id,"should_use_header_over_cookies":True},
            separators=(",",":")
        ), encoding="utf-8")
    ).decode("utf-8")
    return {"Authorization":f"Bearer IGT:2:{auth}"}