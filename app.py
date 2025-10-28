from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str
    model: str = "xhosa"

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    if request.model == "xhosa":
        translations = {
            "hello": "Molo",
            "thank you": "Enkosi", 
            "how are you": "Unjani?",
            "good morning": "Molweni",
            "goodbye": "Sala kakuhle",
            "i love you": "Ndiyakuthanda",
            "please": "Ndicela",
            "yes": "Ewe",
            "no": "Hayi"
        }
    else:  # zulu
        translations = {
            "hello": "Sawubona",
            "thank you": "Ngiyabonga",
            "how are you": "Unjani?",
            "good morning": "Sawubona",
            "goodbye": "Hamba kahle",
            "i love you": "Ngiyakuthanda",
            "please": "Ngiyacela",
            "yes": "Yebo",
            "no": "Cha"
        }
    
    input_lower = request.text.lower()
    result = translations.get(input_lower, f"Translation for '{request.text}'")
    
    return {
        "success": True,
        "original_text": request.text,
        "translated_text": result,
        "model_used": request.model
    }

@app.get("/")
async def root():
    return {"message": "MetaWell AI API - LIVE", "status": "active"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
