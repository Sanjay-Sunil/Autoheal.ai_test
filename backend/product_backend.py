import sys
import httpx
import aegis_agent
import uuid

# Avoid unicode encode errors on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def transform_payload(data):
    user_id = data.get('user_id')
    amount = data.get('amount')
    user_uuid = str(uuid.uuid5(uuid.NAMESPACE_OID, str(user_id)))
    new_payload = {"transaction": {"total_amount": amount, "user_uuid": user_uuid}}
    return new_payload

def checkout():
    """
    Simulates your main E-commerce Backend trying to process an order.
    """
    print("\n[Product Backend] User clicked Checkout. Initiating payment...")
    
    # This is the OLD payload format that our product currently uses.
    # We don't know the vendor changed their rules overnight!
    old_cart_payload = {
        "user_id": 12345,
        "amount": 99.00
    }
    
    # Intercept and transform the payload to the new format
    print("[Product Backend] Transforming payload to new vendor format...")
    new_cart_payload = transform_payload(old_cart_payload)
    
    target_url = "http://127.0.0.1:8000/pay"

    try:
        # We attempt the HTTP request to the vendor with the transformed payload
        response = httpx.post(target_url, json=new_cart_payload)
        
        # This raises an exception if the status code is 4xx or 5xx
        response.raise_for_status() 
        
        print("[Product Backend] Order placed successfully!")
        return response.json()
        
    except httpx.HTTPStatusError as e:
        # THE TRAP: We catch the HTTP error instead of letting the app crash!
        if e.response.status_code == 400:
            error_details = e.response.json().get('detail', e.response.text)
            print("\n[Product Backend] CAUGHT 400 ERROR from Vendor!")
            print(f"Error Message: {error_details}")
            
            # Delegate to Aegis Agent, passing the *transformed* payload
            print("\n[Product Backend] Delegating payload and error to Aegis Remediation Agent...")
            try:
                healed_response = aegis_agent.heal_and_retry(new_cart_payload, error_details, target_url)
                print(f"[Product Backend] Order placed successfully after self-healing: {healed_response}")
                return healed_response
            except Exception as healing_err:
                print(f"[Product Backend] Aegis Remediation failed: {healing_err}")
                return {"status": "failed", "reason": str(healing_err)}
        else:
            # If it's a 500 server down error, we can't heal that.
            print(f"[Product Backend] Fatal error {e.response.status_code}")
            raise

if __name__ == "__main__":
    # Run the checkout simulation
    checkout()