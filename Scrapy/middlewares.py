from fake_useragent import UserAgent
import random
import time

class RandomUserAgentMiddleware:
    def __init__(self):
        self.ua = UserAgent()

    def process_request(self, request, spider):
        # Set a random user-agent
        user_agent = self.ua.random
        request.headers['User-Agent'] = user_agent

        # Introduce random delay between requests (throttling)
        time.sleep(random.uniform(2, 4))  # Random delay between 2 to 4 seconds
