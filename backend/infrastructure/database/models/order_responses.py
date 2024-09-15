from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from .base import (
    Base,
    int_pk,
    str_500,
)


class OrderResponse(Base):
    __tablename__ = 'order_responses'

    response_id: Mapped[int_pk]
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.order_id'))
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.question_id'))
    selected_option_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('options.option_id')
    )
    text_response: Mapped[Optional[str_500]]


class OrderResponseFile(Base):
    __tablename__ = 'order_response_files'

    file_id: Mapped[int_pk]
    response_id: Mapped[int] = mapped_column(ForeignKey(OrderResponse.response_id))
    file_url: Mapped[str]
    file_name: Mapped[str]
    file_size: Mapped[int]
    file_type: Mapped[str_500]
