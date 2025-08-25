import logging
import os
import sys
import threading
import typing
from typing import Any

from redis import Redis as r

import urllib.parse
from config import PASSWORD

log = logging.getLogger("telethon")


class Redis(r):    
    # In-memory cache
    _in_memory_cache = {}
    

    def __init__(
        self,
        host: str = None,
        port: int = None,
        password: str = None,
        logger=log,
        encoding: str = "utf-8",
        decode_responses=True,
        **kwargs,
    ):
        if ":" in host:
            data = host.split(":")
            host = data[0]
            port = int(data[1])
        if host.startswith("http"):
            logger.error("Your REDIS_URI should not start with http!")
            sys.exit()
        elif not host or not port:
            logger.error("Port Number not found")
            sys.exit()
        kwargs["host"] = host
        if password and len(password) > 1:
            kwargs["password"] = password
        kwargs["port"] = port
        kwargs["encoding"] = encoding
        kwargs["decode_responses"] = decode_responses
        # kwargs['client_name'] = client_name
        # kwargs['username'] = username
        try:
            super().__init__(**kwargs)
        except Exception as e:
            logger.error(f"❌ Error while connecting to Redis: {e}")
            logger.error(f"   Host: {host}")
            logger.error(f"   Port: {port}")
            if "Name or service not known" in str(e):
                logger.error("   DNS resolution failed - check if the hostname is correct")
            elif "Connection refused" in str(e):
                logger.error("   Connection refused - check if Redis server is running")
            elif "timed out" in str(e):
                logger.error("   Connection timed out - check network connectivity")
            logger.error("Please verify your Redis configuration and ensure the server is accessible")
            sys.exit()
        self.logger = logger
        self._cache = {}
        threading.Thread(target=self.re_cache).start()

    def re_cache(self):
        try:
            key = self.keys()
            for keys in key:
                self._cache[keys] = self.get(keys)
                self._in_memory_cache[keys] = self.get(keys)
            self.logger.info("Cached {} keys from Redis".format(len(self._cache)))
        except Exception as e:
            self.logger.warning("Could not cache from Redis: {}. Using in-memory cache only.".format(e))

    def get_key(self, key: Any):
        if key in self._cache:
            return self._cache[key]
        elif key in self._in_memory_cache:
            return self._in_memory_cache[key]
        else:
            try:
                data = self.get(key)
                if data:
                    self._cache[key] = data
                    self._in_memory_cache[key] = data
                return data
            except Exception:
                # If Redis is not available, return from in-memory cache
                return self._in_memory_cache.get(key)

    def del_key(self, key: Any):
        if key in self._cache:
            del self._cache[key]
        if key in self._in_memory_cache:
            del self._in_memory_cache[key]
        try:
            return self.delete(key)
        except Exception:
            return 0  # Return 0 if Redis is not available

    def set_key(self, key: Any = None, value: Any = None):
        self._cache[key] = value
        self._in_memory_cache[key] = value
        try:
            return self.set(key, value)
        except Exception:
            return True  # Return True even if Redis is not available
    
    # Add a method to check Redis availability
    def is_redis_available(self):
        try:
            return self.ping()
        except Exception:
            return False


# Use configuration from config.py which now handles REDIS_URL parsing
db = None
connection_error = None

try:
    redis_url = os.getenv('REDIS_URL')
    if redis_url:
        parsed_url = urllib.parse.urlparse(redis_url)
        HOST = parsed_url.hostname
        PORT = parsed_url.port
        PASSWORD = parsed_url.password
    else:
        # Fallback to config values if REDIS_URL is not set
        from config import HOST, PORT, PASSWORD

    log.info(f"Attempting to connect to Redis on {HOST}:{PORT}")
    db = Redis(
        host=HOST,
        port=PORT,
        password=PASSWORD if len(PASSWORD) > 1 else None,
        decode_responses=True,
        ssl=False,  # Disable SSL for testing
    )
    
    # Test connection
    if db.ping():
        log.info("✅ Redis connection successful!")
    else:
        log.error("❌ Redis ping failed")
        exit(1)
        
except Exception as e:
    connection_error = str(e)
    log.error(f"❌ Failed to connect to Redis: {e}")
    log.error("Please check your Redis configuration:")
    log.error(f"- HOST: {HOST}")
    log.error(f"- PORT: {PORT}")
    log.error("Make sure the Redis server is running and accessible")
    exit(1)
