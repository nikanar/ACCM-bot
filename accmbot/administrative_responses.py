from accmbot import AccmHandler

class Autoanswerer(AccmHandler):
    def __init__(self, listen_channel, response_channel):
        self.listen_channel = listen_channel
        self.response_channel = response_channel

    def handle_message(self, slack_client, event):
        """Move the 'This is an administrative query, we have a precanned answer to it.' ball forward with the correct answer."""

        if event["channel"] != self.listen_channel: return
        message = event["text"].strip()
        BOT_TRIGGER = "This is an administrative query"
        if not BOT_TRIGGER in message: return
        msg = "FIXME" # get this from the FasttextHandler, or parse the conversation above.

        json_data = json.load(open("administration.json"))
        precanned_answers = [e['response'] for e in json_data if "test" not in e['response']]
        response = "\n\n".join(precanned_answers)
        # FIXME pick the correct answer to the msg instead of sending them all
        
        print("bot selects {} from the list of preformatted answers"
              .format("FIXME-currently-doesn't-select"))
        slack_client.api_call("chat.postMessage", channel=self.response_channel, text=response)
