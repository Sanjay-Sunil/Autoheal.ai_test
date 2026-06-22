# --- AUTOHEAL.AI AUTO-PATCH ---
import uuid

def transform_payload(data):
    user_id_str = str(data["user_id"])
    user_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, user_id_str))
    return {
        "transaction": {
            "total_amount": data["amount"],
            "user_uuid": user_uuid
        }
    }
