from datetime import datetime

from loguru import logger

# РЕКОМЕНДУЮ ЗАЙТИ В handlers/other настроить фильтры сообщений!
API_TOKEN = "7283969138:AAE2jQ9LitXKIGp67rAsxMQjI2aM83jwxc4"  # взятие токена из переменной среды

ADMINS_ID = [7202855596]
CHANNEL_ID = -1001150582525

DATABASE_FILE = "base.db"  # имя файла базы данных

SHARE = 4  # проц в день
MINIK = 100  # минимальная сумма инвестиции

START_DATE = datetime(2021, 9, 19, 14, 0)  # дата старта проэкта

PAYMENTS_MODE = True

PAY_ROWS = 10

ADMINS_CHAT = ""
OUT_CHAT = ""  # чат с пополнениями бота, если None - не куда
SUPP = ""

# for qiwi payments
QIWI_TOKENS = "YOUR_QIWI_TOKENS"
if not QIWI_TOKENS:
    logger.error("Please specify the qiwi token... env variable - QIWI_TOKENS")
else:
    QIWI_TOKENS = [x for x in QIWI_TOKENS.split(";") if x]  # среда

QIWI_ACCOUNTS = "YOUR_QIWI_ACCOUNTS"
if not QIWI_ACCOUNTS:
    logger.error("Please specify the qiwi token... env variable - QIWI_ACCOUNTS")
else:
    QIWI_ACCOUNTS = [
        x for x in QIWI_ACCOUNTS.split(";") if x
    ]  # пополнение в боте - сюда
    if len(QIWI_TOKENS) != len(QIWI_ACCOUNTS):
        logger.error("Value of tokens dont suply value of numbers")


SKIP_UPDATES = True  # если бот был выключен, а в этот момент
# кто то писал ему, то после включения он проигнорит эти сообщения

# Все круто!
logger.debug("Config setup succes!")
