from telethon.sync import TelegramClient
from datetime import datetime, timedelta
import pytz
# api_id and api_hash you must take from https://my.telegram.org/. Create your app (any) and get it.
api_id =                                        # Your api_id in int format (for example, 1234567)
api_hash =                                      # Your api_hash in str format (for example, 'deadbeef1337600613')
username =                                      # Session name in str format (for example, 'Anon')

client = TelegramClient(username, api_id, api_hash)
client.start()
tz = pytz.timezone("Europe/Moscow")             # You can choose any zone. For example, you can use UTC (tz = pytz.UTC)
delta = timedelta(hours=24)                     # For all message, older than 24 hours.
for dialog in client.iter_dialogs():
    try:
        for message in client.iter_messages(dialog.id, from_user='me'):
            if (tz.localize(datetime.now()) - message.date.replace(tzinfo=tz)) > delta:
                client.delete_messages(dialog.id, message)
    except Exception:
        pass
