import asyncio, sys, os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import instagram_reel as instagram

async def do():
    url=input("URL: ")
    state, url, id = await instagram.check_url(url)
    if state:
        await instagram.download(url, id)
asyncio.run(do())
