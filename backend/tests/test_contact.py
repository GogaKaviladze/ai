from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_contact_create(monkeypatch):
    def fake_enqueue(func, contact_id):
        return None
    monkeypatch.setattr("app.api.routes.Queue.enqueue", lambda self, func, contact_id: fake_enqueue(func, contact_id))
    payload = {"name": "Max", "email": "max@example.com", "message": "Hallo"}
    r = client.post("/api/v1/contact", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "Max"
