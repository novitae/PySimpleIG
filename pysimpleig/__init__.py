"""
## PySimpleIG
A simple Python library focused on instagram.
"""

__version__ = "0.1"
__author__ = "novitae"
__all__ = [
    "Login"
]

from .login import Login
from .conversions import (
    sessionid_to_cookies,
    sessionid_to_id,
    sessionid_to_ios_auth,
    sessionid_to_username,
    cookies_to_sessionid
)
from .__a1 import A1