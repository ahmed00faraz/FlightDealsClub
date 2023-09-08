import smtplib
from twilio.rest import Client

TWILIO_SID = "Your Credentials"
TWILIO_AUTH_TOKEN = "Your Credentials"
FROM_NUMBER = "Your Credentials"
TO_NUMBER = "Your Credentials"

EMAIL = "Your Credentials"
PASSWORD = "Your Credentials"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=TO_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
