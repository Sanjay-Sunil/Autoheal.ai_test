# --- AUTOHEAL.AI AUTO-PATCH ---
import uuid

def transform_payload(data):
    user_id = data.get("user_id")
    amount = data.get("amount")

    # Generate a deterministic UUID from user_id
    # Using uuid.NAMESPACE_URL as a consistent namespace
    user_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, str(user_id)))

    return {
        "transaction": {
            "total_amount": amount,
            "user_uuid": user_uuid
        }
    }
