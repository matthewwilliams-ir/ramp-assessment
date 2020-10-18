
def test_multiply(client):
    input_data = '{"input": "0.1,0.9,0.123,0.99,0.5,1.0,0"}'
    response = client.post('/transform/multiply', data=input_data)
    
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert {"Week 1", "Week 2", "Week 3"}.issubset(set(response.json.keys()))
    assert {"1": 0.1,"2": 0.9,"3": 0.123,"4": 0.99,"5": 0.5,"6": 1.0,"7": 0.0} == response.json["Week 1"]
    assert {"1": 0.2,"2": 1.8,"3": 0.246,"4": 1.98,"5": 1.0,"6": 2.0,"7": 0.0} == response.json["Week 2"]
    assert {"1": 0.3,"2": 2.7,"3": 0.369,"4": 2.97,"5": 1.5,"6": 3.0,"7": 0.0} == response.json["Week 3"]

def test_multiply_not_json(client):
    input_data = '{/'
    response = client.post('/transform/multiply', data=input_data)

    assert response.status_code == 400
    assert b"Failed to decode JSON object" in response.data

def test_multiply_empty_json(client):
    input_data = '{}'
    response = client.post('/transform/multiply', data=input_data)

    assert response.status_code == 400
    assert b"Expected JSON object with string 'input' attribute" in response.data

def test_multiply_missing_attr(client):
    input_data = '{"other": ""}'
    response = client.post('/transform/multiply', data=input_data)

    assert response.status_code == 400
    assert b"Missing 'input' attribute" in response.data

def test_multiply_unexpected_chars(client):
    input_data = '{"input": "54a, abc"}'
    response = client.post('/transform/multiply', data=input_data)

    assert response.status_code == 400
    assert b"Provide 'input' attribute contains unexpected characters" in response.data

def test_multiply_length(client):
    input_data = '{"input": "0.1,0.9,0.123,0.99"}'
    response = client.post('/transform/multiply', data=input_data)

    assert response.status_code == 400
    assert b"Expected 7 comma-separated decimal values" in response.data