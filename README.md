# FitnessCoach AI

An AI-powered fitness coach that generates personalized nutrition meal plans and weightlifting workout programs.

## Features

- 🍎 **Nutrition Coach** - AI-powered meal planning with automatic macro tracking (calories, protein, carbs, fat)
- 💪 **Weightlifting Coach** - Weekly workout plans with exercises, sets, and reps
- 🤖 Powered by GPT-4o-mini for intelligent, personalized recommendations
- 🎨 Beautiful, modern UI with tab-based navigation
- 💻 React + TypeScript frontend
- 🚀 FastAPI backend

## Prerequisites

- Python 3.8+
- Node.js 16+
- OpenAI API key

## Setup Instructions

### 1. Backend Setup

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env

# Edit .env and add your actual API key
```

### 2. Get Your OpenAI API Key

1. Go to https://platform.openai.com/api-keys
2. Sign up/login and create a new API key
3. Add it to `backend/.env`:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

### 3. Frontend Setup

```bash
cd fitness-coach

# Install dependencies
npm install
```

## Running the Application

### Start Backend Server

```bash
cd backend
python api.py
```

The API will be available at http://localhost:8001

### Start Frontend

In a new terminal:

```bash
cd fitness-coach
npm start
```

The app will open at http://localhost:3000

## Usage

### Nutrition Coach

1. Open http://localhost:3000 in your browser
2. Select the **Nutrition** tab (🍎)
3. Enter your meal preferences (e.g., "I want a 2000 calorie meal plan with high protein, no dairy")
4. Click "Generate Plan"
5. View your personalized meal plan with complete macro breakdown

### Weightlifting Coach

1. Select the **Weightlifting** tab (💪)
2. Describe your workout goals (e.g., "I want a 4-day push/pull/legs split focusing on hypertrophy")
3. Click "Generate Plan"
4. View your weekly workout plan (Monday-Sunday) with exercises, sets, and reps

## CLI Mode (Optional)

You can also use the command-line interface for nutrition planning:

```bash
cd backend
python main.py
```

## Project Structure

```
FitnessCoachAI/
├── backend/
│   ├── agent.py          # AI agents for meal planning & workout generation
│   ├── api.py           # FastAPI server with nutrition & weightlifting endpoints
│   ├── main.py          # CLI interface
│   ├── requirements.txt  # Python dependencies
│   └── .env             # Environment variables (create this)
├── fitness-coach/
│   ├── src/
│   │   ├── App.tsx      # React frontend with tab navigation
│   │   ├── App.css      # Modern styling
│   │   └── index.css    # Global styles
│   └── package.json
└── README.md
```

## Example Requests

### Nutrition Examples:
- "2500 calorie meal plan for muscle gain with 180g protein"
- "Vegetarian meal plan with 1800 calories"
- "Keto diet plan with less than 50g carbs per day"

### Weightlifting Examples:
- "5-day body part split for advanced lifter"
- "3-day full body workout for beginners"
- "Push/pull/legs program with focus on strength, include rest days"

## Troubleshooting

**Module not found errors:**
- Run `pip install -r requirements.txt` in the backend directory

**API connection errors:**
- Verify backend is running on port 8001
- Check that your OpenAI API key is set in `backend/.env`

**CORS errors:**
- Ensure frontend is running on port 3000
- Backend CORS is configured for localhost:3000

**Button stays disabled:**
- Make sure you've typed text in the input box
- The button only enables when there's content to submit

## License

MIT
