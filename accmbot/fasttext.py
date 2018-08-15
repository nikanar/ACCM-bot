from subprocess import Popen, PIPE

from accmbot import AccmHandler


class FasttextHandler(AccmHandler):
    def __init__(self, listen_channels, discreet_channel):
        self.listen_channels = listen_channels
        self.discreet_channel = discreet_channel
        self.BOT_TRIGGER = "bot"
        
    def handle_message(self, slack_client, event):
        if event["channel"] not in self.listen_channels: return
        message = event["text"].strip()
        if not message.startswith(self.BOT_TRIGGER): return
        msg = message[len(self.BOT_TRIGGER):].strip()
        
        label = self.get_label(msg)
        prettyfy = {b"__label__u" : "This seems urgent.",
                    b"__label__d" : "Spell out an answer",
                    b"__label__a" : "This is a usual query, we already have an answer to it. Let me find it...",
                    b"__label__r" : "Ignore this message."
                    }
        try:
            response = prettyfy[label]
        except KeyError:
            print("no response or unexpected response")
        else:
            if (event["channel"] != self.discreet_channel
                or label in [b"__label__u", b"__label__a"]):
                print("fasttext answers '{}' with '{}'".format(msg, response))
                slack_client.api_call("chat.postMessage", channel=event["channel"], text=response)


    def get_label(self, msg):
        fasttext_cmd = "fastText/fasttext"
        model_file = "fasttext_model.bin"
        with open('tmp', 'w') as tmp:
            tmp.write(msg)
            tmp.write('\n')

        process = Popen([fasttext_cmd, 'predict', model_file, 'tmp'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.strip()
        print("stdout: {}".format(stdout))
        return stdout
