import os
from dotenv import load_dotenv

load_dotenv()

class Config:
# Bot Configuration
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
#BOT_USERNAME = os.getenv('BOT_USERNAME')
#ADMINS =list(map(int, os.getenv('ADMINS', '').split(',')
REDIS_URL = os.getenv('REDIS_URL')  # Heroku Redis URL if you're using Redis

#import os
#from dotenv import load_dotenv

#load_dotenv()

    #API_ID = os.environ.get('API_ID')
    #API_HASH = os.environ.get('API_HASH')
    #BOT_TOKEN = os.environ.get('BOT_TOKEN')
    #REDIS_URL = os.environ.get('REDIS_URL')  # Heroku Redis URL if you're using Redis
    
    # Add any other configuration variables you need
    #OWNER_ID = os.environ.get('OWNER_ID')
    #AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "").split(",") if x]


# Bot Configuration
BOT_USERNAME = os.getenv('BOT_USERNAME')
ADMINS = list(map(int, os.getenv('ADMINS', '').split(',')))

# Terabox Configuration
COOKIE = os.getenv('TERABOX_COOKIE', '')


# REDIS
HOST = "redis-14201.c15.us-east-1-2.ec2.redns.redis-cloud.com:14201"  # redis host uri
PORT = 6379  # redis port
PASSWORD = "1hlUwaWzkStWzk0AcdiSSUBIwkHBKARc"  # redis password

PRIVATE_CHAT_ID = -1002315965012  # CHAT WHERE YOU WANT TO STORE VIDEOS
# COOKIE FOR AUTHENTICATION (get from chrome dev tools) ex: "PANWEB=1; csrfToken=;
COOKIE = COOKIE = """TSID=FOeqq2M60uJoPxT91h2d6hTp8OQyvy7l; __bid_n=191b41263b2dec67e64207; _ga=GA1.1.261504964.1725302990; browserid=zaSJoZFVXlwkzflrk_rkKylLduLQyfaBziB0Ne6E2swa7dePFOROFF_2GQk=; lang=en; csrfToken=rJfB7saNm1dsNe6n7FE-f_MC; ab_ymg_result={"data":"f2661a2fe509971ce941e66c00e87c4c787b0d43d7b1f16958f00bc695bd6c1f0ccddb0782c88124728c5c81c25a74d7d2c2d3785321227821001fd421d83e3d318d208c7a9ade5ccf3db07b17e66509b16f16f49725eb08c16a166fc4f7c5549b4e24ab6bd77ebd2a2d0429e6f620ec2d52a51ef1387d0cfbd402e760ffcc6b","key_id":"66","sign":"e7440ed6"}; ndus=YyYP664teHuidtxnSrRJZnvavH7rvI-3YvzLu5NX; ndut_fmt=2B0B1085F3AB75480D97AD5F92A093A9ED893440E12EB5B3D3AD1AB96FE83990; ab_sr=1.0.1_YTQ4OTI1NTY2OWY3YzY0MDM1N2E5YTFlODJiMDkxYWE1ZjUzNzUxNTc4ZjIxNjhmMTAzOTViMTRkN2ZkZDQ3MjFiZjhjNDY1N2VkMTI4NTNmYzM2NjY5NjAyNzYzZTY3NzVmNjU1NGQxOGRiZmI3OWRkZmJmNzc3ZTk5NzcxY2UwMTA2NDYyZGFhYjZhZGVkMGM0ZWM5NThjMGFiYjVlNg==; _ga_06ZNKL8C2E=GS1.1.1736788921.3.1.1736788992.49.0.0"""

ADMINS = [5321385511]


BOT_USERNAME = "Terabox_Links_To_Videos_bot"

# Force user to join this channel. (make sure you have promoted the bot on this chat.)
FORCE_LINK = "@Terabox_Links_To_Videos"

PUBLIC_EARN_API = "853a417e6360effc641fbe39633b730869df8e21"  # https://publicearn.com/api
