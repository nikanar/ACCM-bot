# Simple slack bot for ACCM

Tested with python3+venv+slackclient

There is a bug as of v0.48.0 of websocket-client, which is a dependency of slackclient.
For now, it can be resolved by downgrading to v0.47.0.
More details at https://github.com/websocket-client/websocket-client/issues/413
