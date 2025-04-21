import uuid

class guess:
    def __init__(self, guess):
        self.guess = guess
        self.ue_registry = {}

    def register_ue(self, ue_id):
        print(f"[guess] UE {ue_id} requested registration.")
        session_info = self.guess.create_session(ue_id)
        self.ue_registry[ue_id] = session_info
        print(f"[guess] Session established for UE {ue_id}: {session_info}")
        return session_info


class guess_1:
    def __init__(self):
        self.sessions = {}

    def create_session(self, ue_id):
        print(f"[guess_1] Creating session for UE {ue_id}.")
        teid = self.generate_teid()
        ip = self.allocate_ip(ue_id)
        session = {"teid": teid, "ip": ip}
        self.sessions[ue_id] = session
        print(f"[guess_1] Session created for UE {ue_id}: {session}")
        return session

    def generate_teid(self):
        return uuid.uuid4().int & 0xFFFFFFFF

    def allocate_ip(self, ue_id):
        base_ip = "10.10.0."
        last_octet = 100 + len(self.sessions)
        return f"{base_ip}{last_octet}"