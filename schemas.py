from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    created_at: datetime.time
    username: str
    password: str


class ReadUsers(BaseModel):
    id: int
    created_at: datetime.time
    username: str
    password: str
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    id: int
    created_at: datetime.time
    title: str
    description: str
    status: str
    priority: str
    visibility: bool


class ReadTasks(BaseModel):
    id: int
    created_at: datetime.time
    title: str
    description: str
    status: str
    priority: str
    visibility: bool
    class Config:
        from_attributes = True


class Teams(BaseModel):
    id: int
    created_at: datetime.time
    Title: str
    created_by_user_id: int
    description: str


class ReadTeams(BaseModel):
    id: int
    created_at: datetime.time
    Title: str
    created_by_user_id: int
    description: str
    class Config:
        from_attributes = True


class TaskUsers(BaseModel):
    id: int
    task_id: int
    user_id: int


class ReadTaskUsers(BaseModel):
    id: int
    task_id: int
    user_id: int
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    created_at: str
    username: str
    password: str

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    title: str
    description: str
    status: str
    priority: str
    visibility: str

    class Config:
        from_attributes = True



class PutTasksId(BaseModel):
    id: str
    created_at: str
    title: str
    description: str
    status: str
    priority: str
    visibility: str

    class Config:
        from_attributes = True



class PostTeams(BaseModel):
    id: str
    created_at: str
    Title: str

    class Config:
        from_attributes = True



class PutTeamsId(BaseModel):
    id: str
    created_at: str
    Title: str

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True



class PostAssignUser(BaseModel):
    user_id: int
    task_id: int

    class Config:
        from_attributes = True



class DeleteUnassignUser(BaseModel):
    user_id: int
    task_id: int

    class Config:
        from_attributes = True

