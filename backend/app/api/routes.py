from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlmodel import Session, select
from typing import List, Optional
import redis
from rq import Queue

from app.db.session import get_session
from app import models, schemas
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.config import settings
from app.jobs.tasks import handle_contact

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)) -> models.User:
    from jose import JWTError, jwt

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        user_id = int(payload.get("sub"))
    except Exception as e:
        raise credentials_exception from e
    user = session.get(models.User, user_id)
    if not user:
        raise credentials_exception
    return user


@router.post("/api/v1/auth/register", response_model=schemas.UserRead)
def register(user_in: schemas.UserCreate, session: Session = Depends(get_session)):
    if session.exec(select(models.User).where(models.User.email == user_in.email)).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user = models.User(email=user_in.email, hashed_password=get_password_hash(user_in.password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.post("/api/v1/auth/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = session.exec(select(models.User).where(models.User.email == form_data.username)).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(str(user.id))
    return schemas.Token(access_token=access_token)


@router.get("/api/v1/auth/me", response_model=schemas.UserRead)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


@router.post("/api/v1/contact", response_model=schemas.ContactRead, status_code=201)
def create_contact(contact: schemas.ContactCreate, session: Session = Depends(get_session)):
    db_contact = models.Contact.from_orm(contact)
    session.add(db_contact)
    session.commit()
    session.refresh(db_contact)
    q = Queue("default", connection=redis.from_url(settings.redis_url))
    q.enqueue(handle_contact, db_contact.id)
    return db_contact

@router.get("/api/v1/contact", response_model=List[schemas.ContactRead])
def list_contacts(current_user: models.User = Depends(get_current_user), session: Session = Depends(get_session)):
    return session.exec(select(models.Contact)).all()
@router.get("/api/v1/cases", response_model=List[schemas.CaseRead])
def list_cases(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None,
    sort: Optional[str] = None,
):
    query = select(models.Case)
    if search:
        query = query.where(models.Case.title.contains(search))
    if sort == "desc":
        query = query.order_by(models.Case.created_at.desc())
    else:
        query = query.order_by(models.Case.created_at)
    cases = session.exec(query.offset(skip).limit(limit)).all()
    return cases


@router.post("/api/v1/cases", response_model=schemas.CaseRead, status_code=201)
def create_case(case: schemas.CaseCreate, session: Session = Depends(get_session), current_user: models.User = Depends(get_current_user)):
    db_case = models.Case.from_orm(case)
    session.add(db_case)
    session.commit()
    session.refresh(db_case)
    return db_case


@router.get("/api/v1/cases/{case_id}", response_model=schemas.CaseRead)
def get_case(case_id: int, session: Session = Depends(get_session)):
    case = session.get(models.Case, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case


@router.put("/api/v1/cases/{case_id}", response_model=schemas.CaseRead)
def update_case(case_id: int, case_in: schemas.CaseCreate, session: Session = Depends(get_session), current_user: models.User = Depends(get_current_user)):
    case = session.get(models.Case, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    case.title = case_in.title
    case.description = case_in.description
    session.add(case)
    session.commit()
    session.refresh(case)
    return case


@router.delete("/api/v1/cases/{case_id}", status_code=204)
def delete_case(case_id: int, session: Session = Depends(get_session), current_user: models.User = Depends(get_current_user)):
    case = session.get(models.Case, case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    session.delete(case)
    session.commit()
    return None
