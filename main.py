import logging
from telethon import TelegramClient, events

# Configura il logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Sostituisci con i tuoi valori reali
api_id = 22971115  # Il tuo API ID
api_hash = '4499f6d481b41a92ace8273f685f829c'  # Il tuo API hash
session_name = 'session_name'  # Può essere qualsiasi stringa
group_id = -1002121069890  # Questo dovrebbe essere un intero, non una stringa
channel_id = '@test190503'  # Nome utente del canale

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=group_id))
async def handler(event):
    try:
        await client.forward_messages(channel_id, event.message)
        logger.info(f"Messaggio dal gruppo {group_id} inoltrato al canale {channel_id}")
    except Exception as e:
        logger.error(f"Errore nell'inoltro del messaggio: {e}")

async def main():
    await client.start()
    logger.info("Userbot avviato")
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.loop.run_until_complete(main())
