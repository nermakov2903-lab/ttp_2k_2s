from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
async def read_root():
    return FileResponse("index.html")

# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
#
# app = FastAPI()
#
#
# @app.get("/", response_class=HTMLResponse)
# def read_root():
#     with open("index.html", encoding="utf-8") as f:
#         return f.read()



