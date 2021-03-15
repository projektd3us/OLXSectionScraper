from twilio.rest import Client


# tested and working, not needed in implementation
def sendMessage(text=''):
    """
    Function used for sending stuff as a text message.
    I can't currently find any use for this within this project.
    """
    account_sid = 'sid'
    auth_token = 'token'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=text,        from_='sender',
        to="receiver"
    )
    print(message.sid)
