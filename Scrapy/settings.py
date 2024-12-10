# Enable user-agent rotation using fake_useragent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Set up the Random User-Agent Middleware
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'your_project_name.middlewares.RandomUserAgentMiddleware': 400,  # Enable our custom middleware
}

# Enable Throttling
DOWNLOAD_DELAY = 1  # Delay between requests in seconds
AUTOTHROTTLE_ENABLED = True  # Enable AutoThrottle
AUTOTHROTTLE_START_DELAY = 1  # Initial download delay (seconds)
AUTOTHROTTLE_MAX_DELAY = 3  # Maximum download delay (seconds)
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Average number of requests to send concurrently

# Enable logging
LOG_LEVEL = 'INFO'
