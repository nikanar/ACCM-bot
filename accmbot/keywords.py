import json

from accmbot import AccmHandler


class JsonKeywordData:
    "FIXME This wheel has been invented before."
    def __init__(self, filename):
        self.items = list()
        with open(filename, 'r') as file:
            data = json.loads(file.read())
            for item in data:
                keywords = item['keywords']
                response = item['response']
                self.items.append((keywords, response))


class KeywordHandler(AccmHandler):
    def __init__(self, keywords_data, channel):
        self.keywords_data = keywords_data
        self.channel = channel

    def handle_message(self, slack_client, event):
        if event["channel"] == self.channel:
            response = list()
            message = event["text"]
            for keywords_item in self.keywords_data.items:
                response.extend(self.find_keywords(message.lower(), keywords_item))

            if len(response) > 0:
                self.send_response(slack_client, response)

    def find_keywords(self, message, keywords_item):
        response = list()
        for keyword in keywords_item[0]:
            if message.find(keyword) != -1:
                response.append(keywords_item[1])
        return response

    def send_response(self, slack_client, responses):
        for response in responses:
            slack_client.api_call("chat.postMessage", channel=self.channel, text=response)
