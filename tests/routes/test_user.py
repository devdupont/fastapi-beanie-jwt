"""User information tests."""

import pytest
from httpx import AsyncClient

from tests.data import add_empty_user
from tests.util import auth_headers


@pytest.mark.asyncio
async def test_user_get(client: AsyncClient) -> None:
    """Test user endpoint returns authorized user."""
    email = await add_empty_user()
    auth = await auth_headers(client, email)
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == email


@pytest.mark.asyncio
async def test_user_update(client: AsyncClient) -> None:
    """Test updating user fields."""
    email = await add_empty_user()
    name, key = "Empty", "first_name"
    auth = await auth_headers(client, email)
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == email
    assert data[key] is None
    # Update user
    name = "Tester"
    resp = await client.patch("/user", headers=auth, json={key: name})
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == email
    assert data[key] == name
    # Check persistance
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == email
    assert data[key] == name


@pytest.mark.asyncio
async def test_user_update_email(client: AsyncClient) -> None:
    """Test updating user email."""
    email = await add_empty_user()
    new_email, key = "test_replace@test.io", "email"
    auth = await auth_headers(client, email)
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 200
    data = resp.json()
    assert data[key] == email
    # Update email
    resp = await client.patch("/user", headers=auth, json={key: new_email})
    assert resp.status_code == 200
    data = resp.json()
    assert data[key] == new_email
    # Check old email
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 404
    # Check persistance
    auth = await auth_headers(client, new_email, email)
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 200
    data = resp.json()
    assert data[key] == new_email


@pytest.mark.asyncio
async def test_user_delete(client: AsyncClient) -> None:
    """Test deleting a user from the database."""
    email = await add_empty_user()
    auth = await auth_headers(client, email)
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == email
    # Delete user
    resp = await client.delete("/user", headers=auth)
    assert resp.status_code == 204
    # Check deletion
    resp = await client.get("/user", headers=auth)
    assert resp.status_code == 404
