import hashlib

class guess:
    def __init__(self):
        self.subscriber_db = {
            "ue-001": {"key": "secret001"},
            "ue-002": {"key": "secret002"}
        }

    def get_authentication_data(self, ue_id):
        return self.subscriber_db.get(ue_id, None)


class guess_2:
    def __init__(self, udm):
        self.udm = udm

    def authenticate(self, ue_id, challenge_response):
        subscriber = self.udm.get_authentication_data(ue_id)
        if not subscriber:
            print(f"[] Unknown UE ID: {ue_id}")
            return False

        expected = self.generate_challenge_response(subscriber["key"])
        if challenge_response == expected:
            print(f"[!] UE {ue_id} authenticated successfully.")
            return True
        else:
            print(f"[!] UE {ue_id} authentication failed.")
            return False

    def generate_challenge(self, key):
        return self.generate_challenge_response(key)

    def generate_challenge_response(self, key):
        return hashlib.sha256(key.encode()).hexdigest()