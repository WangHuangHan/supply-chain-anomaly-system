import logging

logging.basicConfig(filename="monitoring.log", level=logging.INFO)

def log_prediction(record):
    logging.info(f"Predicted anomaly for SKU {record['sku']}")