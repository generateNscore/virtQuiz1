from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
# import jwt # Imported from pyjwt

from app.dependencies import get_db
from app.models import User
# from app.schemas import UserCreate
# from app.auth import password_helper
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from datetime import datetime, timedelta, timezone


router = APIRouter()

# @router.post("/register")
# def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
#
#     # 1. Check if username already exists in the database
#     existing_user = db.query(User).filter(User.username == user_in.username).first()
#     if existing_user:
#         # raise HTTPException(status_code=400, detail="Username already registered.")
#         return {"message": "400: Username already registered."}
#
#     # 2. Hash the password safely using pwdlib
#     hashed_password = password_helper.hash(user_in.password)
#
#     # 3. Create a new instance of the SQLAlchemy DBUser model
#     new_user = User(
#         username=user_in.username,
#         hashed_password=hashed_password,
#         role=user_in.role
#     )
#
#     # 4. Save to PostgreSQL database
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)  # Refresh to get the generated ID from PostgreSQL
#
#     return new_user
#
#
# @router.post("/login")
# def login_user(user_in: UserCreate, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == user_in.username).first()
#
#     if not user:
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#
#     # 3. Verify the password
#     is_valid = password_helper.verify(user_in.password, user.hashed_password)
#     if not is_valid:
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#
#     # 4. Generate JWT Token expiration time
#     expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#
#     # 5. Create payload data
#     payload = {
#         # "sub": user["username"],  # "sub" means subject
#         "sub": user.username,
#         "exp": expire
#     }
#
#     # 6. Encode the token
#     token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
#
#     # 7. Return standard OAuth2 token payload
#     return {"access_token": token, "token_type": "bearer"}
#
