class TrainingPlan:
    def __init__(self, sport, skill_level, equipment, fitness_goal):
        self.sport = sport
        self.skill_level = skill_level
        self.equipment = equipment
        self.fitness_goal = fitness_goal

    def generate_plan(self):
        # Mock implementation for generating a training plan
        return f"Training plan for a {self.skill_level} {self.sport} athlete aiming for {self.fitness_goal}, using {self.equipment}."
