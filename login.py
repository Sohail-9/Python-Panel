from fastapi import FastAPI, Request, Form

app = FastAPI()

@app.post("/login")
async def login(request: Request, username: Form(None), password: Form(None)):
    # Implement your login logic here, e.g., check credentials against a database
    if username == "admin" and password == "admin":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}