from fastapi import APIRouter, Response
from models import UserModel
from services import create_new_user


router = APIRouter(prefix='/api', tags=['User Registration'])


@router.post('/register')
async def register_user(userdata: UserModel, response: Response):
    message = create_new_user(userdata)

    if isinstance(message, dict):
        if "error" in message:
            response.status_code = 409
            return {"error": message["error"]}
        else:
            response.status_code = 201
            return {"message": "Successfully created"}