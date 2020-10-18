
def test_index(client):
    response = client.get('/')
    assert b"Hello, World!" in response.data

def test_multiply(client):
    input = "0.1,0.9,0.123,0.99,0.5,1.0,0"
    response = client.post('/multiply', data='{{"input": "{}"}}'.format(input))
    assert b"0.1,0.9,0.123,0.99,0.5,1.0,0" in response.data