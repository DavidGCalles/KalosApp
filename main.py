from fastapi import FastAPI

app = FastAPI()
@app.get("/", status_code=403)
async def root():
	return {"message": "No hay nada que ver aqui"}