import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()



# Your Account SID and Auth Token from console.twilio.com
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token  = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=os.getenv('MY_PHONE_NUMBER'),
    from_=os.getenv('MY_TWILIO_PHONE_NUMBER'),
    body="What hath God wrought!")

print(message.sid)