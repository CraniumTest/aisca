from models.training_plan import TrainingPlan
from utils.data_loader import load_user_data, load_wearable_data

def main():
    user_data = load_user_data()
    wearable_data = load_wearable_data()

    # Initialize a training plan for the user
    plan = TrainingPlan(
        sport=user_data['sport'],
        skill_level=user_data['skill_level'],
        equipment=user_data['equipment'],
        fitness_goal=user_data['fitness_goal']
    )

    # Generate and print the training plan
    training_plan_details = plan.generate_plan()
    print(training_plan_details)

    # Display wearable data as a placeholder for performance tracking
    print("Performance Tracking Data:")
    print(f"Heart Rate: {wearable_data['heart_rate']} bpm")
    print(f"Speed: {wearable_data['speed']} m/s")
    print(f"Agility: {wearable_data['agility']}")

if __name__ == "__main__":
    main()
