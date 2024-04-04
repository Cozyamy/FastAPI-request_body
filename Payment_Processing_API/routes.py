from fastapi import APIRouter, Response, Depends
from models import PaymentModel, TransactionModel
from services import complete_transaction

router = APIRouter(tags=['Payment Processing'])

@router.post('/payments', response_model=TransactionModel)
async def make_payment(
    payment: PaymentModel,
    response: Response
):
    data = complete_transaction(payment)

    if "error" in data: #pragma: no cover
        response.status_code = 400
        return data
    response.status_code = 200
    return data