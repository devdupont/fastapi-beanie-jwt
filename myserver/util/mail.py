"""Mail server config."""

from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType

from myserver.config import CONFIG

mail_conf = ConnectionConfig(
    MAIL_USERNAME=CONFIG.mail_username,
    MAIL_PASSWORD=CONFIG.mail_password,
    MAIL_FROM=CONFIG.mail_sender,
    MAIL_PORT=CONFIG.mail_port,
    MAIL_SERVER=CONFIG.mail_server,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
)

mail = FastMail(mail_conf)


async def send_verification_email(email: str, token: str) -> None:
    """Send user verification email."""
    # Change this later to public endpoint
    url = CONFIG.root_url + "/mail/verify/" + token
    if CONFIG.mail_console:
        print("POST to " + url)
    else:
        message = MessageSchema(
            recipients=[email],
            subject="MyServer Email Verification",
            body=f"Welcome to MyServer! We just need to verify your email to begin: {url}",
            subtype=MessageType.plain,
        )
        await mail.send_message(message)


async def send_password_reset_email(email: str, token: str) -> None:
    """Send password reset email."""
    # Change this later to public endpoint
    url = CONFIG.root_url + "/register/reset-password/" + token
    if CONFIG.mail_console:
        print("POST to " + url)
    else:
        message = MessageSchema(
            recipients=[email],
            subject="MyServer Password Reset",
            body=f"Click the link to reset your MyServer account password: {url}\nIf you did not request this, please ignore this email",
            subtype=MessageType.plain,
        )
        await mail.send_message(message)
