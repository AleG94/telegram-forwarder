# telegram-forwarder
Forward messages that match a specific pattern from multiple Telegram chats to one or more chats.

## Requirements
- Docker

## Installation and usage

1. Pull the [Docker](https://www.docker.com) image from the [DockerHub](https://hub.docker.com/r/aleg94/telegram-forwarder):

    ```
    docker pull aleg94/telegram-forwarder
    ```

2. Create a Telegram **session** by getting developer's api id and api hash from [here](https://core.telegram.org/api/obtaining_api_id) and running the command:

    ```
    docker run -it --rm aleg94/telegram-forwarder python ./scripts/create_session.py --api-id <api-id> --api-hash <api-hash>
    ```

    Follow the on-screen instructions and enter your confirmation code and password (if two-factor authentication is enabled).


3. Run the image in a **container** providing the following *environment variables*:

    * `API_ID`: the [api id](https://core.telegram.org/api/obtaining_api_id) associated with your Telegram account
    * `API_HASH`: the [api hash](https://core.telegram.org/api/obtaining_api_id) associated with your Telegram account
    * `SESSION`: the session obtained in step 2
    * `INPUT_CHATS`: comma separated list of chat's ids or usernames that you'd like to forward messages from (must be present on dialogs)
    * `OUTPUT_CHATS`: comma separated list of chat's ids or usernames that you'd like to forward messages to (must be present on dialogs)
    * `MESSAGE_PATTERN`: a regular expression that messages must match to be forwarded

    <br>

    ```
    docker run --name telegram_forwarder -d
      -e API_ID=<api-id>
      -e API_HASH=<api-hash>
      -e SESSION=<session>
      -e INPUT_CHATS=<id1>,<username2>
      -e OUTPUT_CHATS=<username3>,<id4>
      -e MESSAGE_PATTERN=<regex>
      aleg94/telegram-forwarder
    ```
