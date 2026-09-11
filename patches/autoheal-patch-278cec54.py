# AutoHeal.ai Automated Patch
# Source: backend/product_backend.py
# Gate Decision: auto_merge

import uuid

def transform_payload(data):
    user_id = data.get('user_id')
    amount = data.get('amount')

    # Generate a deterministic UUID based on user_id
    # Using a fixed namespace to ensure determinism for the same user_id
    namespace_uuid = uuid.UUID('f9b1c2d3-e4f5-6789-0123-456789abcdef')
    user_uuid = str(uuid.uuid5(namespace_uuid, str(user_id)))

    new_payload = {
        'transaction': {
            'total_amount': amount,
            'user_uuid': user_uuid
        }
    }
    return new_payload
