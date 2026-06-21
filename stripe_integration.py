#dummy file for integrating automated pr in autoheal.ai

# --- AEGIS AUTO-PATCH ---
def transform_payload(data):
    transformed_data = {
        "transaction": {
            "user_uuid": str(data["user_id"]),
            "total_amount": data["amount"]
        }
    }
    return transformed_data
