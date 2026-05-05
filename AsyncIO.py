# save time and download image fast in squence 
import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("func 1")

async def function2():
    await asyncio.sleep(1)
    
    print("func 2")

async def function3():
    await asyncio.sleep(3)
    
    print("fun 3")
    

async def main():
    # Here our function 1 is loacted that take time excuted ,here fun 2 take 1 second after 3 second brake in fun 1 run and give output  
    task = asyncio.create_task(function1())
    #await function1()
    await function2()
    await function3()



    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )


asyncio.run(main())
