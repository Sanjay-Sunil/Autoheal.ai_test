# AutoHeal.ai Patch
# Gate Decision: confirm
def transform_payload(data):
    # This function corrects the drift by using the nominal 'amount'
    # and transforming the payload to the vendor's expected structure.
    transformed_data = {
        "transaction": {
            "total_amount": data["amount"], # Corrected: no multiplication
            "user_uuid": str(data["user_id"]) # Type conversion
        }
    }
    return transformed_data
