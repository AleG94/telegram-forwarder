from argparse import ArgumentParser
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

parser = ArgumentParser()

parser.add_argument('--api-id', action='store', dest='api_id', help='Telegram Api ID', required=True)
parser.add_argument('--api-hash', action='store', dest='api_hash', help='Telegram Api Hash', required=True)

args = parser.parse_args()

with TelegramClient(StringSession(), args.api_id, args.api_hash) as client:
    print(f"Your session is: \n{client.session.save()}")
