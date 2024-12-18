def load_user_data():
    # Mocking user data - In real application, this might come from a database or API
    return {
        "name": "John Doe",
        "sport": "tennis",
        "skill_level": "intermediate",
        "equipment": ["racket", "shoes"],
        "fitness_goal": "endurance"
    }

def load_wearable_data():
    # Mocking data that might be pulled from a wearable device
    return {
        "heart_rate": 72,
        "speed": 5.0,  # in meters per second
        "agility": 3.5  # arbitrary units for demonstration
    }
