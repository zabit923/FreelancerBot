from pydantic import BaseModel


class Option(BaseModel):
    id: int
    key: str
    text: str
    subtitle: str
    icon_url: str
    display_order: int


class Question(BaseModel):
    id: int
    key: str
    type: str
    text: str
    description: str
    required: bool
    has_text_input: bool
    text_input_type: str
    text_input_description: str
    text_input_placeholder: str
    has_file_input: bool
    file_input_types: str
    file_input_button_text: str
    link_url: str
    link_text: str
    options: list[Option]


class Section(BaseModel):
    name: str
    questions: list[Question]


class OrderFormResponse(BaseModel):
    sections: list[dict]
