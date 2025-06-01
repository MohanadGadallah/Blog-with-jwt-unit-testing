from fastapi import Depends, status, HTTPException
from blog.schemas import blog_schema
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from typing import List, Sequence
from sqlalchemy.orm import Session, selectinload, joinedload
from sqlalchemy import Result, Select, create_engine, Column, Integer, String, select
from typing import Tuple, Optional, Dict, Any
from blog.database.models.Blog_model import Blog
from blog.database.session import get_db
from blog.schemas import blog_user_shared


async def get_all(db: AsyncSession = Depends(get_db)) -> Sequence[Blog]:
    result = await db.execute(
        select(Blog).options(joinedload(Blog.creator))
    )
    blogs = result.scalars().all()
    return blogs


async def create(request: blog_schema.AddBlog, db: AsyncSession = Depends(get_db)) -> Blog:
    new_blog: Blog = Blog(
        title=request.title, body=request.body, user_id=request.userid)
    db.add(new_blog)
    try:
        await db.commit()
        await db.refresh(new_blog)
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    finally:
        db.close
    return new_blog


async def delete(id: int, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        blog_query = select(Blog).where(Blog.id == id)
        result = await db.execute(blog_query)
        blog = result.scalar_one_or_none()

        if not blog:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

        await db.delete(blog)
        await db.commit()

    return {"message": "Blog deleted successfully"}


async def update(request: blog_schema.Blog, id: int, db: AsyncSession = Depends(get_db)):
    result: Select[Tuple[Blog]] = select(Blog).where(Blog.id == id)
    query_result: Result[Tuple[Blog]] = await db.execute(result)
    blog: Blog | None = query_result.scalar_one_or_none()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

    # Update the blog attributes
    blog.title = request.title
    blog.body = request.body

    # Commit the changes
    await db.commit()

    return {"message": "Blog updated successfully"}


async def get_one(id: int, db: AsyncSession = Depends(get_db)) -> Any | blog_user_shared.ShowBlog | None:
    statement: Blog = select(Blog).options(
        joinedload(Blog.creator)).where(Blog.id == id)
    result = await db.execute(statement)
    blog: blog_user_shared.ShowBlog = result.scalar_one_or_none()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return blog
