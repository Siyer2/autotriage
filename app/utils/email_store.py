import json
from typing import Optional
from pathlib import Path
from uuid import UUID

from app.schemas.email import Email

# Data file path
DATA_FILE = Path("data/emails.json")


def get_emails() -> list[Email]:
    """Get all emails from the JSON store.

    Returns:
        List of all emails

    Raises:
        FileNotFoundError: If the data file doesn't exist
        json.JSONDecodeError: If the data file contains invalid JSON
    """
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Data file {DATA_FILE} does not exist")

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Email(**email_data) for email_data in data]


def get_email_by_id(email_id: UUID) -> Optional[Email]:
    """Get a specific email by ID.

    Args:
        email_id: The ID of the email to retrieve

    Returns:
        Email object if found, None otherwise
    """
    emails = get_emails()
    return next((email for email in emails if email.id == email_id), None)


def save_email(email: Email) -> Email:
    """Save an email to the JSON store.

    Args:
        email: Email object to save. ID will be auto-generated if creating a new email.

    Returns:
        The saved email with its ID
    """
    # Ensure data directory exists
    DATA_FILE.parent.mkdir(exist_ok=True)

    # Get existing emails
    emails = get_emails()

    # Add or update the email
    existing_index = next((i for i, e in enumerate(emails) if e.id == email.id), None)
    if existing_index is not None:
        emails[existing_index] = email
    else:
        emails.append(email)

    # Save back to file
    data = [email.model_dump() for email in emails]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)

    return email
