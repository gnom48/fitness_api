from fastapi import APIRouter, HTTPException, Header, Request
from .models import *
from ..repository import *
from datetime import datetime


router_statistics = APIRouter(prefix="/statistics", tags=["Statistics"])

@router_statistics.post("/statistics/")
async def create_statistic(statistic: StatisticModel):
    success = await DBRepository.add_entity(statistic)
    if success:
        return {"message": "Statistic created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create statistic")

@router_statistics.get("/statistics/", response_model=List[StatisticModel])
async def read_all_statistics():
    statistics_list = await DBRepository.get_all_entity(StatisticModel)
    if statistics_list:
        return statistics_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve statistics")

@router_statistics.get("/statistics/{id}", response_model=list[StatisticModel])
async def read_statistic(id: int):
    statistic = await DBRepository.get_statistics(id)
    if statistic:
        return statistic
    else:
        raise HTTPException(status_code=404, detail="Statistic not found")

@router_statistics.put("/statistics/{id}")
async def update_statistic(id: int, statistic: StatisticModel):
    success = await DBRepository.update_entity(id, statistic)
    if success:
        return {"message": "Statistic updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update statistic")

@router_statistics.delete("/statistics/{id}")
async def delete_statistic(id: int):
    success = await DBRepository.delete_entity(id, StatisticModel)
    if success:
        return {"message": "Statistic deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete statistic")

@router_statistics.post("/workout_history/")
async def create_workout_history(workout_history: WorkoutHistoryModel):
    success = await DBRepository.add_entity(workout_history)
    if success:
        return {"message": "Workout history created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create workout history")

@router_statistics.get("/workout_history/", response_model=List[WorkoutHistoryModel])
async def read_all_workout_history():
    workout_history_list = await DBRepository.get_all_entity(WorkoutHistoryModel)
    if workout_history_list:
        return workout_history_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve workout history")

@router_statistics.get("/workout_history/{id}", response_model=list[WorkoutHistoryViewModel])
async def read_workout_history(id: int):
    workout_history = await DBRepository.get_workout_history_view(id)
    if workout_history:
        return workout_history
    else:
        raise HTTPException(status_code=404, detail="Workout history not found")

@router_statistics.put("/workout_history/{id}")
async def update_workout_history(id: int, workout_history: WorkoutHistoryModel):
    success = await DBRepository.update_entity(id, workout_history)
    if success:
        return {"message": "Workout history updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update workout history")

@router_statistics.delete("/workout_history/{id}")
async def delete_workout_history(id: int):
    success = await DBRepository.delete_entity(id, WorkoutHistoryModel)
    if success:
        return {"message": "Workout history deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete workout history")

@router_statistics.post("/nutrition/")
async def create_nutrition(nutrition: NutritionModel):
    success = await DBRepository.add_entity(nutrition)
    if success:
        return {"message": "Nutrition created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create nutrition")

@router_statistics.get("/nutrition/", response_model=List[NutritionModel])
async def read_all_nutrition():
    nutrition_list = await DBRepository.get_all_entity(NutritionModel)
    if nutrition_list:
        return nutrition_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve nutrition")