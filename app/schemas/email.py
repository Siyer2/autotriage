from pydantic import BaseModel, Field, ConfigDict, field_serializer
from datetime import datetime
from uuid import UUID, uuid4


class Email(BaseModel):
    """Email data model."""

    model_config = ConfigDict()

    id: UUID = Field(default_factory=uuid4, description="Unique email identifier")
    sender: str = Field(..., description="Email sender address")
    date: datetime = Field(..., description="Email date and time")
    subject: str = Field(..., description="Email subject")
    email_content: str = Field(..., description="Email content")

    @field_serializer("date")
    def serialize_date(self, value: datetime) -> str:
        return value.isoformat()


class EmailList(BaseModel):
    """List of emails response model."""

    emails: list[Email] = Field(..., description="List of emails")
    total: int = Field(..., description="Total number of emails")
