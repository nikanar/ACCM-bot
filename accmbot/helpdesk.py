from accmbot import AccmHandler


class HelpdeshHandler(AccmHandler):
    def __init__(self, listen_channel, helpdesk_channel):
        self.listen_channel = listen_channel
        self.helpdesk_channel = helpdesk_channel

    def handle_message(self, slack_client, event):
        if event["channel"] == self.listen_channel:
            message = event["text"]
            split = message.split("helpdesk:")
            if len(split) == 2:
                subject = split[1].strip()
                slack_client.api_call("chat.postMessage", channel=self.helpdesk_channel, text="subject: {}".format(subject))
