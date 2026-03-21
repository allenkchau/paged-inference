
class Request:
    def __init__(self, request_id, prompt_text, prompt_token_ids: list[int], max_new_tokens, eos_token_id):
        # identity
        self.request_id = request_id

        # input/output content
        # we store the token ids in the request object as Python lists
        self.prompt_text = prompt_text
        self.prompt_token_ids = prompt_token_ids
        self.generated_token_ids: list[int] = []

        # generation constraints
        self.max_new_tokens = max_new_tokens
        self.eos_token_id = eos_token_id

        # status
        self.finished = False

    def get_prompt_length(self) -> int:
        return len(self.prompt_token_ids)

    def get_generated_length(self) -> int:
        return len(self.generated_token_ids)

    def get_total_length(self) -> int:
        return len(self.prompt_token_ids) + len(self.generated_token_ids)

    def get_total_token_ids(self) -> list[int]:
        return self.prompt_token_ids + self.generated_token_ids

    def append_token(self, new_token: int):
        self.generated_token_ids.append(new_token)
        if new_token == self.eos_token_id or self.get_generated_length() == self.max_new_tokens:
            self.finished = True

    

