from flask import request
from requests import Response
from src.config.config import CONFIG


class MailGun():
    @staticmethod
    def sendMail(to, subject, title, link) -> Response:
        return request.post(
            f"{CONFIG.MAILGUN_API_BASE_URL}/messages",
            auth=('api', CONFIG.MAILGUN_API_KEY),
            data={
                "from": f"{title} <{CONFIG.MAILGUN_EMAIL}>",
                "to": to,
                "subject": subject,
                "text": f"Please click the link to confirm your registration: {link}"
            }

        )
        
        
mail_gunner = MailGun.sendMail
