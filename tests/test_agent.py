from fastapi.testclient import TestClient
from rca.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'draft rca', **{'payload': {'changed': True, 'saturated': False}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["hypothesis"] == "change"
    refused = client.post("/agent/run", json={"goal": 'close incident rca complete'}).json()
    assert refused["refused"] is True
