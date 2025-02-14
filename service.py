from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    username:str = raw_data.username
    password:str = raw_data.password


    
    from datetime import datetime

    try:
        # Get current timestamp
        timestamp:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'username': username, 'password': password, 'created_at': timestamp}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    user = new_users.to_dict()


    

    try:
        status = True if user else False
    except Exception as e:
        raise HTTPException(500, str(e))


    res = {
        'user': user,
        'status': status,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    username:str = raw_data.username
    password:str = raw_data.password


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'username': username, 'password': password}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record.to_dict() 

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def get_tasks(db: Session):

    tasks_all = db.query(models.Tasks).all()
    tasks_all = [new_data.to_dict() for new_data in tasks_all] if tasks_all else tasks_all

    res = {
        'tasks_all': tasks_all,
    }
    return res

async def get_tasks_id(db: Session, id: int):

    tasks_one = db.query(models.Tasks).filter(models.Tasks.id == id).first() 
    tasks_one = tasks_one.to_dict() if tasks_one else tasks_one

    res = {
        'tasks_one': tasks_one,
    }
    return res

async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    title:str = raw_data.title
    description:str = raw_data.description
    status:str = raw_data.status
    priority:str = raw_data.priority
    visibility:str = raw_data.visibility



    is_visiible: bool = False


    

    try:
        is_visible = visibility.lower() == "true" if visibility else False
    except Exception as e:
        raise HTTPException(500, str(e))



    
    from datetime import datetime

    try:
        # Get current timestamp
        timestamp:datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'title': title, 'description': description, 'status': status, 'priority': priority, 'visibility': is_visiible, 'created_at': timestamp}
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    task_created = new_tasks.to_dict()

    res = {
        'tasks_inserted_record': task_created,
    }
    return res

async def put_tasks_id(db: Session, raw_data: schemas.PutTasksId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    title:str = raw_data.title
    description:str = raw_data.description
    status:str = raw_data.status
    priority:str = raw_data.priority
    visibility:str = raw_data.visibility


    tasks_edited_record = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'title': title, 'description': description, 'status': status, 'priority': priority, 'visibility': visibility}.items():
          setattr(tasks_edited_record, key, value)
    db.commit()
    db.refresh(tasks_edited_record)
    tasks_edited_record = tasks_edited_record.to_dict() 

    res = {
        'tasks_edited_record': tasks_edited_record,
    }
    return res

async def delete_tasks_id(db: Session, id: int):

    tasks_deleted = None
    record_to_delete = db.query(models.Tasks).filter(models.Tasks.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete.to_dict() 

    res = {
        'tasks_deleted': tasks_deleted,
    }
    return res

async def get_teams(db: Session):

    teams_all = db.query(models.Teams).all()
    teams_all = [new_data.to_dict() for new_data in teams_all] if teams_all else teams_all

    res = {
        'teams_all': teams_all,
    }
    return res

async def get_teams_id(db: Session, id: int):

    teams_one = db.query(models.Teams).filter(models.Teams.id == id).first() 
    teams_one = teams_one.to_dict() if teams_one else teams_one

    res = {
        'teams_one': teams_one,
    }
    return res

async def post_teams(db: Session, raw_data: schemas.PostTeams):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    Title:str = raw_data.Title


    record_to_be_added = {'id': id, 'created_at': created_at, 'Title': Title}
    new_teams = models.Teams(**record_to_be_added)
    db.add(new_teams)
    db.commit()
    db.refresh(new_teams)
    teams_inserted_record = new_teams.to_dict()

    res = {
        'teams_inserted_record': teams_inserted_record,
    }
    return res

async def put_teams_id(db: Session, raw_data: schemas.PutTeamsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    Title:str = raw_data.Title


    teams_edited_record = db.query(models.Teams).filter(models.Teams.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'Title': Title}.items():
          setattr(teams_edited_record, key, value)
    db.commit()
    db.refresh(teams_edited_record)
    teams_edited_record = teams_edited_record.to_dict() 

    res = {
        'teams_edited_record': teams_edited_record,
    }
    return res

async def delete_teams_id(db: Session, id: int):

    teams_deleted = None
    record_to_delete = db.query(models.Teams).filter(models.Teams.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        teams_deleted = record_to_delete.to_dict() 

    res = {
        'teams_deleted': teams_deleted,
    }
    return res

async def post_login(db: Session, raw_data: schemas.PostLogin):
    username:str = raw_data.username
    password:str = raw_data.password


    user = db.query(models.Users).filter(models.Users.username == username).first() 
    user = user.to_dict() if user else user



    password_match: str = user['password']


    

    try:
        if  user and password == password_match:
            status = True
        else:
            status = False
    except Exception as e:
        raise HTTPException(500, str(e))




    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=3600000)).timestamp()),
        'data': user
    }

    token = jwt.encode(bs_jwt_payload, 'my_secret_key', algorithm='HS256')



    user_id: int = user['id']

    res = {
        'token': token,
        'status': status,
        'user_id': user_id,
    }
    return res

async def post_assign_user(db: Session, raw_data: schemas.PostAssignUser):
    user_id:int = raw_data.user_id
    task_id:int = raw_data.task_id


    record_to_be_added = {'task_id': task_id, 'user_id': user_id}
    new_task_users = models.TaskUsers(**record_to_be_added)
    db.add(new_task_users)
    db.commit()
    db.refresh(new_task_users)
    task_users = new_task_users.to_dict()

    res = {
        'task_users': task_users,
    }
    return res

async def delete_unassign_user(db: Session, raw_data: schemas.DeleteUnassignUser):
    user_id:int = raw_data.user_id
    task_id:int = raw_data.task_id

    res = {
    }
    return res

