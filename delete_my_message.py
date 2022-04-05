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
counter_deleted_message = 0
for dialog in client.iter_dialogs():
    try:
        for message in client.iter_messages(dialog.id, from_user='me'):
            if (tz.localize(datetime.now()) - message.date.replace(tzinfo=tz)) > delta and message.raw_text is not None:
                try:
                    client.delete_messages(dialog.id, message)
                    counter_deleted_message += 1
                except errors.FloodWaitError as e:
                    print('Have to sleep', e.seconds, 'seconds')
                    time.sleep(e.seconds)    
    except Exception:
        pass
print('Deleted {} post(s)'.format(counter_deleted_message))
