"""
Server main runtime
"""

# pylint: disable=unused-import

from myserver import jwt
from myserver.app import app
from myserver.routes.auth import router as AuthRouter
from myserver.routes.mail import router as MailRouter
from myserver.routes.register import router as RegisterRouter
from myserver.routes.user import router as UserRouter


app.include_router(AuthRouter)
app.include_router(MailRouter)
app.include_router(RegisterRouter)
app.include_router(UserRouter)
