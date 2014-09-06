#!/usr/bin/python

# Subfinder script
# Queries subfinder to check for avalable jobs

import time
from requests import session
import smtplib
from email.mime.text import MIMEText

headers = {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://subfinder.wrdsb.on.ca/wc2/',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Origin': 'https://subfinder.wrdsb.on.ca',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}


#   (r'__VSTATE', r'%2FwEPDwUKMTgwNzQ1NzE0OQ9kFgICAQ9kFgICAQ9kFgJmD2QWAmYPZBYCZg8PFgIeBFRleHQFHkluY29ycmVjdCBVc2VyTmFtZSBvciBQYXNzd29yZGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQZTdWJtaXQ'),

payload = {
    '__VIEWSTATE' : '/wEPDwUKMTgwNzQ1NzE0OQ9kFgICAQ9kFgICAQ9kFgJmD2QWAmYPZBYCZg8PFgIeBFRleHQFHkluY29ycmVjdCBVc2VyTmFtZSBvciBQYXNzd29yZGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQZTdWJtaXQ=' , #'%2FwEPDwUKMTgwNzQ1NzE0OQ9kFgICAQ9kFgICAQ9kFgJmD2QWAmYPZBYCZg8PFgIeBFRleHQFHkluY29ycmVjdCBVc2VyTmFtZSBvciBQYXNzd29yZGRkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQZTdWJtaXQ%3D',
    'UserName': 'delafranier',
    'Password': '36379663',
    'Submit.x': '0',
    'Submit.y': '0'
}

no_jobs = 'No jobs available'

#email setup
msg = MIMEText('Jobs are available!!')
msg['Subject'] = 'Subfinder Script'
msg['From'] = 'servos@gmail.com'
msg['To'] = 'servos@gmail.com'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("servos@gmail.com", "baden7")

while True:

    with session() as c:
        request = c.post('https://subfinder.wrdsb.on.ca/WC2/uiGenLogin.aspx', data=payload, headers=headers)
        request = c.post('https://subfinder.wrdsb.on.ca/WC2/sub/SubAvailableJobs.aspx', data=payload, headers=headers)
        if no_jobs in request.text:
            print 'No Jobs'
        else:
            print 'JOBS!!'
            print( request.text )
            server.sendmail('servos@gmail.com', 'servos@gmail.com', msg.as_string())

        time.sleep(600)

server.quit()
