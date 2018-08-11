simple slack bot for accm
tested with python3+venv+slackclient

there is a bug as of v0.48.0 of websocket-client,
which is a dependency of slackclient
more details here:
https://github.com/websocket-client/websocket-client/issues/413

for now, it can be resolved by downgrading to v0.47.0

test.json file contains examples for keyword responses
