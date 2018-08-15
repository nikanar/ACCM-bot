import time
from abc import abstractmethod

from slackclient import SlackClient

RTM_READ_DELAY = 1

MULTI_LINE_RESPONSE = """multi line response
hello, world!
12345
qwert"""


class AccmHandler:
    @abstractmethod
    def handle_message(self, slack_client, event):
        raise NotImplementedError


class AccmBot:
    def __init__(self, slack_bot_token, *handlers):
        self.slack_client = SlackClient(slack_bot_token)
        self.listen_channels = list()
        self.handlers = tuple(handlers)

    def connect(self):
        self.slack_client.rtm_connect(with_team_state=False, auto_reconnect=True)
        response = self.slack_client.api_call("auth.test")
        if "user_id" in response:
            self.bot_id = response["user_id"]
            print("Accm Bot connected.")
            return True
        return False

    def add_channels(self, *channels):
        self.listen_channels.extend(channels)

    def start(self):
        while True:
            self.handle_events(self.slack_client.rtm_read())
            time.sleep(RTM_READ_DELAY)

    def handle_events(self, slack_events):
        for event in slack_events:
            if (event["type"] == "message" and event["channel"] in self.listen_channels):
                if "subtype" not in event or event['subtype'] == "bot_message":
                    return self.handle_event_message(event)

    def handle_event_message(self, event):
        print("non-filtered event: {}".format(event))
        for handler in self.handlers:
            handler.handle_message(self.slack_client, event)
