from twilio.rest import Client
from private_info import PHONE_NUMBER,TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN, TWILIO_NUMBER

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=f'+{TWILIO_NUMBER}',
                     to=f'+{PHONE_NUMBER}'
                 )

print(message.sid)