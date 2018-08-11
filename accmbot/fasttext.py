from subprocess import Popen, PIPE

from accmbot import AccmHandler


class FasttextHandler(AccmHandler):
    def __init__(self, listen_channel, response_channel):
        self.listen_channel = listen_channel
        self.response_channel = response_channel

    def handle_message(self, slack_client, event):
        if event["channel"] == self.listen_channel:
            message = event["text"].strip()
            BOT = "bot"
            if message.startswith(BOT):
                msg = message[len(BOT):].strip()
                response = self.get_label(msg)
                if response:
                    print("selftext text: {} response: {}".format(msg, response))
                    slack_client.api_call("chat.postMessage", channel=self.response_channel, text=response)
                else:
                    print("no response")

    def get_label(self, msg):
        fasttext_cmd = "/Users/jp/Desktop/fastText-0.1.0/fasttext"
        model_file = "/Users/jp/Desktop/fastText-0.1.0/model.bin"
        with open('/Users/jp/Desktop/fastText-0.1.0/tmp', 'w') as fout:
            fout.write(msg)
            fout.write('\n')

        process = Popen([fasttext_cmd, 'predict', model_file, '/Users/jp/Desktop/fastText-0.1.0/tmp'], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.strip()
        prettyfy = {b"__label__d" : "Spell out an answer",
                    b"__label__a" : "Give <THIS> precanned answer to this 'administrative' query.",
                     b"__label__r" : "Ignore this message.",
                    b"__label__u" : "This is [URGENT] !!"
        }
        print("stdout: {}".format(stdout))
        if stdout in prettyfy:
            return prettyfy[stdout]
