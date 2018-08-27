import json

from accmbot import AccmHandler

class JsonKeywordData:
    def __init__(self, filename):
        self.items = [([k.lower() for k in p['keywords']], p['response'])
                      for p in json.load(open(filename))]

class KeywordHandler(AccmHandler):
    def __init__(self, keywords_data, channel):
        self.keywords_data = keywords_data
        self.channel = channel

    def handle_message(self, slack_client, event):
        if event["channel"] == self.channel and "subtype" not in event:
            response = []
            message = event["text"]
                
            for keywords_item in self.keywords_data.items:
                response.extend(self.find_keywords(message.lower(), keywords_item))

            if 'files' in event:
                for f in event['files']:
                    if f['mimetype'] == 'image/jpeg':
                        response.extend(self.find_keywords("<image-is-being-sent>", keywords_item))
                
            if response:
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
