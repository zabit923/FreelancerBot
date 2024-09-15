from fastapi import FastAPI, APIRouter

from .models import Question, OrderFormResponse, Section, Option
from services.order_form_service import OrderFormService

app = FastAPI()
api_router = APIRouter(prefix='/api')


@api_router.get(
    '/orders/form_structure',
    response_model=OrderFormResponse
)
async def form_structure():
    repo = None
    order_service = OrderFormService(repo)

    return order_service.get_order_form()


app.include_router(api_router)
