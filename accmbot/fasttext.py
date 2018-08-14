from subprocess import Popen, PIPE

from accmbot import AccmHandler


class FasttextHandler(AccmHandler):
    def __init__(self, listen_channel):
        self.listen_channel = listen_channel
        self.response_channel = listen_channel
        self.BOT_TRIGGER = "bot"

        
    def handle_message(self, slack_client, event):
        if event["channel"] != self.listen_channel: return
        message = event["text"].strip()
        if not message.startswith(self.BOT_TRIGGER): return
        msg = message[len(self.BOT_TRIGGER):].strip()
        
        label = self.get_label(msg)
        prettyfy = {b"__label__u" : "This is [URGENT] !!",
                    b"__label__d" : "Spell out an answer",
                    b"__label__a" : "This is an administrative query, we have a precanned answer to it.",
                    b"__label__r" : "Ignore this message."
                    }
        try:
            response = prettyfy[label]
        except KeyError:
            print("no response or unexpected response")
        else:
            print("fasttext answers '{}' with '{}'".format(msg, response))
            slack_client.api_call("chat.postMessage", channel=self.response_channel, text=response)


    def get_label(self, msg):
        fasttext_cmd = "fastText-0.1.0/fasttext"
        model_file = "fasttext_model.bin"
        with open('tmp', 'w') as tmp:
            tmp.write(msg)
            tmp.write('\n')

        process = Popen([fasttext_cmd, 'predict', model_file, 'tmp'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.strip()
        print("stdout: {}".format(stdout))
        return stdout
