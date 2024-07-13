import logging
from telethon.sync import TelegramClient, events
from telethon.tl.types import InputChannel
from telethon.sessions import StringSession

logger = logging.getLogger(__name__)


class Forwarder:
    def __init__(self, config):
        self.telegram = TelegramClient(StringSession(config.session), config.api_id, config.api_hash)
        self.message_pattern = config.message_pattern
        self.input_chat_ids = config.input_chat_ids
        self.output_chat_ids = config.output_chat_ids
        self.input_chats = []
        self.output_chats = []

    def start(self):
        self.__connect()
        self.__load_input_chats()
        self.__load_output_chats()
        self.__start_forwarding()

    def __connect(self):
        self.telegram.start()

    def __load_input_chats(self):
        dialogs = self.telegram.get_dialogs()

        for chat_id in self.input_chat_ids:
            dialog = next(filter(lambda e: e.entity.username == chat_id or str(e.entity.id) == chat_id, dialogs), None)

            if dialog:
                self.input_chats.append(InputChannel(dialog.entity.id, dialog.entity.access_hash))
            else:
                raise RuntimeError(f"Input chat '{chat_id}' was not found")

    def __load_output_chats(self):
        dialogs = self.telegram.get_dialogs()

        for chat_id in self.output_chat_ids:
            dialog = next(filter(lambda e: e.entity.username == chat_id or str(e.entity.id) == chat_id, dialogs), None)

            if dialog:
                self.output_chats.append(InputChannel(dialog.entity.id, dialog.entity.access_hash))
            else:
                raise RuntimeError(f"Output chat '{chat_id}' was not found")

    def __start_forwarding(self):
        @self.telegram.on(events.NewMessage(chats=self.input_chats, pattern=self.message_pattern))
        async def handler(event):
            logger.info("Forwarding 1 message")

            for output_chat in self.output_chats:
                await self.telegram.forward_messages(output_chat, event.message)

        logger.info(f"Listening on {len(self.input_chats)} chats.")
        logger.info(f"Forwarding messages to {len(self.output_chats)} chats.")

        self.telegram.run_until_disconnected()
