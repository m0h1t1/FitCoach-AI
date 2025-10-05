from agent import generate_meal_plan

def main():
    prompt = input("What do you want your meal plan to include? ")
    result = generate_meal_plan(prompt)

    print("\nGenerated Meal Plan:\n")
    for meal in result["meals"]:
        print(f"{meal['name']}: {', '.join(meal['items'])}")
        print(f"   Macros: {meal['macros']}")
        print()

    print("Daily Total Macros:")
    print(result["totals"])

if __name__ == "__main__":
    main()
