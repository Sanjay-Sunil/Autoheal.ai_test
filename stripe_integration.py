#dummy file for integrating automated pr in autoheal.ai
import uuid

def transform_payload(data):
    return {
        "transaction": {
            "total_amount": data["amount"],
            "user_uuid": str(uuid.uuid5(uuid.NAMESPACE_OID, str(data["user_id"])))
        }
    }