"""Authentication tests."""

import pytest
from httpx import AsyncClient

from tests.data import add_empty_user
from tests.util import auth_header_token, auth_payload


@pytest.mark.asyncio
async def test_not_authorized(client: AsyncClient) -> None:
    """Test user not authorized if required."""
    resp = await client.get("/user")
    assert resp.status_code == 401
    headers = auth_header_token("eyJ0eXAiOiJKV1QiLCJhbG")
    resp = await client.get("/user", headers=headers)
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_refresh(client: AsyncClient) -> None:
    """Test refresh token updates access token."""
    email = await add_empty_user()
    # Check login
    auth = await auth_payload(client, email)
    headers = auth_header_token(auth.access_token)
    resp = await client.get("/user", headers=headers)
    assert resp.status_code == 200
    # Token refresh
    headers = auth_header_token(auth.refresh_token)
    resp = await client.post("/auth/refresh", headers=headers)
    assert resp.status_code == 200
    # Check second call
    headers = auth_header_token(resp.json()["access_token"])
    resp = await client.get("/user", headers=headers)
    assert resp.status_code == 200
