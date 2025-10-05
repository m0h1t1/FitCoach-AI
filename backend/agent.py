from openai import OpenAI
import os
import json

def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_meal_plan(prompt: str):
    client = get_openai_client()
    system_prompt = """
    You are a nutrition and meal planning assistant. 
    Given a user request, create a structured meal plan with 3-5 meals.
    You should make sure to follow the user's request and restrictions strictly and do not vary from the request.
    For example, if the user requests a vegetarian meal plan, you should not include any meat in the meal plan.
    If the user requests a certain amount of calories or a certain macro, that amount should be strictly followed.
    Be sure to create a meal plan that is realistic and achievable, but do not deviate from the user's request.
    For each meal, include:
    - A meal name (e.g., "Breakfast", "Lunch", "Dinner", "Snack")
    - A list of food items with approximate serving sizes
    - Estimated macros for the entire meal (calories, protein in grams, carbs in grams, fat in grams)
    
    Use your knowledge to provide realistic macro estimates based on typical serving sizes.
    
    IMPORTANT: Output ONLY valid JSON in this exact format:
    {
        "meals": [
            {
                "name": "Breakfast",
                "items": ["2 eggs", "1 cup oatmeal", "1 banana"],
                "macros": {
                    "calories": 450,
                    "protein": 20,
                    "carbs": 65,
                    "fat": 12
                }
            },
            {
                "name": "Lunch",
                "items": ["6oz grilled chicken", "1 cup brown rice", "1 cup broccoli"],
                "macros": {
                    "calories": 520,
                    "protein": 45,
                    "carbs": 55,
                    "fat": 8
                }
            }
        ]
    }
    
    Make sure all macro values are numbers (not strings). Be accurate and helpful.
    """
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    plan = completion.choices[0].message.content
    meal_plan = json.loads(plan)

    total_macros = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    for meal in meal_plan["meals"]:
        for key in total_macros:
            total_macros[key] += meal["macros"][key]

    meal_plan["totals"] = total_macros
    return meal_plan

def generate_workout_plan(prompt: str):
    client = get_openai_client()
    system_prompt = """
    You are a professional weightlifting and fitness coach.
    Given a user request, create a structured weekly workout plan (Monday through Sunday).
    You should follow the user's specific requests and restrictions strictly.
    For example, if the user wants to focus on upper body, prioritize those exercises.
    If they mention specific goals (strength, hypertrophy, endurance), tailor the plan accordingly.
    
    For each day:
    - If it's a workout day, include:
      - The muscle group focus or workout type
      - A list of exercises with sets and reps (e.g., "Barbell Bench Press: 4 sets x 8-10 reps")
    - If it's a rest day, simply mark it as "Rest Day"
    
    IMPORTANT: Output ONLY valid JSON in this exact format:
    {
        "week": [
            {
                "day": "Monday",
                "type": "workout",
                "focus": "Push (Chest, Shoulders, Triceps)",
                "exercises": [
                    "Barbell Bench Press: 4 sets x 8-10 reps",
                    "Dumbbell Shoulder Press: 3 sets x 10-12 reps",
                    "Incline Dumbbell Press: 3 sets x 10-12 reps",
                    "Cable Tricep Pushdown: 3 sets x 12-15 reps",
                    "Lateral Raises: 3 sets x 12-15 reps"
                ]
            },
            {
                "day": "Tuesday",
                "type": "rest",
                "focus": "Rest Day",
                "exercises": []
            }
        ]
    }
    
    Make sure to provide realistic and effective workout programming. Include appropriate rest days.
    """
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    plan = completion.choices[0].message.content
    workout_plan = json.loads(plan)
    
    return workout_plan
