import numpy as np
import time
import yagmail
from functions import current_time, intervals, capture_image, current_weekday, current_date
from private_info import sender_email, receiver_emails, sender_email_password

def main(usage='test'):
    low,high = intervals(usage=usage)
    relative_image_path = 'screen.png'
    while True:
        try:
            time.sleep(np.random.randint(low,high))
            capture_image(relative_image_path)
            yag = yagmail.SMTP(user=sender_email, password=sender_email_password)
            subject = f'Yishai\'s screen {current_weekday()} {current_date()}'
            yag.send(to=receiver_emails, 
                    subject=subject, 
                    contents='See the attached image!',
                    attachments=relative_image_path
                    )
            print(f'Sent at {current_time()}')
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    main(
        usage='real' # comment out in order to run as test
        )