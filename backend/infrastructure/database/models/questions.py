import enum
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    true,
    false,
    ForeignKey,
)

from .base import (
    Base,
    TableNameMixin,
    int_pk,
    str_50,
)


class QuestionCategory(enum.Enum):
    ORDER = 'ORDER'
    FREELANCER_PROFILE = 'FREELANCER_PROFILE'
    CLIENT_PROFILE = 'CLIENT_PROFILE'


class TextInputType(enum.Enum):
    text = 'text'
    date = 'date'
    number = 'number'
    email = 'email'
    password = 'password'
    tel = 'tel'
    textarea = 'textarea'


class QuestionType(enum.Enum):
    checkbox = 'checkbox'
    radio = 'radio'
    vertical_slider = 'vertical_slider'
    drag_and_drop = 'drag_and_drop'
    select = 'select'
    text = 'text'
    combobox = 'combobox'


class Question(Base, TableNameMixin):
    question_id: Mapped[int_pk]
    category: Mapped[QuestionCategory]
    section: Mapped[Optional[str_50]]
    question_key: Mapped[str_50] = mapped_column(unique=True)
    question_type: Mapped[QuestionType]
    question_text: Mapped[str]
    question_description: Mapped[Optional[str]]

    link_url: Mapped[Optional[str]]
    link_text: Mapped[Optional[str]]

    is_required: Mapped[bool] = mapped_column(server_default=true())

    has_text_input: Mapped[bool] = mapped_column(server_default=false())
    text_input_type: Mapped[Optional[TextInputType]]
    text_input_description: Mapped[Optional[str]]
    text_input_placeholder: Mapped[Optional[str]]

    has_file_input: Mapped[bool] = mapped_column(server_default=false())
    file_input_types: Mapped[Optional[str]]
    file_input_button_text: Mapped[Optional[str]]

    display_order: Mapped[int]
    parrent_question_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('questions.question_id')
    )
    condition_option_id: Mapped[Optional[int]]
