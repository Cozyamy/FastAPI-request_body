from fastapi import APIRouter, Query, Path, Response
from services import get_vehicle_by_id, get_vehicles

router = APIRouter(prefix="/api", tags=["Vehicle Inventory"])

@router.get("/vehicles/{vehicle_id}")
async def get_vehicle_by_id_route(
    response: Response,
    vehicle_id: int = Path(
        ...,
        title="Vehicle ID",
        description="Unique identifier for the vehicle",
        ge=1,
    ),
):
    data = get_vehicle_by_id(vehicle_id) #pragma: no cover
    if data is None: #pragma: no cover
        response.status_code = 404
        return {"error": "Vehicle not found"}

    response.status_code = 200 #pragma: no cover
    return data.dict() #pragma: no cover


@router.get("/vehicles")
async def get_vehicle_by_params_route(
    response: Response,
    make: str = Query(
        None,
        title="Make",
        description="Make of the vehicle",
    ),
    model: str = Query(
        None,
        title="Model",
        description="Model of the vehicle",
    ),
    price_range: str = Query(
        "10000-200000",
        title="Price Range",
        description="Price range of the vehicle",
    ),
):
    data = get_vehicles(make, model, price_range) #pragma: no cover
    if isinstance(data, dict) and "error" in data: #pragma: no cover
        response.status_code = 404
        return data

    response.status_code = 200 #pragma: no cover
    return [vehicle.dict() for vehicle in data] #pragma: no cover