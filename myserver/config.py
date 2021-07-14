"""
FastAPI server configuration
"""

# pylint: disable=too-few-public-methods

from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    """Server config settings"""

    # Mongo Engine settings
    mongo_uri = config("MONGO_URI")

    # Security settings
    authjwt_secret_key = config("SECRET_KEY")
    salt = config("SALT").encode()

    # FastMail SMTP server settings
    mail_console = config("MAIL_CONSOLE", default=False, cast=bool)
    mail_server = config("MAIL_SERVER", default="smtp.myserver.io")
    mail_port = config("MAIL_PORT", default=587, cast=int)
    mail_username = config("MAIL_USERNAME", default="")
    mail_password = config("MAIL_PASSWORD", default="")
    mail_sender = config("MAIL_SENDER", default="noreply@myserver.io")

    testing = config("TESTING", default=False, cast=bool)


CONFIG = Settings()
