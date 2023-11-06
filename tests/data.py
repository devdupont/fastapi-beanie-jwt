"""Test data handlers."""

from datetime import datetime, timedelta, UTC

from myserver.models.user import User
from myserver.util.password import hash_password


def make_user(email: str, offset: int | None = 0) -> User:
    """Return a minimal, uncommitted User."""
    now = None
    if offset is not None:
        now = datetime.now(tz=UTC) - timedelta(days=offset)
    user = User(
        email=email,
        password=hash_password(email),
        email_confirmed_at=now,
    )
    return user


async def add_empty_user() -> str:
    """Add minimal user to user collection."""
    user = make_user("empty@test.io")
    await user.create()
    return user.email
