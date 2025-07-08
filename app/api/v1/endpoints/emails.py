from fastapi import APIRouter, HTTPException, status
from uuid import UUID

from app.schemas.email import Email
from app.utils.email_store import get_emails, get_email_by_id

router = APIRouter()


@router.get("/", response_model=list[Email], status_code=status.HTTP_200_OK)
async def get_all_emails() -> list[Email]:
    """
    Get all emails from the store.

    Returns:
        List of all emails

    Raises:
        HTTPException: If there's an error retrieving emails
    """
    try:
        return get_emails()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving emails: {str(e)}",
        )


@router.get("/{email_id}", response_model=Email, status_code=status.HTTP_200_OK)
async def get_email(email_id: UUID) -> Email:
    """
    Get a specific email by ID.

    Args:
        email_id: The ID of the email to retrieve

    Returns:
        Email object if found

    Raises:
        HTTPException: If email is not found or there's an error
    """
    try:
        email = get_email_by_id(email_id)
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Email with id {email_id} not found",
            )
        return email
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving email: {str(e)}",
        )
