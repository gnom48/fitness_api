from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey, Column, Integer, String
from enum import Enum
from sqlalchemy import Column, Integer, String, Date, Enum, DECIMAL, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class BaseModelOrm(DeclarativeBase):
    ...

class PersonalDataOrm(BaseModelOrm):
    __tablename__ = 'personal_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    contact_info = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(7), nullable=False)
    weight = Column(DECIMAL(5, 2), nullable=False)
    height = Column(DECIMAL(5, 2), nullable=False)
    fitness_level = Column(String(50))
    goal = Column(DECIMAL(5, 2))

class WorkoutOrm(BaseModelOrm):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    image_url = Column(String(255))

class ExerciseOrm(BaseModelOrm):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True, autoincrement=True)
    workout_id = Column(Integer, ForeignKey(WorkoutOrm.id, ondelete='CASCADE'), nullable=False)
    name = Column(String(255), nullable=False)
    workout_text = Column(Text)
    workout_time = Column(Integer)
    workout_count = Column(Integer, default=0)
    calories_burned = Column(Integer)
    video_url = Column(String(255))
    image_url = Column(String(255))

class StatisticOrm(BaseModelOrm):
    __tablename__ = 'statistics'

    user_id = Column(Integer, ForeignKey(PersonalDataOrm.id, ondelete='CASCADE'), primary_key=True)
    weight = Column(DECIMAL(5, 2), nullable=False)
    timestamp = Column(DateTime, default=func.current_timestamp(), primary_key=True)

class WorkoutHistoryOrm(BaseModelOrm):
    __tablename__ = 'workout_history'

    user_id = Column(Integer, ForeignKey(PersonalDataOrm.id, ondelete='CASCADE'), primary_key=True)
    workout_id = Column(Integer, ForeignKey(WorkoutOrm.id, ondelete='CASCADE'), primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    workout_length = Column(Integer)
    
class WorkoutHistoryViewOrm(BaseModelOrm):
    __tablename__ = 'workout_history_view'

    user_id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, primary_key=True)
    workout_length = Column(Integer)
    calories = Column(Integer)
    image_url = Column(String(255))

class NutritionOrm(BaseModelOrm):
    __tablename__ = 'nutrition'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_name = Column(String(255), nullable=False)
    recipe_text = Column(String(255))
    calories = Column(Integer)
    protein = Column(DECIMAL(5, 2))
    fat = Column(DECIMAL(5, 2))
    carbohydrates = Column(DECIMAL(5, 2))
    image_url = Column(String(255))
