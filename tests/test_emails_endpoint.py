from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_emails():
    """Test the get all emails endpoint."""
    response = client.get("/api/v1/emails/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:  # If emails exist
        # Check first email structure
        email = data[0]
        assert "id" in email
        assert "sender" in email
        assert "date" in email
        assert "subject" in email
        assert "email_content" in email
