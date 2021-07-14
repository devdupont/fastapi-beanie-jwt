"""
Authentication tests
"""

import pytest
from httpx import AsyncClient

from tests.data import add_empty_user
from tests.util import auth_payload


@pytest.mark.asyncio
async def test_not_authorized(client: AsyncClient) -> None:
    """Test user not authorized if required"""
    resp = await client.get("/user")
    assert resp.status_code == 401
    headers = {"AUTHORIZATION": "Bearer eyJ0eXAiOiJKV1QiLCJhbG"}
    resp = await client.get("/user", headers=headers)
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_refresh(client: AsyncClient) -> None:
    """Test refresh token updates access token"""
    await add_empty_user()
    # Check login
    auth = await auth_payload(client, "empty@test.io")
    headers = {"AUTHORIZATION": "Bearer " + auth.access_token}
    resp = await client.get("/user", headers=headers)
    assert resp.status_code == 200
    # Token refresh
    headers = {"AUTHORIZATION": "Bearer " + auth.refresh_token}
    resp = await client.post("/auth/refresh", headers=headers)
    assert resp.status_code == 200
    # Check second call
    headers = {"AUTHORIZATION": "Bearer " + resp.json()["access_token"]}
    resp = await client.get("/user", headers=headers)
    assert resp.status_code == 200
