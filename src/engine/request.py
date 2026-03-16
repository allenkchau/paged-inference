class Request:
    def __init__(self, request_id, prompt_text, prompt_token_ids, generated_token_ids, max_new_tokens, finished=False):
        # identity
        self.request_id = request_id

        # input/output content
        self.prompt_text = prompt_text
        self.prompt_token_ids = prompt_token_ids
        self.generated_token_ids = generated_token_ids

        # generation constraints
        self.max_new_tokens = max_new_tokens

        # status
        self.finished = finished

    def get_prompt_length(self, ):
        pass

    def get_generated_length(self, ):
        pass

    

