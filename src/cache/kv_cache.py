import torch


class KVCache:
    def __init__(self):
        self.cache = # backend cache structure?

        # how many tokens are currently cached
        self.cur_len = 0

    # initialize our cache during model prefill phase
    def initialize_cache(self, ):
        self.cache = 
        

    # update the cache from the decode phase
    def update_cache(self, new_token_id):

        # we added a token to the cache
        self.cur_len += 1

    # get the length of our cache
    # this method exists in addition to cur_len attribute because 
    def get_cache_length(self):
        return self.cur_len
