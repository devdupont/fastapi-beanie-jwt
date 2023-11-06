"""FastAPI JWT configuration."""

from datetime import timedelta

from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer, JwtRefreshBearer

from myserver.config import CONFIG
from myserver.models.user import User

ACCESS_EXPIRES = timedelta(minutes=15)
REFRESH_EXPIRES = timedelta(days=30)

access_security = JwtAccessBearer(
    CONFIG.authjwt_secret_key,
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)

refresh_security = JwtRefreshBearer(
    CONFIG.authjwt_secret_key,
    access_expires_delta=ACCESS_EXPIRES,
    refresh_expires_delta=REFRESH_EXPIRES,
)


async def user_from_credentials(auth: JwtAuthorizationCredentials) -> User | None:
    """Return the user associated with auth credentials."""
    return await User.by_email(auth.subject["username"])


async def user_from_token(token: str) -> User | None:
    """Return the user associated with a token value."""
    payload = access_security._decode(token)
    return await User.by_email(payload["subject"]["username"])
