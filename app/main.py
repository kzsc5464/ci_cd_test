from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Cross Origin 막는용도 React 호환을 위해서
from routers import router_login

app = FastAPI()
app.include_router(router_login.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 특정 도메인을 지정하거나 모든 도메인을 허용하려면 "*" 사용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Test 1")

if __name__=="__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)