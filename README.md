# Simple slack bot for ACCM

Tested with python3

## Installing slackclient

    pip install slackclient --user

## Installing fastText

    cd ACCM-bot/accmbot
    git clone https://github.com/facebookresearch/fastText.git
    cd fastText/
    make

And you're good to go ! This is also [well documented online](https://fasttext.cc/docs/en/support.html) and there are even some [unofficial instructions for Windows](https://www.cs.mcgill.ca/~mxia3/FastText-for-Windows/).
If you install fastText somewhere else than in the `accmbot` folder, then you will need to adapt the `fasttext_cmd` variable in `fasttext.py`.

## Installing the bot at ACCM's Slack

Follow instructions at https://api.slack.com/bot-users, up to and including step *3/ Installing the bot to a workspace*. You'll get a bot token. Change the token in file `start_bot.py` for yours. 

Start the bot (`python start_bot.py`, on your Heroku), and hope for the best ! 

Anticipated problems : channels have to be managed right, lines 13 (CHANNEL_IDS) and 17-20 (TODO)

## For triggering on all Slack channels

Likely takes a bit of code : see https://pridehacks2018.slack.com/archives/CC2SSGH18/p1535670226000100
