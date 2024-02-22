from pydantic import BaseModel, EmailStr, Field
import hashlib

from ...loaders.orm.Queries import Queries
from ...loaders.orm.ORMStatus import ORMStatus
from ...loaders.models.User import User as UserORMModel
from ...loaders.models.Token import Token
from ...loaders.Context import SessionMaker
from random import randint

class User(BaseModel):
    username: str = Field(min_length=5)
    
class UserLogin(User):
    password: str = Field(min_length=8)
    
class UserRequest(User):
    email: EmailStr # По хорошему надо валидировать путем отправки письма
    password: str = Field(min_length=8)

class UserResponse(User):
    message: str
    success: bool

class UserTokenResponse(UserResponse):
    token: int|None
    
status_mapping = {ORMStatus.OK: "Success", 
                  ORMStatus.Fail: "Failed to create user"}

def find_user(user: User):
    id = Queries(SessionMaker).find_user(user.username)
    if id is None:
        return UserResponse(username=user.username,
                            message="No user with that name",
                            success=False)
    
    return UserResponse(username=user.username,
                        message="Username already used",
                        success=True)
    
def get_id_by_username(user: User):
    return Queries(SessionMaker).find_user(user.username)


def add_user(user: UserRequest) -> UserResponse:
    model = UserORMModel(username=user.username,
                         email=user.email,
                         password=hashlib.md5(user.password.encode()).hexdigest())
    
    status = Queries(SessionMaker).add(model)
    return UserResponse(username=user.username,
                        message=status_mapping[status],
                        success=status==ORMStatus.OK)
    
def validate(id: int, token: int) -> bool:
    return Queries(SessionMaker).validate_token(user_id=id, token=token)
    
def login(user: UserRequest) -> UserResponse:
    id = Queries(SessionMaker).find_pass(username=user.username, 
                                         password=hashlib.md5(user.password.encode()).hexdigest())
    
    if id is None:
        return UserTokenResponse(username=user.username,
                            message="Wrong password",
                            success=False,
                            token=None)
        
    token = randint(1, 10_000) + id[0] # change later
    status = Queries(SessionMaker).add(Token(token=token, user_id=id[0]))
    
    if not status == ORMStatus.OK:
        return UserTokenResponse(username=user.username,
                                 message="Token failed to generate",
                                 success=False,
                                 token=None)
        
    return UserTokenResponse(username=user.username, 
                             message="Logged in", 
                             token=token, 
                             success=True)
        
