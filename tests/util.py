"""Common test utilities."""

from httpx import AsyncClient

from myserver.models.auth import RefreshToken


def auth_header_token(token: str) -> dict[str, str]:
    """Create authorization headers with a token value."""
    return {"Authorization": f"Bearer {token}"}


async def auth_payload(
    client: AsyncClient, email: str, password: str | None = None
) -> RefreshToken:
    """Return the login auth payload for an email."""
    data = {"email": email, "password": password or email}
    resp = await client.post("/auth/login", json=data)
    return RefreshToken(**resp.json())


async def auth_headers(
    client: AsyncClient, email: str, password: str | None = None
) -> dict[str, str]:
    """Return the authorization headers for an email."""
    auth = await auth_payload(client, email, password)
    return auth_header_token(auth.access_token)
