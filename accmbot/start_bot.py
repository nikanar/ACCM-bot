import os

from accmbot import AccmBot
from keywords import KeywordHandler, JsonKeywordData
from helpdesk import HelpdeshHandler

TOKEN = "xoxb-416305909766-414764731412-jaXu2M1NO9khA3bJvBjVFT6Z"
LISTEN_CHANNELS = ["CC68GD2QG", "CC82B8Z6K"]


def main():
    token = TOKEN or os.environ.get('SLACK_BOT_TOKEN')
    helpdesk_handler = HelpdeshHandler("CC68GD2QG", "CC73Z93E1")
    keyword_handler = KeywordHandler(JsonKeywordData("./test.json"), "CC68GD2QG")
    fasttext_handler = FasttextHandler("CC68GD2QG", "CC73Z93E1")
    autoanswer_handler = Autoanswerer("CC68GD2QG", "CC73Z93E1")

    accm_bot = AccmBot(token, keyword_handler, helpdesk_handler, fasttext_handler, )
    accm_bot.add_channels(*LISTEN_CHANNELS)
    accm_bot.connect()
    accm_bot.start()


if __name__ == "__main__":
    main()
