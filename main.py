from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String, unique=True, index=True)
	hashed_password = Column(String)
Base.metadata.create_all(bind=engine)
app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
	hashed_password = pwd_context.hash(user.password)
	db_user = User(username=user.username, hashed_password=hashed_password)
	db.add(db_user)
	db.commit()
	return {"username": user.username}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	user = db.query(User).filter(User.username == form_data.username).first()
	if not user or not pwd_context.verify(form_data.password, user.hashed_password):
		raise HTTPException(status_code=400, detail="Incorrect username or password")
	return {"access_token": user.username, "token_type": "bearer"}