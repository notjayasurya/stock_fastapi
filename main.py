from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
import models
from sqlalchemy.orm import Session
from database import SessionLocal,engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get('/')
def home(request: Request):
    ''' 
    Displays the stock screener on the dashboard/homescreen
    '''

    return templates.TemplateResponse("home.html",{"request":request,"somevar":2})

@app.post('/stock')
def create_stock():
    '''
    Created a stock and stores it in the create stock database.
    '''

    return{
        'code':'success',
        'message':'stocks are created',
    }