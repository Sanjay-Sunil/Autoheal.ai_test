# --- AUTOHEAL.AI AUTO-PATCH ---
import uuid

def transform_payload(data):
    user_id = data['user_id']
    amount = data['amount']
    deterministic_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, str(user_id)).hex
    return {
        "transaction": {
            "total_amount": amount,
            "user_uuid": deterministic_uuid
        }
    }
