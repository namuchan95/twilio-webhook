from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
import os
port = int(os.getenv('PORT'))


@app.route("/record", methods=['GET', 'POST'])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = VoiceResponse()

    # Use <Say> to give the caller some instructions
    response.say('Hello')

    # Use <Record> to record the caller's message
    response.record()

    # End the call with <Hangup>
    response.hangup()

    return str(response)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")
    print(body)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
