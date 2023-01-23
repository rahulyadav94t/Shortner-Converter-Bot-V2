# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "8170128"))
API_HASH = os.environ.get("API_HASH", "ae7d882b947e580086b630b70e53f9a9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5925601430:AAGeqdUOdai6tgk6lTzlyBf6r4GqBvCuecA")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1787833858")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "mdisk shortX")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1787833858")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1787833858)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100mdisk_shortx")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "mdisk_shortx") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
