# Global
class RateLimitError(Exception): pass
class MissingArgumentsError(Exception): pass

# Login
class InvalidSessionIdError(Exception): pass
class InvalidCredentialsError(Exception): pass
class NotConnectedAccount(Exception): pass
class LoginError(Exception): pass
class NotLoggedInError(Exception): pass

# __a1
class UserNotFoundError(Exception): pass