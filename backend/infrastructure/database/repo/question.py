from .base import BaseRepo


class QuestionRepo(BaseRepo):
    async def get_order_form(self) -> dict:
        return {}