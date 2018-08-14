# Simple slack bot for ACCM

Tested with python3+slackclient

There is a bug as of v0.48.0 of websocket-client, which is a dependency of slackclient.
For now, it can be resolved by downgrading to v0.47.0.
More details at https://github.com/websocket-client/websocket-client/issues/413

## Installing slackclient

    pip install slackclient --user

## Installing fasttext:

    cd ACCM-bot/accmbot
    git clone https://github.com/facebookresearch/fastText.git
    cd fastText/
    make

And you're good to go ! This is also [well documented online](https://fasttext.cc/docs/en/support.html) and there are even some [unofficial instructions for Windows](https://www.cs.mcgill.ca/~mxia3/FastText-for-Windows/).
