-- Таблица Личные данные
CREATE TABLE personal_data (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    gender VARCHAR(10) CHECK (gender IN ('Мужской', 'Женский')) NOT NULL,
    weight DECIMAL(5,2) NOT NULL,
    height DECIMAL(5,2) NOT NULL,
    fitness_level VARCHAR(50),
    goal VARCHAR(255)
);

-- Таблица Тренировки
CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    image_url VARCHAR(255),
);

-- Таблица Упражнения
CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    workout_id INT,
    name VARCHAR(255) NOT NULL,
    workout_text TEXT,
    workout_time_minutes INT,
    calories_burned INT,
    video_url VARCHAR(255),
    image_url VARCHAR(255),
    FOREIGN KEY (workout_id) REFERENCES workouts(id) ON DELETE CASCADE
);

-- Таблица Статистика
CREATE TABLE statistics (
    user_id INT,
    weight DECIMAL(5,2),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES personal_data(id) ON DELETE CASCADE
);

-- Таблица История тренировок
CREATE TABLE workout_history (
    user_id INT,
    workout_id INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES personal_data(id) ON DELETE CASCADE,
    FOREIGN KEY (workout_id) REFERENCES workouts(id) ON DELETE CASCADE
);

-- Таблица Питание
CREATE TABLE nutrition (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(255) NOT NULL,
    recipe_text TEXT,
    calories INT,
    protein DECIMAL(5,2),
    fat DECIMAL(5,2),
    carbohydrates DECIMAL(5,2)
    image_url VARCHAR(255),
);
