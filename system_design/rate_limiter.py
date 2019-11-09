import time

class RateLimiter:
    def __init__(self):
        self.hour_limit = 500
        self.minute_limit = 10
        self.hashmap = {}

    def request(self, user_id):
        count = 0
        current_time = time.time()
        curr_key = None

        if user_id in self.hashmap:
            for key, value in self.hashmap[user_id]:
                if key - current_time > 3600:
                    del self.hashmap[key]
                else:
                    if key - current_time < 600:
                        curr_key = key
                    count += value

        else:
            self.hashmap[user_id] = {current_time: 1}
            return "200: Success"

        if count >= self.hour_limit or self.hashmap[user_id][curr_key] >= self.minute_limit:
            return "429: Too many requests"
        
        if not curr_key:
            self.hashmap[user_id][current_time] = 1
            return "200: Success"

        self.hashmap[user_id][curr_key] += 1
        return "200: Success"
                    
