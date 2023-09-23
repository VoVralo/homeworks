import asyncio

from sqlalchemy import insert, select, update, delete

from models import User, Order
from database import async_session_maker


async def create_user(
        name: str,
        login: str,
        password: str,
        notes: str = '',
        is_conflict: bool = False,
):
    async with async_session_maker() as session:
        query = insert(User).values(
            name=name,
            login=login,
            password=password,
            notes=notes,
            is_conflict=is_conflict,
        )
        await session.execute(query)
        await session.commit()


async def create_order(
        pizza_quantity: int,
        pizza_price: float,
        customer: int,
        notes: '',
):
    async with async_session_maker() as session:
        query = insert(Order).values(
            pizza_quantity=pizza_quantity,
            pizza_price=pizza_price,
            customer=customer,
            notes=notes,
        )
        await session.execute(query)
        await session.commit()


async def fetch_users(skip: int = 0, limit: int = 10):
    async with async_session_maker as session:
        query = select(User).offset(skip).limit(limit)
        result = await session.execute(query)
        print(result.all())
        return result


async def update_user(user_id: int):
    async with async_session_maker as session:
        query = update(User).where(User.id == user_id).values(name='adsfsm')
        print(query)
        await session.execute(query)
        await session.commit()


async def delete_user(user_id: int):
    async with async_session_maker as session:
        query = delete(User).where(User.id == user_id)
        print(query)
        await session.execute(query)
        await session.commit()


async def main():
    await asyncio.gather(
        create_order(
            pizza_quantity=2,
            pizza_price=100.50,
            customer=2,
            notes='notes',
        )
    )

    # await asyncio.gather(update_user(2))
    # await asyncio.gather(delete_user(2))


asyncio.run(main())
