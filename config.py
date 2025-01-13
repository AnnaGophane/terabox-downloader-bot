import os

class Config:
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    REDIS_URI = os.environ.get("REDIS_URL", "") # Heroku Redis URL
    REDIS_PORT = os.environ.get("REDIS_PORT", "")
    REDIS_PASS = os.environ.get("REDIS_PASS", "")
    OWNER = os.environ.get("Ravanraj21", "")  # Bot owner's username


API_ID = 22620071  # api id
API_HASH = "85b7c68ac5da126389cfb9bbb89a5190"  # api hash

BOT_TOKEN = "7902732073:AAFVrEh5cyaJXhmur-vOCSMUIoay5DyLtXg"  # bot token


# REDIS
HOST = "redis-14201.c15.us-east-1-2.ec2.redns.redis-cloud.com:14201"  # redis host uri
PORT = 6379  # redis port
PASSWORD = "1hlUwaWzkStWzk0AcdiSSUBIwkHBKARc"  # redis password

PRIVATE_CHAT_ID = -1002315965012  # CHAT WHERE YOU WANT TO STORE VIDEOS
# COOKIE FOR AUTHENTICATION (get from chrome dev tools) ex: "PANWEB=1; csrfToken=;
COOKIE = "TSID=KGQXgFvgYgnwRJyx1zXCFMQ2hOPu87ot; __bid_n=1918fe6e58b6c4b0e24207; _ga=GA1.1.966127542.1724696176; g_state={"i_l":0}; ndus=YyYP664teHuisg26Y083n59lsWLAoPkK1rrlN14i; PANWEB=1; browserid=TzHtqXtjz8v8OXd4ThrPzk8Z2lsQf66ybvWfogKMjsz8ZzSTgogC9U35k5k=; lang=en; csrfToken=PcnfIYSm-V_OLF8sLee2BTxP; _gcl_au=1.1.1234066097.1736772371; _fbp=fb.1.1736772372121.332307306828524343; _tt_enable_cookie=1; _ttp=8SHKFaBMwKYtQMiyjrH2B-iRosQ.tt.1; _ga_K6JMPYL99R=GS1.1.1736772371.1.1.1736772924.0.0.0; _ga_RSNVN63CM3=GS1.1.1736772372.1.1.1736772924.60.0.0; ndut_fmt=99E7D9B531B397D9EEBE374DFB8E8F0DF923A45FBAD2962424AF11691022ADA2; ab_sr=1.0.1_YjI3YTgxNWMwZWI3ZjhjNzg2YTdjYzc1MzIzYjdmMTcxMGE1YWE0YzJjYWUyMmQ5NGJjNmZkZmI1Mzc0NzljMzBmMjQ2NGI1ZjVjMGRmYzQzZjVmZWIxODY2YjM3ZTc4MDg1YzgzMDMwNDIwZjM1NDkxYWI4YTc4NDRhY2JhYTgyOGU1YzMyZjliNDJlOTk5NDdmZDU3OGQ3MmVmMWVhMQ==; _ga_06ZNKL8C2E=GS1.1.1736771205.1.1.1736773299.60.0.0"
ADMINS = [5321385511]


BOT_USERNAME = "Terabox_Links_To_Videos_bot"

# Force user to join this channel. (make sure you have promoted the bot on this chat.)
FORCE_LINK = "@Terabox_Links_To_Videos"

PUBLIC_EARN_API = "853a417e6360effc641fbe39633b730869df8e21"  # https://publicearn.com/api
