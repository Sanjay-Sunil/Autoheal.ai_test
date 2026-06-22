# --- AUTOHEAL.AI AUTO-PATCH ---
import uuid

def transform_payload(data):
    user_id = data.get('user_id')
    amount = data.get('amount')

    # Generate a deterministic UUID from user_id using uuid.NAMESPACE_OID
    user_uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, str(user_id)))

    new_payload = {
        "transaction": {
            "total_amount": amount,
            "user_uuid": user_uuid
        }
    }
    return new_payload
