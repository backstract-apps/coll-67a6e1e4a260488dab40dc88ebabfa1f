from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(db: Session = Depends(get_db)):
    try:
        return await service.get_tasks(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id')
async def get_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(raw_data: schemas.PostTasks, db: Session = Depends(get_db)):
    try:
        return await service.post_tasks(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(raw_data: schemas.PutTasksId, db: Session = Depends(get_db)):
    try:
        return await service.put_tasks_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id')
async def delete_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teams/')
async def get_teams(db: Session = Depends(get_db)):
    try:
        return await service.get_teams(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teams/id')
async def get_teams_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_teams_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/teams/')
async def post_teams(raw_data: schemas.PostTeams, db: Session = Depends(get_db)):
    try:
        return await service.post_teams(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/teams/id/')
async def put_teams_id(raw_data: schemas.PutTeamsId, db: Session = Depends(get_db)):
    try:
        return await service.put_teams_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/teams/id')
async def delete_teams_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_teams_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/assign/user')
async def post_assign_user(raw_data: schemas.PostAssignUser, db: Session = Depends(get_db)):
    try:
        return await service.post_assign_user(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/unassign/user')
async def delete_unassign_user(raw_data: schemas.DeleteUnassignUser, db: Session = Depends(get_db)):
    try:
        return await service.delete_unassign_user(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

