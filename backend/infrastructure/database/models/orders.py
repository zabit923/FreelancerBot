import enum
import datetime

from sqlalchemy import (
    ForeignKey,
    false,
    TIMESTAMP,
)
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from .base import (
    Base,
    TableNameMixin,
    int_pk,
    str_20,
    str_255,
    timestamp_now
)


class MarketArea(enum.Enum):
    GLOBAL = 'GLOBAL'
    EUROPE = 'EUROPE'
    ASIA = 'ASIA'
    AMERICA = 'AMERICA'
    AFRIKA = 'AFRIKA'
    AUSTRALIA = 'AUSTRALIA'


class OrderStatus(enum.Enum):
    DRAFT = 'DRAFT'
    ON_MODERATION = 'ON_MODERATION'
    APPROVED = 'APPROVED'
    COMPLETED = 'COMPLETED'
    ARCHIVED = 'ARCHIVED'


class Order(Base, TableNameMixin):
    order_id: Mapped[int_pk]
    client_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    title: Mapped[str_255]
    description: Mapped[Optional[str]]
    deadline: Mapped[Optional[datetime.date]]
    status: Mapped[OrderStatus] = mapped_column(server_default=OrderStatus.DRAFT.value)

    is_promoted: Mapped[bool] = mapped_column(server_default=false())
    promoted_until: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)

    created_at: Mapped[timestamp_now]
    updated_at: Mapped[timestamp_now]


class OrderCountry(Base):
    __tablename__ = 'order_countries'

    order_country_id: Mapped[int_pk]
    order_id: Mapped[int] = mapped_column(ForeignKey(Order.order_id))
    country_key: Mapped[str_20]
