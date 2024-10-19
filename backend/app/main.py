import sys
import uvicorn
from fastapi import FastAPI
from routers import foods
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(foods.router)

# CORS origins
ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    # Add other origins as needed
]

#Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def get_message():
    return {"Message": "Hello from FastAPI. More power to you!"}

if __name__ == "__main__":
    print(f"By default reload state is False.")
    print("Available CLI argument: Reload state (True/False)")

    args = sys.argv[1:]
    reload = False

    if len(args) == 1:
        if args[0].lower() == 'true':
            reload = True
    print(f"Reload State: {reload}")

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=reload)