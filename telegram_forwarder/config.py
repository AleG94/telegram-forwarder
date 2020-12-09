import os

session = os.environ.get('SESSION')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
input_chat_usernames = os.environ.get('INPUT_CHAT_USERNAMES').split(',')
output_chat_usernames = os.environ.get('OUTPUT_CHAT_USERNAMES').split(',')
message_pattern = os.environ.get('MESSAGE_PATTERN')
