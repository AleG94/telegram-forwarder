# telegram-forwarder
Forward messages that match a specific pattern from multiple Telegram chats to one or more chats.

## Requirements
- Docker

## Installation and usage

Pull the [Docker](https://www.docker.com) image from the [DockerHub](https://hub.docker.com/r/aleg94/telegram-forwarder):

```
docker pull aleg94/telegram-forwarder
```

The first time you'll be required to create a new session by signing into your Telegram account.

Run a container in `interactive` mode, providing the following *environment variables*:

* `PHONE`: the phone number of your Telegram account
* `API_ID`: the developer [api id](https://core.telegram.org/api/obtaining_api_id) associated with your Telegram account
* `API_HASH`: the developer [api hash](https://core.telegram.org/api/obtaining_api_id) associated with your Telegram account
* `SESSION_NAME`: a unique name for the session
* `INPUT_CHAT_USERNAMES`: comma separated list of chat's usernames that you'd like to forward messages from (must be present on dialogs)
* `OUTPUT_CHAT_USERNAMES`: comma separated list of chat's usernames that you'd like to forward messages to (must be present on dialogs)
* `MESSAGE_PATTERN`: a regular expression that messages must match to be forwarded

<br>

```
docker run --name telegram_forwarder -it
  -e PHONE=<phone>
  -e API_ID=<api-id>
  -e API_HASH=<api-hash>
  -e SESSION_NAME=<session-name>
  -e INPUT_CHAT_USERNAMES=<username1>,<username2>
  -e OUTPUT_CHAT_USERNAMES=<username3>,<username4>
  -e MESSAGE_PATTERN=<regex>
  aleg94/telegram-forwarder
```

Follow the on-screen instructions and enter your confirmation code and password (if two-factors authentication is enabled).

Press `CTRL + P` then `CTRL + Q` to switch from `interactive` to `detached` mode.
This will keep the container running in background.
