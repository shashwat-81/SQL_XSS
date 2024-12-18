import requests

def test_xss():
    payload = "<script>alert('XSS')</script>"
    response = requests.post("http://127.0.0.1:5000/", data=payload)
    assert response.status_code == 403

