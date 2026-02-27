from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Fake database (for now)
chickens = [
    {"id": 1, "name": "Shada Murgi", "image": "chicken1.webp"},
    {"id": 2, "name": "Lal Murgi", "image": "chicken2.webp"},
    {"id": 3, "name": "Pookie Murgi", "image": "chicken3.jpg"},
    {"id": 4, "name": "Rainbow Murgi", "image": "chicken4.jpg"},
    {"id": 5, "name": "Gray Murgi", "image": "chicken5.jpg"},
    {"id": 6, "name": "Nigga Murgi", "image": "chicken6.jpg"} 
    
] 

@app.get("/", response_class=HTMLResponse) 
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})  

@app.get("/api/chickens") 
async def get_chickens():
    return chickens

@app.get("/api/chicken/{chicken_id}")
async def get_chicken(chicken_id: int): 
    for chicken in chickens:
        if chicken["id"] == chicken_id:
            return {
                "name": chicken["name"],
                "title":"What do you wanna eat?",
                "options": ["Biriani\n200tk", "Morog Pulao\n150tk", "Korma\n220tk", "Grill\n180tk"]
            }
    return {"error": "Not found"} 