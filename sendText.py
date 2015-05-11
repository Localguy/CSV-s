from twilio.rest import TwilioRestClient

accountSID = 'xxxxxxxxxxx'
authToken = 'cxxxxxxxxxxx'

twilioCLI = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+xxxxxxxx'
myCellPhone = '+1xxxxxxxx'

message = twilioCLI.messages.create(body='Mr. Chandler - come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
