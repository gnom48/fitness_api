from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional

class PersonalDataModel(BaseModel):
    id: int
    full_name: str
    contact_info: str
    password: str
    birth_date: date
    gender: str
    weight: float
    height: float
    fitness_level: Optional[str] = None
    goal: Optional[float] = None

class WorkoutModel(BaseModel):
    id: int
    name: str
    image_url: Optional[str] = None

class ExerciseModel(BaseModel):
    id: int
    workout_id: int
    name: str
    workout_text: Optional[str] = None
    workout_time_minutes: Optional[int] = None
    workout_count: Optional[int]
    calories_burned: Optional[int] = None
    video_url: Optional[str] = None
    image_url: Optional[str] = None

class StatisticModel(BaseModel):
    user_id: int
    weight: float
    timestamp: datetime = Field(default_factory=datetime.now)

class WorkoutHistoryModel(BaseModel):
    user_id: int
    workout_id: int
    timestamp: datetime = Field(default_factory=datetime.now)
    workout_length: int

class WorkoutHistoryViewModel(BaseModel):
    user_id: int
    workout_id: int
    timestamp: datetime
    workout_length: int
    calories: Optional[int]
    image_url: Optional[str]
    workout_name: Optional[str]

class NutritionModel(BaseModel):
    id: int
    recipe_name: str
    recipe_text: str
    calories: Optional[int] = None
    protein: Optional[float] = None
    fat: Optional[float] = None
    carbohydrates: Optional[float] = None
    image_url: Optional[str]
