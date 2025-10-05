import { useState } from "react";
import "./App.css";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

type CoachType = "nutrition" | "weightlifting";

function App() {
  const [activeTab, setActiveTab] = useState<CoachType>("nutrition");
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const API_URL = (process.env.REACT_APP_API_URL as string) || "http://localhost:8001";

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim()) return;
    
    setIsLoading(true);
    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, type: activeTab }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setResponse("Sorry, there was an error processing your request. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleTabChange = (tab: CoachType) => {
    setActiveTab(tab);
    setMessage("");
    setResponse("");
  };

  const placeholderText = activeTab === "nutrition" 
    ? "e.g., I want a 2000 calorie meal plan with high protein, no dairy..."
    : "e.g., I want a 4-day push/pull/legs split focusing on hypertrophy...";

  return (
    <div className="App">
      <div className="app-container">
        <header className="app-header">
          <h1 className="app-title">AI Fitness Coach</h1>
          <p className="app-subtitle">Your personalized nutrition and workout planning assistant</p>
        </header>
        
        <div className="tab-container">
          <button 
            className={`tab-button ${activeTab === "nutrition" ? "active" : ""}`}
            onClick={() => handleTabChange("nutrition")}
          >
            🍎 Nutrition
          </button>
          <button 
            className={`tab-button ${activeTab === "weightlifting" ? "active" : ""}`}
            onClick={() => handleTabChange("weightlifting")}
          >
            💪 Weightlifting
          </button>
        </div>

        <div className="content-card">
          <form onSubmit={handleSubmit} className="form-container">
            <textarea
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              rows={6}
              placeholder={placeholderText}
              className="textarea-input"
              disabled={isLoading}
            />
            <button 
              type="submit"
              className="submit-button"
              disabled={isLoading || !message.trim()}
            >
              {isLoading ? "Generating..." : "Generate Plan"}
            </button>
          </form>
          
          {isLoading && (
            <div className="loading-state">
              <p>Creating your personalized plan...</p>
            </div>
          )}
          
          {response && !isLoading && (
            <div className="response-container">
              <div className="response-content">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>{response}</ReactMarkdown>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
