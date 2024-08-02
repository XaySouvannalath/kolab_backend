import asyncio
import aiomysql

loop = asyncio.get_event_loop()
async def test_example():
    conn = await aiomysql.connect(
        host=db_config.host, 
        port=db_config.port,
        user=db_config.user, 
        password=db_config.password, 
        db='mariadb',
        loop=loop
    )

    cur = await conn.cursor()
    await cur.execute("SELECT * from agency")
    print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()

loop.run_until_complete(test_example())
