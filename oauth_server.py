from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")

    print("\nAuthorization Code:\n")
    print(code)

    return {
        "message": "Authorization successful",
        "code": code
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)