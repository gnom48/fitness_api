from fastapi import APIRouter, HTTPException, Header, Request
from .models import *
from ..repository import *
from datetime import datetime


router_workout = APIRouter(prefix="/workout", tags=["Workout"])

@router_workout.get("/workouts/", response_model=List[WorkoutModel])
async def read_all_workouts():
    workouts_list = await DBRepository.get_all_entity(WorkoutModel)
    if workouts_list:
        return workouts_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve workouts")

@router_workout.get("/workouts/{id}/exercises", response_model=List[ExerciseModel])
async def read_workout(id: int):
    exercises = await DBRepository.get_exercises_in_workout(id)
    if exercises:
        return exercises
    else:
        raise HTTPException(status_code=404, detail="Workout or exercises not found")
