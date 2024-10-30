from fastapi import APIRouter, HTTPException, Header, Request
from .models import *
from ..repository import *
from datetime import datetime


router_person = APIRouter(prefix="/person", tags=["Person"])

@router_person.get("/personal_data/auth", response_model=PersonalDataModel)
async def read_personal_data(contact_info: str, password: str):
    personal_data = await DBRepository.get_personal_data_by_login_password(contact_info, password)
    if personal_data:
        return personal_data
    else:
        raise HTTPException(status_code=404, detail="Personal data not found")

@router_person.post("/personal_data/")
async def create_personal_data(personal_data: PersonalDataModel):
    success = await DBRepository.add_entity(personal_data)
    if success:
        return {"message": "Personal data created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create personal data")

@router_person.get("/personal_data/", response_model=List[PersonalDataModel])
async def read_all_personal_data():
    personal_data_list = await DBRepository.get_all_entity(PersonalDataModel)
    if personal_data_list:
        return personal_data_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve personal data")

@router_person.get("/personal_data/{id}", response_model=PersonalDataModel)
async def read_personal_data(id: int):
    personal_data = await DBRepository.get_entity_by_id(PersonalDataModel, id)
    if personal_data:
        return personal_data
    else:
        raise HTTPException(status_code=404, detail="Personal data not found")

@router_person.put("/personal_data/{id}")
async def update_personal_data(id: int, personal_data: PersonalDataModel):
    success = await DBRepository.update_entity(id, personal_data)
    if success:
        return {"message": "Personal data updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update personal data")

@router_person.delete("/personal_data/{id}")
async def delete_personal_data(id: int):
    success = await DBRepository.delete_entity(id, PersonalDataModel)
    if success:
        return {"message": "Personal data deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete personal data")

@router_person.get("/nutrition/", response_model=List[NutritionModel])
async def read_all_nutrition():
    nutrition_list = await DBRepository.get_all_entity(NutritionModel)
    if nutrition_list:
        return nutrition_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve nutrition")