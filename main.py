from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
