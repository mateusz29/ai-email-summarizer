from datetime import UTC, datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class EmailSummary(Base):
    __tablename__ = "email_summaries"

    id: Mapped[int] = mapped_column(primary_key=True)
    email_text: Mapped[str] = mapped_column(String, nullable=False)
    summary: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC), nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"EmailSummary(id={self.id}, email_text={self.email_text},"
            f"summary={self.summary}, created_at={self.created_at})"
        )
