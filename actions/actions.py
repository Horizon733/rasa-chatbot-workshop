# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def send_email(email,content):
        try:
            message = MIMEMultipart()
            message["Subject"] ="Order Confirmation mail"
            with open(filename, "rb") as attachment:
                            part = MIMEBase("application", "octet-stream")
                            part.set_payload(attachment.read())
            encoders.encode_base64(part) 
            part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
            fromadd = 'dishantgandhi733@gmail.com'
            toadd = email
            username = 'dishantgandhi733@gmail.com'
            obj = open('pass.txt')
            password = obj.read()
            server = smtplib.SMTP('smtp.gmail.com', 587,)
            server.ehlo()
            context = ssl.create_default_context()
            server.starttls(context=context)
            server.login(username, password)
            msg = MIMEText(content,"html")
            message.attach(msg)
            message.attach(part)
            server.sendmail(fromadd, toadd, message.as_string())
            server.quit()
        except SMTPAuthenticationError as x:
            print("Your email is wrong ",x)
        except SMTPConnectError as e:
            print("Your connection Error ",e)
        except SMTPException as a:
            print("error: ",a)
            content_text = "Sorry system run into trouble.. Can you please check again?"
            print(content_text)
        return[]


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
