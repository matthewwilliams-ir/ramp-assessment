
def test_multiply(client):
    input = "0.1,0.9,0.123,0.99,0.5,1.0,0"
    response = client.post('/multiply', data='{{"input": "{}"}}'.format(input))
    
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert isinstance(response.json, dict)
    assert {"Week 1", "Week 2", "Week 3"}.issubset(set(response.json.keys()))
    assert {"1": 0.1,"2": 0.9,"3": 0.123,"4": 0.99,"5": 0.5,"6": 1.0,"7": 0.0} == response.json["Week 1"]
    assert {"1": 0.2,"2": 1.8,"3": 0.246,"4": 1.98,"5": 1.0,"6": 2.0,"7": 0.0} == response.json["Week 2"]
    assert {"1": 0.3,"2": 2.7,"3": 0.369,"4": 2.97,"5": 1.5,"6": 3.0,"7": 0.0} == response.json["Week 3"]