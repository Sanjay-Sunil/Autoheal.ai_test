# AutoHeal.ai Patch
# Gate Decision: confirm
def transform_payload(data):
    # Correct the 'amount' field by dividing by 100 to reverse the 100x scaling drift.
    corrected_amount = data.get('amount', 0.0) / 100.0

    # Restructure the payload to match the vendor's OpenAPI schema.
    # Map 'user_id' from the original payload to 'transaction.user_uuid'.
    # Convert user_id to a string. Note: This does not guarantee a valid UUID format
    # if the original user_id was not designed to be a UUID or convertible to one.
    user_uuid_value = str(data.get('user_id'))

    transformed_data = {
        'transaction': {
            'total_amount': corrected_amount,
            'user_uuid': user_uuid_value
        }
    }
    return transformed_data
