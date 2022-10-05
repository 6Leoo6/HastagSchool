from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

templates = Jinja2Templates(directory='templates')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

# -------------------------------------HTML Templates-------------------------------------
@app.get('/')
def login(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

@app.get('/register')
def login(req: Request):
    return templates.TemplateResponse('register.html', {'request': req})


# --------------------------------------API Requests--------------------------------------
@app.get('/api/test')
def register(param: str):  
    return {'status': 200, 'error': param}



# To run the app: python -m uvicorn server:app --host 0.0.0.0 --reload