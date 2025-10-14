import google.generativeai as genai
from app.config import get_settings
import asyncio
from typing import Dict, List

class GeminiService:
    def __init__(self):
        settings = get_settings()  # Get settings in __init__ to avoid caching
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel(settings.MODEL_NAME)
    
    async def generate_recommendation(
        self, 
        user_profile: Dict, 
        products: List,
        feedback_stats: Dict
    ) -> str:
        prompt = f"""
        Based on the user profile, available products, and feedback statistics, 
        generate personalized product recommendations.
        
        User Profile:
        {user_profile}
        
        Feedback Statistics:
        {feedback_stats}
        
        Available Products:
        {products}
        
        Format your response like this:
        
        🎯 TOP RECOMMENDATIONS
        
        1. [Product Name]
           ★ Key Features: [2-3 key features]
           ✨ Why It's Perfect: [1-2 sentences about why this matches the user]
           📊 Feedback Score: [Include if available in feedback stats]
        
        2. [Product Name]
           ★ Key Features: [2-3 key features]
           ✨ Why It's Perfect: [1-2 sentences about why this matches the user]
           📊 Feedback Score: [Include if available in feedback stats]
        
        3. [Product Name]
           ★ Key Features: [2-3 key features]
           ✨ Why It's Perfect: [1-2 sentences about why this matches the user]
           📊 Feedback Score: [Include if available in feedback stats]
        
        💡 PERSONALIZATION INSIGHTS
        • [2-3 bullet points about why these recommendations match the user profile]
        • [Include insights from feedback statistics]
        """
        
        try:
            loop = asyncio.get_event_loop()
            # Set a reasonable timeout for Gemini API calls (30 seconds)
            response = await asyncio.wait_for(
                loop.run_in_executor(
                    None, 
                    lambda: self.model.generate_content(prompt)
                ),
                timeout=30.0
            )
            
            return response.text
        except asyncio.TimeoutError:
            raise Exception("Gemini API request timed out after 30 seconds")
        except Exception as e:
            raise Exception(f"Error generating AI recommendation: {str(e)}")
