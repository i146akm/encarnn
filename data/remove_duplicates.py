import aiosqlite
import asyncio


# def remove_duplicates():
#     conn = sqlite3.connect('db/cars_sql.db')
#     conn.execute("""
#         DELETE FROM cars
#         WHERE rowid NOT IN (
#             SELECT MIN(rowid)
#             FROM cars
#             GROUP BY car_number
#         )
#     """)
#     conn.commit()
#     conn.close()


async def drop_table():
    async with aiosqlite.connect('db/cars_sql.db') as conn:
        await conn.execute("DROP TABLE IF EXISTS cars")
        await conn.commit()
        print("Таблица 'cars' удалена.")

asyncio.run(drop_table())
