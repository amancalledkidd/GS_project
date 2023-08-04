import os
from datetime import datetime, timedelta
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

class OrderConfirmation():
    def __init__(self, order):
        self.order = order
        self.time = datetime.now().strftime('%H:%M:%S')

    def get_customer_message(self):
        return f'Thank you! Your order was placed at {self.time} and will be delivered before {(datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")}'

    def send_order_confirmation(self):
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token  = os.getenv('TWILIO_AUTH_TOKEN')

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=os.getenv('MY_PHONE_NUMBER'),
            from_=os.getenv('MY_TWILIO_PHONE_NUMBER'),
            body=(self.get_customer_message() + " \n" + self.order.get_order_reciept())
        )

        print(message.sid)