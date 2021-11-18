from src.config.config import CONFIG
from requests import Response
from flask import request
from typing import List
import requests


class MailGun():
    @staticmethod
    def sendMail(to: List[str], subject: str, title: str, text: str, html: str) -> Response:
        print(text, "text")
        return requests.post(
            f"{CONFIG.MAILGUN_API_BASE_URL}/messages",
            auth=('api', CONFIG.MAILGUN_API_KEY),
            data={
                "from": f"{title} <{CONFIG.MAILGUN_EMAIL}>",
                "to": to,
                "subject": subject,
                "text": text,
                "html": html
            }

        )


mail_gunner = MailGun.sendMail
