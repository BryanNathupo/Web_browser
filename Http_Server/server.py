from aiohttp import web
import aiohttp
from pathlib import Path
import json
import os

#defining asyncio methods
async def handle_index(request):
    file_path = Path(__file__).parent/"templates/index.html"
    if os.path.exists(file_path):
        try:
            with open(file_path,mode="r") as file_from_templates:
                new_file = file_from_templates.read()
            return web.Response(text=new_file, content_type='text/html')

        except FileNotFoundError as e:
            return web.Response(text="File is NOT Found", status=500)
    else:
        print("do not exist")

async def handle_register(request):
    register_file = Path(__file__).parent/"templates/register.html"
    if os.path.exists(register_file):
        try:
            with open(register_file, mode="r") as newFile_from_templates:
                newRegister_File = newFile_from_templates.read()
            return web.Response(text=newRegister_File, content_type="text/html")    
        except FileNotFoundError as e:
            return web.Response(text="File is Not Found", status=500)
        

async def handle_submit(request):

    submit_content = request.post()

    username = submit_content.get("username","").strip()
    email = submit_content.get("email", "").strip()
    try:
        with open(Path(__file__).parent/"db.txt") as db:
            db.write(f"{username} {email}\n")
    except FileNotFoundError as e:
        web.Response(text="db not found", status=404)

        

app = web.Application() #Creating the loader to load the files
app.add_routes([
    web.get("/", handle_index),
    web.get("/register", handle_register),
    web.post("/submit", handle_submit)
])
#app.router.add_static(
    #"/assets/",
    #path=Path("assets"),
    #name="assets"
#)


HOST = "localhost"
PORT = 9494

if __name__ == "__main__":
    web.run_app(app, host=HOST, port=PORT) #starting the server
    