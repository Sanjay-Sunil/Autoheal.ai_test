# AutoHeal.ai Patch
# Gate Decision: confirm
def transform_payload(data):
    transformed_data = {
        "transaction": {
            "total_amount": data["amount"] / 100.0,
            "user_uuid": str(data["user_id"])
        }
    }
    return transformed_data
