enc_t = "+SLJ92pAj0k8vKeidebUH1e/nW1+4SZjpQ9DInlRWAiRPHsW2V6Jerly05O5VJmEz6U5qEV79my8N62lB3UBtztAtW5ZEyzSaYWlJ3WEqu331zI8RJDUEQ=="
email = "avinash9588@gmail.com"
from kite_trade import *
import time
kite = KiteApp(enc_t)

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add message body
    message.attach(MIMEText(body, 'plain'))

    # Connect to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to your gmail account
    server.login(sender_email, sender_password)

    # Send Email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Quit the server
    server.quit()


def price_fetcher(symbol):              #this function can be used to fetch the current market price of that particular symbol
    price = kite.ltp(["NFO:" + symbol])
    final_price = price["NFO:" + symbol]["last_price"]

    return final_price




#authentication and basic services starts here

green_view_symbol = "NIFTY24MAR22200CE"
red_view_symbol = "NIFTY24MAR22150PE"


def price_test(symbol):
  curr_price = price_fetcher(symbol)
  if curr_price == None:
    print("price validation failed")
    print("check the credetials and start over")
    time.sleep(10000000)

  else:
    print("api and network compnonents and hardware are working fine")
    sender_email = "avinashaws9588@gmail.com"
    sender_password = "mcst rhrz krcr baoe"
    receiver_email = email
    subject = "API WORKING FINE"
    body = "It is to inform you that the we are correctly abled to fetch the correct price of the DESIRED INSTRUEMENT and network other componenets are working fine"
    send_email(sender_email, sender_password, receiver_email, subject, body)





def initilaize(enc,email):
  kite = KiteApp(enc_t)
  sender_email = "avinashaws9588@gmail.com"
  sender_password = "mcst rhrz krcr baoe"
  receiver_email = email
  subject = "Authentication Sucessfull"
  body = "Hello, welcome to Cancerian Capital.This is to informed that you have been succesfull authenticated"
  send_email(sender_email, sender_password, receiver_email, subject, body)
  print("authentication mail sent")

  if kite.positions() != None:
    print("hey successfull signin")



  else:
    print("invalid enc token")
    print("restert the application")
    time.sleep(10000000)


initilaize(enc_t,email)
price_test(green_view_symbol)



#authentication basic services finishes here



print("NOW ITS REQUIRED FOR US TO KNOW YOUR VIEW")
print("so for BULLISH - green")
print("and for bearish - red")
print("REMEMBER THE INPUT WILL BE CASE-SENSATIVE")

view = "green"
if view == "green":
  fsym = green_view_symbol
  print("now all the trades will be taken in the upside of the market")
elif view == "red":
  fsym = red_view_symbol
  print("now all the trades will be taken in the downside of the market")
else:
  print("sorry you have entered a wrong input")
  time.sleep(3)
  print("go and retstart the application with the right input")
  time.sleep(100000000000)

sender_email = "avinashaws9588@gmail.com"
sender_password = "mcst rhrz krcr baoe"
receiver_email = email
subject = "TRADE SETUP SUCESSFULL BUDDY,ALL SET TO GOT"
body = "Hello ,now we are all set to trade !!,algo will start trade whenever its feels like to go into a trade now sit back and relax,and just make sure the hardware the your network remains stable ,else algo might get interuppted in between and will spoil your experienrnce"
send_email(sender_email, sender_password, receiver_email, subject, body)



#function definations required to setup trade and variable declarataion required for trading

#fsym== declared already in the above code (based upon the users input on his/her view on the current trend)

ntr = 15 #as the maximum no of trades can be placed by an algorithm in a single day is 10,so ntr = 10

h_c_o = [] #list used for hieken ashi calculation which stores only opens of the candles
h_c_c = [] #list used for hieken ashi calculation which stores closing values for the hieken ashi calculation
nature = []


def init_ha(fsym):
  open = price_fetcher(fsym)
  start = time.time()
  now = time.time()
  while now - start <=60:
    now = time.time()
  close = price_fetcher(fsym)
  h_c_o.append(open)
  h_c_c.append(close)
  if close > open:
    nature.append("green")
  else:
    nature.append("red")





def hieken_ashi(fsym):
  open = price_fetcher(fsym)
  low = price_fetcher(fsym)

  high = price_fetcher(fsym)
  start = time.time()
  now = time.time()
  while now - start <= 60 :
    curr_price = price_fetcher(fsym)
    if curr_price > high:
      high = curr_price
    if curr_price < low:
      low = curr_price
    now = time.time()
  close = price_fetcher(fsym)

  curr_open = (h_c_o[-1]+h_c_c[-1])/2
  curr_close = (open+low+high+close)/4

  h_c_o.append(curr_open)
  h_c_c.append(curr_close)


  if curr_open >= curr_close:
    curr_nature = "red"
  if curr_close > curr_open:
    curr_nature = "green"

  nature.append(curr_nature)
  return curr_nature

#hieken ashi,s main function defination and init function for the same has been defined in above blocks


# in this we are gonna create paper functions for wallet set up and making buy sell sqaure off and other function
wallet = 20000
buy_l = []
sell_l = []


def buy(fsym):
    global buy_capital, wallet
    curr_price = price_fetcher(fsym)
    buy_capital = curr_price * 50
    wallet = wallet - buy_capital
    print("buy order has been executed")
    sender_email = "avinashaws9588@gmail.com"
    sender_password = "mcst rhrz krcr baoe"
    receiver_email = email
    subject = "BUY ORDER PLACED"
    body = "hello just we have placed a buy order  and capital deployed is " + str(
        buy_capital) + "and your current wallet balance is " + str(wallet)
    send_email(sender_email, sender_password, receiver_email, subject, body)


def buy_square_off(fsym):
    global wallet
    curr_sell_value = price_fetcher(fsym) * 50
    change = curr_sell_value - buy_capital
    wallet = wallet + curr_sell_value
    print("BUY ORDER SQAURED OFF")
    sender_email = "avinashaws9588@gmail.com"
    sender_password = "mcst rhrz krcr baoe"
    receiver_email = email
    subject = "BUY ORDER SQAURED OFF"
    # print("buy order has been sqaured off of the instrumemt ",fsym,"with the net value of",change,"and now net balance is ",wallet)
    body = "hello just now have sqaured of the buy trade with a net chnage value of" + str(
        change) + "and you current balance is" + str(wallet)
    send_email(sender_email, sender_password, receiver_email, subject, body)






#time related logic is here

import datetime
import pytz
import time

def is_between_10_to_3():
    # Get the current time in Indian Standard Time (IST)
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist)

    # Define the start and end times for the allowed period (10 am to 3 pm)
    start_time = current_time.replace(hour=10, minute=0, second=0, microsecond=0)
    end_time = current_time.replace(hour=15, minute=0, second=0, microsecond=0)

    # Check if the current time is between start and end times
    if start_time <= current_time <= end_time:
        return True
    else:
        return False


# proposed main logic

def start_ha(fsym):
    global ntr
    while True:
        if ntr == 0:
            print("no of trades per day has been exceeded so sorry dear,see you tomorrow")
            break
        if is_between_10_to_3() and ntr > 0:
            trend = hieken_ashi(fsym)
            if view == nature[-1] != nature[-2]:
                if nature[-1] == "green":
                    buy(fsym)
                    red_obs(fsym)

        else:

            break


def red_obs(fsym):
    global ntr
    trend = hieken_ashi(fsym)
    while True:
        if trend == "red":
            ntr -= 1
            buy_square_off(fsym)
            start_ha(fsym)

        trend = hieken_ashi(fsym)


init_ha(fsym)
start_ha(fsym)

















