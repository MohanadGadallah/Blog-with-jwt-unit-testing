from fastapi import Depends, status, HTTPException
from blog.schemas import user_schema, blog_schema, blog_user_shared
from blog.hash_p import hashing
from blog.database.session import get_db
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy import create_engine, Column, Integer, String, select
from typing import Tuple, Optional, Dict, Any
from blog.database.models.Users_model import Users


async def create(request: user_schema.User, db: AsyncSession = Depends(get_db)) -> Users:
    new_user: Users = Users(
        name=request.name, email=request.email,
        password=hashing.create_hash(request.password))
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user)
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        await db.close()
    return new_user


async def get(id: int, db: AsyncSession = Depends(get_db)) -> Optional[Dict[str, str]]:
    # Query the database to get the user's name and email
    # statement = select(models.Users.name, models.Users.email).where(
    #     models.Users.id == id
    # )
    # result = await db.execute(statement)
    # user: Optional[schemas.ShowUserNameAndEmail] = result.scalar_one_or_none()
    user = await db.get(Users, id)
    # Raise an exception if the user is not found
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return user
