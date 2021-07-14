"""
Test data handlers
"""

from datetime import datetime, timezone

from myserver.models.user import User
from myserver.util.password import hash_password


async def add_empty_user() -> None:
    """Adds test users to user collection"""
    empty_user = User(
        email="empty@test.io",
        password=hash_password("empty@test.io"),
        email_confirmed_at=datetime.now(tz=timezone.utc),
    )
    await empty_user.create()
