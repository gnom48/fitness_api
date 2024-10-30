from fastapi import APIRouter, HTTPException, Header, Request
from .models import *
from ..repository import *
from datetime import datetime


router_workout = APIRouter(prefix="/workout", tags=["Workout"])

@router_workout.post("/workouts/")
async def create_workout(workout: WorkoutModel):
    success = await DBRepository.add_entity(workout)
    if success:
        return {"message": "Workout created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create workout")

@router_workout.get("/workouts/", response_model=List[WorkoutModel])
async def read_all_workouts():
    workouts_list = await DBRepository.get_all_entity(WorkoutModel)
    if workouts_list:
        return workouts_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve workouts")

@router_workout.get("/workouts/{id}", response_model=WorkoutModel)
async def read_workout(id: int):
    workout = await DBRepository.get_entity_by_id(WorkoutModel, id)
    if workout:
        return workout
    else:
        raise HTTPException(status_code=404, detail="Workout not found")

@router_workout.put("/workouts/{id}")
async def update_workout(id: int, workout: WorkoutModel):
    success = await DBRepository.update_entity(id, workout)
    if success:
        return {"message": "Workout updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update workout")

@router_workout.delete("/workouts/{id}")
async def delete_workout(id: int):
    success = await DBRepository.delete_entity(id, WorkoutModel)
    if success:
        return {"message": "Workout deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete workout")

@router_workout.post("/exercises/")
async def create_exercise(exercise: ExerciseModel):
    success = await DBRepository.add_entity(exercise)
    if success:
        return {"message": "Exercise created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to create exercise")

@router_workout.get("/exercises/", response_model=List[ExerciseModel])
async def read_all_exercises():
    exercises_list = await DBRepository.get_all_entity(ExerciseModel)
    if exercises_list:
        return exercises_list
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve exercises")

@router_workout.get("/exercises/{id}", response_model=ExerciseModel)
async def read_exercise(id: int):
    exercise = await DBRepository.get_entity_by_id(ExerciseModel, id)
    if exercise:
        return exercise
    else:
        raise HTTPException(status_code=404, detail="Exercise not found")

@router_workout.put("/exercises/{id}")
async def update_exercise(id: int, exercise: ExerciseModel):
    success = await DBRepository.update_entity(id, exercise)
    if success:
        return {"message": "Exercise updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update exercise")

@router_workout.delete("/exercises/{id}")
async def delete_exercise(id: int):
    success = await DBRepository.delete_entity(id, ExerciseModel)
    if success:
        return {"message": "Exercise deleted successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to delete exercise")
