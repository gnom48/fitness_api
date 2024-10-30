import inspect
from typing import List, Type
from .database.orm import new_session
from sqlalchemy.sql import text
from .database.models import *
from .api.models import *
import time
import logging
from sqlalchemy import select, update, delete, and_
from pydantic import BaseModel
import time

assotiative_types = {
    PersonalDataModel: PersonalData,
    WorkoutModel: Workout,
    ExerciseModel: Exercise,
    StatisticModel: Statistic,
    WorkoutHistoryModel: WorkoutHistory,
    NutritionModel: Nutrition,
}

class DBRepository:
    @classmethod
    async def delete_entity(cls, id: int, data_type: Type[BaseModel]) -> bool:
        async with new_session() as session:
            try:
                service_to_delete = await session.get(assotiative_types[data_type], id)
                await session.delete(service_to_delete)
                await session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @classmethod
    async def get_all_entity(cls, data_type: Type[BaseModel]) -> List[BaseModelOrm]:
        async with new_session() as session:
            try:
                result = await session.execute(select(assotiative_types[data_type]))
                return result.scalars().all()
            except Exception as e:
                print(e)
                return []

    @classmethod
    async def get_entity_by_id(cls, data_type: Type[BaseModel], id: int) -> Optional[BaseModelOrm]:
        async with new_session() as session:
            try:
                return await session.get(assotiative_types[data_type], id)
            except Exception as e:
                print(e)
                return None

    @classmethod
    async def add_entity(cls, data: BaseModel) -> bool:
        async with new_session() as session:
            try:
                model = assotiative_types[type(data)](**data.dict())
                try:
                    model.id = None
                except:
                    pass
                session.add(model)
                await session.commit()
                return True
            except Exception as e:
                print(e)
                return False

    @classmethod
    async def update_entity(cls, id: int, data: BaseModel) -> bool:
        async with new_session() as session:
            try:
                entity = await session.get(assotiative_types[type(data)], id)
                for key, value in data.dict().items():
                    setattr(entity, key, value)
                await session.commit()
                return True
            except Exception as e:
                print(e)
                return False
            
    # -------------------------------- person -------------------------------- #

    @classmethod
    async def get_personal_data_by_login_password(cls, contact_info: str, password: str) -> Optional[PersonalData]:
        async with new_session() as session:
            try:                
                result = await session.execute(
                    select(PersonalData).where(PersonalData.contact_info == contact_info, PersonalData.password == password)
                )
                return result.scalars().first()
            except Exception as e:
                print(e)
                return None