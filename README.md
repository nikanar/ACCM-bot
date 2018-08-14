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