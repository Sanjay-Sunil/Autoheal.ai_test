# AutoHeal.ai Patch
# Gate Decision: auto_merge
import uuid

def transform_payload(data):
    user_id_str = str(data.get('user_id', ''))
    user_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, user_id_str))
    
    return {
        'transaction': {
            'total_amount': data.get('amount'),
            'user_uuid': user_uuid
        }
    }
