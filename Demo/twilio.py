# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "ACf1878c77d945891720ba149692535c22"
auth_token = "4ef1e3945a7c9bbbab5d1db3d8a8e36a"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+919999937921", from_="+919999937921" #register twolo no
                                 ,
                                     body="Hello there!")

