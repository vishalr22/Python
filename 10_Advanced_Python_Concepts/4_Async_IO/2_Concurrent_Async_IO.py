import asyncio
import requests


async def function1():
    # print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    return "func 1 returned"


async def function2():
    # print("func 2")
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram2.jpg", "wb").write(response.content)
    return "func 2 returned"


async def function3():
    # print("func 3")
    URL = "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("instagram3.ico", "wb").write(response.content)
    return "func 3 returned"


async def main():
    # This will run all 3 functions one by one
    print(await function1())
    print(await function2())
    print(await function3())

    # This will run concurrently
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print("Run Concurrently:", L)

asyncio.run(main())
