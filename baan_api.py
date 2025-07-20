# baan_api.py

def get_baan_data():
    """
    Placeholder function for fetching data from BAAN.
    In future: Use requests or other lib to call BAAN REST/SOAP API.
    """
    # TODO: Replace this mock with actual BAAN API integration
    dummy_baan_data = {
        "orders": [
            {"id": "ORD123", "status": "Confirmed", "amount": 50000},
            {"id": "ORD124", "status": "Pending", "amount": 32000}
        ]
    }

    return dummy_baan_data
