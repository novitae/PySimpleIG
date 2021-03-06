import requests

from .library import URL, DEFAULT_HEADERS
from .exceptions import UserNotFoundError, ResponseError

class A1:
    def __init__(self, cookies: dict) -> None:
        self.cookies = cookies
        self.headers = DEFAULT_HEADERS

    def infos(self, username: str) -> dict:
        """Adds important informations to the attributes of the class"""
        api = requests.get(
            f'{URL}{username}/?__a=1',
            cookies=self.cookies,
            headers=self.headers,
            allow_redirects=False
            )
            
        if api.status_code not in [200,404]:
            raise ResponseError(f"A1.infos() responded {api.status_code}")
        elif api.status_code == 404:
            raise UserNotFoundError(f"{username} has not been found")

        api = api.json()["graphql"]["user"]
        keys = [
            "biography",
            "external_url",
            (("edge_followed_by","count"),"followers"),
            (("edge_follow","count"),"following"),
            "full_name",
            "id",
            "is_private",
            "is_verified",
            "profile_pic_url_hd",
            "username",
            "followed_by_viewer",
            (("edge_owner_to_timeline_media","count"),"posts")
        ]

        retour = {}
        for key in keys:
            if type(key) is tuple:
                (pth1, pth2), name = key
                retour[name] = api[pth1][pth2]
            else:
                retour[key] = api[key]

        return retour