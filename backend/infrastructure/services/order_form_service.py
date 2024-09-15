from api.models import OrderFormResponse

from database.repo.requests import RequestRepo


class OrderFormService:
    def __init__(self, repo: RequestRepo):
        self.repo = repo

    async def get_order_form(self) -> OrderFormResponse:
        data: dict = await self.repo.questions.get_order_form()
        return OrderFormResponse(**data)
