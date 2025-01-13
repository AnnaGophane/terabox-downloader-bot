import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')
ADMINS = list(map(int, os.getenv('ADMINS', '').split(',')))
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')

# Terabox Configuration
COOKIE = os.getenv('TERABOX_COOKIE', '')


# REDIS
HOST = "redis-14201.c15.us-east-1-2.ec2.redns.redis-cloud.com:14201"  # redis host uri
PORT = 6379  # redis port
PASSWORD = "1hlUwaWzkStWzk0AcdiSSUBIwkHBKARc"  # redis password

PRIVATE_CHAT_ID = -1002315965012  # CHAT WHERE YOU WANT TO STORE VIDEOS
# COOKIE FOR AUTHENTICATION (get from chrome dev tools) ex: "PANWEB=1; csrfToken=;
COOKIE = "TSID=KGQXgFvgYgnwRJyx1zXCFMQ2hOPu87ot; __bid_n=1918fe6e58b6c4b0e24207; _ga=GA1.1.966127542.1724696176; g_state={"i_l":0}; ndus=YyYP664teHuisg26Y083n59lsWLAoPkK1rrlN14i; PANWEB=1; browserid=TzHtqXtjz8v8OXd4ThrPzk8Z2lsQf66ybvWfogKMjsz8ZzSTgogC9U35k5k=; lang=en; csrfToken=PcnfIYSm-V_OLF8sLee2BTxP")
ADMINS = [5321385511]


BOT_USERNAME = "Terabox_Links_To_Videos_bot"

# Force user to join this channel. (make sure you have promoted the bot on this chat.)
FORCE_LINK = "@Terabox_Links_To_Videos"

PUBLIC_EARN_API = "853a417e6360effc641fbe39633b730869df8e21"  # https://publicearn.com/api
