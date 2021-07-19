import requests # it will help us to get our url directed
from bs4 import BeautifulSoup # it will help us to scrap us the data

import time  # to send email on interval
import os
import smtplib  ## this module is used for sending mail
from email.message import EmailMessage

my_email = 'pritamramteke3212@gmail.com'
my_pass = 'stato@123'

# email_id = os.environ.get('EMAIL_ADDR')
# email_pass = os.environ.get('EMAIL_PASS)

# i have used this because i have hidden my credentials if you don't know how to do
# i,ll give a link in description how to hide your credentials


email_id = my_email
email_pass = my_pass


URL = 'https://www.amazon.in/Samsung-inches-Crystal-Ultra-UA55AUE60AKLXL/dp/B092BL5DCX/ref=sr_1_1_sspa?dchild=1&keywords=sony+bravia&qid=1626412229&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUU0xQk5NV1BBSkM5JmVuY3J5cHRlZElkPUEwNTc3OTAyMzRXNjY0T0QwNUsyTyZlbmNyeXB0ZWRBZElkPUEwNzQxNjI4MUNCU0FOU0VGN1REUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

def check_price():
    ## copy url of the product which you are looking for

    headers = {'user-Agents' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    # now let's print our product title to verify it is working perfectly
    page = requests.get(URL, headers = headers)
    soup = BeautifulSoup(page.content , 'html.parser')

    title = soup.find(class_ = "a-size-large product-title-word-break").get_text()
    price = soup.find(class_ = "a-size-medium a-color-price priceBlockBuyingPriceString").get_text()
    converted_price = int(price[1:-3].replace(',',''))  # it is giving value as 69.899 so it will remove . too

    print(title.strip()) ### strip use to remove forwrd and backword spaces
    # print(price)
    print(converted_price)


    # we will send mail if the price is less than present price


    if(converted_price < 54999):
        send_mail()



def send_mail():
    msg = EmailMessage()
    msg['Subject'] = 'Product price fell down'
    msg['From'] = email_id
    msg['To'] = 'pritamramteke3211@gmail.com'
    msg.set_content("Hey Check this amazon link : https://www.amazon.in/Samsung-inches-Crystal-Ultra-UA55AUE60AKLXL/dp/B092BL5DCX/ref=sr_1_1_sspa?dchild=1&keywords=sony+bravia&qid=1626412229&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUU0xQk5NV1BBSkM5JmVuY3J5cHRlZElkPUEwNTc3OTAyMzRXNjY0T0QwNUsyTyZlbmNyeXB0ZWRBZElkPUEwNzQxNjI4MUNCU0FOU0VGN1REUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")


    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:     # 465 is the port number
        smtp.login(email_id,email_pass)
        smtp.send_message(msg)

