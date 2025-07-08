from uuid import UUID
from datetime import datetime
from app.utils.email_store import get_emails, get_email_by_id, save_email
from app.schemas.email import Email


def test_get_emails():
    """Test getting all emails."""
    emails = get_emails()
    assert isinstance(emails, list)

    if emails:  # If emails exist in the data file
        assert len(emails) > 0
        assert all(isinstance(email, Email) for email in emails)


def test_get_email_by_id():
    """Test getting a specific email by ID."""
    emails = get_emails()

    if emails:  # If emails exist
        # Test getting first email
        first_email = get_email_by_id(emails[0].id)
        assert first_email is not None
        assert first_email.id == emails[0].id

    # Test getting non-existent email
    non_existent_id = UUID("00000000-0000-0000-0000-000000000000")
    email = get_email_by_id(non_existent_id)
    assert email is None


def test_save_email():
    """Test saving an email."""
    # Create a test email
    test_email = Email(
        subject="Test Subject",
        email_content="Test email content",
        sender="test@example.com",
        date=datetime.now(),
    )

    # Save the email
    saved_email = save_email(test_email)

    # Verify it was saved with an ID
    assert saved_email.id is not None
    assert saved_email.subject == "Test Subject"
    assert saved_email.email_content == "Test email content"
    assert saved_email.sender == "test@example.com"

    # Verify it can be retrieved
    retrieved_email = get_email_by_id(saved_email.id)
    assert retrieved_email is not None
    assert retrieved_email.id == saved_email.id
    assert retrieved_email.subject == saved_email.subject
