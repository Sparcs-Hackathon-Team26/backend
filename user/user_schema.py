from pydantic import BaseModel, EmailStr, validator

from fastapi import HTTPException


class NewUserForm(BaseModel):
  name: str
  phone: str
  birth: str
  sex: str
  password: str

  @validator('name', 'phone', 'password', 'sex', 'birth')
  def check_empty(cls, v):
      if not v or v.isspace():
          raise HTTPException(status_code=422, detail="필수 항목을 입력해주세요.")
      return v

  @validator('phone')
  def check_phone(cls, v):
      phone = v
      if len(phone) != 11:
          raise HTTPException(status_code=422, detail="올바른 형식의 번호를 입력해주세요.")
      return phone

  @validator('password')
  def validate_password(cls, v):
      if len(v) < 8:
          raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요.")

      if not any(char.isdigit() for char in v):
          raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요.")

      if not any(char.isalpha() for char in v):
          raise HTTPException(status_code=422, detail="비밀번호는 8자리 이상 영문과 숫자를 포함하여 작성해 주세요.")

      return v
  

class Token(BaseModel):
    access_token: str
    token_type: str

class Current_User(BaseModel):
    user_name: str
    phone: str
    birth: str
    family_id: str
