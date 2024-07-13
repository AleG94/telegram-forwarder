import os

session = os.environ.get('SESSION')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
input_chat_ids = os.environ.get('INPUT_CHATS').replace('-100', '').split(',')
output_chat_ids = os.environ.get('OUTPUT_CHATS').replace('-100', '').split(',')
message_pattern = os.environ.get('MESSAGE_PATTERN')
