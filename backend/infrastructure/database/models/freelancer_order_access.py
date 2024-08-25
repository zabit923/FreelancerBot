import enum
import datetime
from typing import Optional
from decimal import Decimal
from sqlalchemy import (
    ForeignKey,
    DECIMAL,
    TIMESTAMP,
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import (
    TableNameMixin,
    Base,
    int_pk,
    timestamp_now,
)


class BidAccessStatus(enum.Enum):
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'


class OrderBid(Base, TableNameMixin):
    bid_id: Mapped[int_pk]
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.order_id'))
    freelancer_id: Mapped[int] = mapped_column(ForeignKey('freelancerprofiles.profile_id'))
    bid_amount: Mapped[Optional[Decimal]] = mapped_column(DECIMAL(10, 2))
    proposal_text: Mapped[Optional[str]]
    status: Mapped[BidAccessStatus] = mapped_column(
        server_default=BidAccessStatus.PENDING.value
    )
    requested_at: Mapped[timestamp_now]
    granted_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
