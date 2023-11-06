"""User router."""

from fastapi import APIRouter, Depends, HTTPException, Response, Security
from fastapi_jwt import JwtAuthorizationCredentials

from myserver.models.user import User, UserOut, UserUpdate
from myserver.jwt import access_security
from myserver.util.current_user import current_user

router = APIRouter(prefix="/user", tags=["User"])


@router.get("", response_model=UserOut)
async def get_user(user: User = Depends(current_user)):  # type: ignore[no-untyped-def]
    """Return the current user."""
    return user


@router.patch("", response_model=UserOut)
async def update_user(update: UserUpdate, user: User = Depends(current_user)):  # type: ignore[no-untyped-def]
    """Update allowed user fields."""
    fields = update.model_dump(exclude_unset=True)
    if new_email := fields.pop("email", None):
        if new_email != user.email:
            if await User.by_email(new_email) is not None:
                raise HTTPException(400, "Email already exists")
            user.update_email(new_email)
    user = user.model_copy(update=fields)
    await user.save()
    return user


@router.delete("")
async def delete_user(
    auth: JwtAuthorizationCredentials = Security(access_security)
) -> Response:
    """Delete current user."""
    await User.find_one(User.email == auth.subject["username"]).delete()
    return Response(status_code=204)
