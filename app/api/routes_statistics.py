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

@router_statistics.get("/statistics/{id}", response_model=list[StatisticModel])
async def read_statistic(id: int):
    statistic = await DBRepository.get_statistics(id)
    if statistic:
        return statistic
    else:
        raise HTTPException(status_code=404, detail="Statistic not found")

@router_statistics.post("/workout_history/")
async def create_workout_history(workout_history: WorkoutHistoryModel):
    success = await DBRepository.add_entity(workout_history)
    if success:
        return {"message": "Workout history created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create workout history")

@router_statistics.get("/workout_history/{id}", response_model=List[WorkoutHistoryViewModel])
async def read_workout_history(id: int):
    workout_history = await DBRepository.get_workout_history_view(id)
    if workout_history:
        return workout_history
    else:
        raise HTTPException(status_code=404, detail="Workout history not found")

