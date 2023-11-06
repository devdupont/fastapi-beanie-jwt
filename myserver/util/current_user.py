"""Current user dependency."""

from fastapi import HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from myserver.models.user import User
from myserver.jwt import access_security, user_from_credentials


async def current_user(
    auth: JwtAuthorizationCredentials = Security(access_security)
) -> User:
    """Return the current authorized user."""
    if not auth:
        raise HTTPException(401, "No authorization credentials found")
    user = await user_from_credentials(auth)
    if user is None:
        raise HTTPException(404, "Authorized user could not be found")
    return user
