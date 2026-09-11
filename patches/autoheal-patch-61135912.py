# AutoHeal.ai Automated Patch
# Source: backend/product_backend.py
# Gate Decision: auto_merge

import uuid

def transform_payload(data):
    user_id = data.get('user_id')
    amount = data.get('amount')

    user_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(user_id))) if user_id is not None else None

    new_payload = {
        'transaction': {
            'total_amount': amount,
            'user_uuid': user_uuid
        }
    }
    return new_payload
