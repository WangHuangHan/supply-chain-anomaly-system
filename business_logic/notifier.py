# business_logic/notifier.py

def send_alert(record):
    print(f"ALERT: SKU {record['sku']} on {record['date']} is HIGH RISK")