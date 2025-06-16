import aiosqlite
import asyncio


async def remove_duplicates():
    async with aiosqlite.connect('db/cars_sql.db') as conn:
        await conn.execute('''
            DELETE FROM cars
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM cars
                GROUP BY car_number
            )
        ''')
        await conn.commit()
        print("Дубликаты по car_number удалены.")

asyncio.run(remove_duplicates())
