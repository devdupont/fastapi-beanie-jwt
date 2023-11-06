"""FastAPI server configuration."""

from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    """Server config settings."""

    root_url: str = config("ROOT_URL", default="http://localhost:8080")

    # Mongo Engine settings
    mongo_uri: str = config("MONGO_URI")

    # Security settings
    authjwt_secret_key: str = config("SECRET_KEY")
    salt: bytes = config("SALT").encode()

    # FastMail SMTP server settings
    mail_console: bool = config("MAIL_CONSOLE", default=False, cast=bool)
    mail_server: str = config("MAIL_SERVER", default="smtp.myserver.io")
    mail_port: int = config("MAIL_PORT", default=587, cast=int)
    mail_username: str = config("MAIL_USERNAME", default="")
    mail_password: str = config("MAIL_PASSWORD", default="")
    mail_sender: str = config("MAIL_SENDER", default="noreply@myserver.io")

    testing: bool = config("TESTING", default=False, cast=bool)


CONFIG = Settings()
