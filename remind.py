#/usr/bin/env python3

import asyncio
from aiolinkding import async_get_client

import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

linkding_url = os.environ.get('LINKDING_URL')
linkding_token = os.environ.get('LINKDING_TOKEN')
linkding_tag = os.environ.get('LINKDING_TAG')

smtp_sender = os.environ.get('SMTP_SENDER')
smtp_recipient = os.environ.get('SMTP_RECIPIENT')
smtp_server = os.environ.get('SMTP_SERVER')
smtp_port = os.environ.get('SMTP_PORT')
smtp_password = os.environ.get('SMTP_PASSWORD')
smtp_username = os.environ.get('SMTP_USERNAME')

async def remind() -> None:

    client = await async_get_client(linkding_url, linkding_token)
    bookmark = await client.bookmarks.async_get_all(query="#" + linkding_tag)

    result = bookmark['results']

    smtp_body=[]
    smtp_body.append("---")
    for i in result:
        smtp_body.append(i['title'])
        smtp_body.append(i['url'])
        smtp_body.append("---")

    multiline_body = "\n".join(smtp_body)

    msg = MIMEMultipart()

    msg['From'] = smtp_sender
    msg['To'] = smtp_recipient
    msg['Subject'] = 'Your Linkding Bookmark Reminder for tag "' + str(linkding_tag) + '"'
    msg.attach(MIMEText(multiline_body))

    server = smtplib.SMTP(smtp_server + ":" + str(smtp_port))
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(smtp_sender, smtp_password)
    server.sendmail(smtp_sender,smtp_recipient,msg.as_string())
    server.quit()

asyncio.run(remind())