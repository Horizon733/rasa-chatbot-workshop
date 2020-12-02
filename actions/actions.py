# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from rasa_sdk.events import SlotSet, EventType
import email
import smtplib, ssl
from email import encoders
from smtplib import SMTPConnectError,SMTPException, SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email,content):
        try:
            message = MIMEMultipart()
            message["Subject"] ="Order Confirmation mail"
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


class ActionMenu(Action):
    def name(self):
        return "action_menu"
    def run(self, dispatcher: CollectingDispatcher,
     tracker: Tracker, domain: Dict) -> List[EventType]:
        menu = pd.read_csv("menu.csv",index_col=0)
        content = ""
        menu_list = menu.values.tolist()
        for i,j in enumerate(menu_list):
            content += f"{i+1}. {j[0]} --- Rs.{j[1]}\n"
        dispatcher.utter_message(text=content)
        return []

class ActionSendMail(Action):
    def name(self):
        return "action_send_mail"
    def run(self, dispatcher: CollectingDispatcher,
     tracker: Tracker, domain: Dict) -> List[EventType]:
            email_msg = f"""
            <h2>{tracker.get_slot("name")}<br>{tracker.get_slot("email")}<h2><br>
            <h4>Item<h4>{tracker.get_slot("order")}
            """
            send_email(tracker.get_slot("email"),email_msg)
            dispatcher.utter_message("Email has been Sent")
