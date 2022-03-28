from re import match

def is_username_syntax_correct(username: str) -> bool:
    """Checks if the username is respecting the instagram username syntax"""
    if match(r"([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)", username):
        return True
    return False

def is_sessionid_syntax_correct(session_id:str) -> bool:
    """Checks if the sessionid syntax is correct"""
    if match(r"(?:[0-9]{1,14}%3A[a-zA-Z0-9]{14}%3A[0-9]{1,2})", session_id):
        if int(session_id.split("%3A")[-1]) < 30:
            return True
    return False