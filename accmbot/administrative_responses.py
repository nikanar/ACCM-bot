import json

from accmbot import AccmHandler

class Autoanswerer(AccmHandler):
    def __init__(self, listen_channel):
        self.listen_channel = listen_channel
        self.response_channel = listen_channel
        self.BOT_TRIGGER = "This is an administrative query"

        json_kb = json.load(open("administration.json"))
        self.precanned_answers = [e['response'] for e in json_kb if "test" not in e['response']]


    def handle_message(self, slack_client, event):
        """Move the 'This is an administrative query, we have a precanned answer to it.' ball forward with the correct answer."""
        if event["channel"] != self.listen_channel: return
        if not self.BOT_TRIGGER in event["text"]: return

        msg = "" # FIXME get this from the FasttextHandler, or parse the conversation above.
        response = "\n\n".join(self.precanned_answers)
        response = "\n".join([" ".join(a.split()[:8])+" ... "+" ".join(a.split()[-3:])
                              for a in self.precanned_answers])
        # FIXME pick the correct answer to the msg instead of sending them all
        
        print("bot selects {} from the list of preformatted answers"
              .format("FIXME-currently-doesn't-select"))
        slack_client.api_call("chat.postMessage", channel=self.response_channel, text=response)
