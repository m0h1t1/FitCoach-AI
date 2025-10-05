from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

from agent import generate_meal_plan, generate_workout_plan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    type: str = "nutrition"  # "nutrition" or "weightlifting"

class ChatResponse(BaseModel):
    response: str

@app.get("/")
def read_root():
    return {"message": "AI Nutrition Coach API"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        if request.type == "weightlifting":
            result = generate_workout_plan(request.message)
            
            # Format the workout plan as markdown
            response_text = "# Your Weekly Workout Plan\n\n"
            
            for day_plan in result["week"]:
                response_text += f"## {day_plan['day']}\n"
                response_text += f"**Focus:** {day_plan['focus']}\n\n"
                
                if day_plan['type'] == 'rest':
                    response_text += "*Rest Day - Recovery and regeneration*\n\n"
                else:
                    response_text += "**Exercises:**\n"
                    for exercise in day_plan['exercises']:
                        response_text += f"- {exercise}\n"
                    response_text += "\n"
            
            return ChatResponse(response=response_text)
        else:  # nutrition
            result = generate_meal_plan(request.message)
            
            # Format the response as markdown
            response_text = "# Your Personalized Meal Plan\n\n"
            
            for meal in result["meals"]:
                response_text += f"## {meal['name']}\n"
                response_text += f"**Items:** {', '.join(meal['items'])}\n\n"
                response_text += f"**Macros:**\n"
                response_text += f"- Calories: {meal['macros']['calories']:.1f}\n"
                response_text += f"- Protein: {meal['macros']['protein']:.1f}g\n"
                response_text += f"- Carbs: {meal['macros']['carbs']:.1f}g\n"
                response_text += f"- Fat: {meal['macros']['fat']:.1f}g\n\n"
            
            response_text += "---\n\n"
            response_text += "## Daily Total Macros\n"
            response_text += f"- **Calories:** {result['totals']['calories']:.1f}\n"
            response_text += f"- **Protein:** {result['totals']['protein']:.1f}g\n"
            response_text += f"- **Carbs:** {result['totals']['carbs']:.1f}g\n"
            response_text += f"- **Fat:** {result['totals']['fat']:.1f}g\n"
            
            return ChatResponse(response=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
