import requests

def test_sqli():
    payload = "' OR 1=1; --"
    response = requests.post("http://127.0.0.1:5000/", data=payload)
    assert response.status_code == 403
