import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "yrlczsoktytuxjrx"
SENDER = "kruger.de.boss@gmail.com"
RECEIVER = "kruger.de.boss@gmail.com"


def send_email(image_path):
    print("Send Email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New detection!"
    email_message.set_content("A new object has been detected on the webcam")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("Send Email function ended")


if __name__ == "__main__":
    send_email("images/pic50.png")
