from fastapi import APIRouter, status, HTTPException, Query, Path, Depends
from fastapi.responses import JSONResponse
from typing import Optional,List
from sqlalchemy.orm import Session
from database.database import get_db
from models.students import StudentModel
from schemas import *
from auth.bearer import TokenBearer

router =  APIRouter(prefix="/api/v1",
                    tags=["crud in blog by Names"])


@router.get("/names",
            response_model=List[ResponseNamesSchema],
            status_code=status.HTTP_200_OK)
async def names_list(user : bool = Depends(TokenBearer()),
                     search : Optional[str] = Query(None, description = "searching names"),
                     db:Session = Depends(get_db)):
    # print("user_token",user.username)
    return db.query(StudentModel).all()


@router.post("/names", response_model=ResponseNamesSchema, status_code=status.HTTP_201_CREATED)
async def names_create(request:NamesSchema,
                       user :bool = Depends(TokenBearer()),
                       db:Session =Depends(get_db)):
    student_obj = StudentModel(name=request.name)
    db.add(student_obj)
    db.commit()
    db.refresh(student_obj)
    return student_obj


@router.get("/names/{item_id}",
            response_model=ResponseNamesSchema,
            status_code=status.HTTP_200_OK)
async def names_detail(user :bool = Depends(TokenBearer()),
                       item_id: int = Path(description="something cool"),
                       db:Session = Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    return student_obj

 


@router.put("/names/{item_id}",
            response_model=ResponseNamesSchema,
            status_code=status.HTTP_200_OK)
async def names_update(item_id: int, request:NamesSchema,
                       user : bool = Depends(TokenBearer()),
                       db:Session = Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    student_obj.name = request.name
    db.commit()
    db.refresh(student_obj)
    return student_obj


@router.delete("/names/{item_id}")
async def names_delete(item_id: int,
                       user :bool = Depends(TokenBearer()),
                       db:Session = Depends(get_db)):
    student_obj = db.query(StudentModel).filter(StudentModel.id == item_id).one_or_none()
    
    if not student_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="item not found")
    db.delete(student_obj)
    db.commit()
    return JSONResponse({"detail": "item removed successfully"},
                        status_code=status.HTTP_200_OK)

