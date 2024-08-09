from datetime import datetime
from typing import Optional
from sqlalchemy import (
    VARCHAR,
    BIGINT,
    false,
    TIMESTAMP
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import (
    Base,
    TableNameMixin,
    str_128,
    str_255,
    timestamp_now,
)


class User(Base, TableNameMixin):
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    full_name: Mapped[str_128]
    username: Mapped[Optional[str]] = mapped_column(VARCHAR(64))
    email: Mapped[Optional[str_255]] = mapped_column(unique=True)
    password_hash: Mapped[Optional[str_255]]
    is_premium: Mapped[bool] = mapped_column(server_default=false())

    created_at: Mapped[timestamp_now]
    last_login: Mapped[Optional[datetime]] = mapped_column(TIMESTAMP)
