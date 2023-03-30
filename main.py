from fastapi import FastAPI, BackgroundTasks, HTTPException, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

templates = Jinja2Templates(directory='templates')

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/homepage")
async def demo_get():
    driver=createDriver()
    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit/")
async def submit(urls: str = Form(...)):
    driver=createDriver()
    driver.get(urls)
    return {driver.page_source}



# @app.post("/backgroundDemo")
# async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
#     background_tasks.add_task(doBackgroundTask, inp)
#     return {"message": "Success, background task started"}
    


