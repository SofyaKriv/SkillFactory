import asyncio
import os

import aiohttp
from aiohttp import web


WS_FILE = os.path.join(os.path.dirname(__file__), 'websocket.html')

NEWS = {
    '1': "Новость 1",
    '2': "Новость 2",
    '3': "Новость 3",
}


async def wshandler(request: web.Request):
    resp = web.WebSocketResponse()
    available = resp.can_prepare(request)
    if not available:
        with open(WS_FILE, "rb") as fp:
            return web.Response(body=fp.read(), content_type="text/html")

    await resp.prepare(request)

    await resp.send_str("Welcome!!!")

    try:
        print("Someone joined.")
        for ws in request.app["sockets"]:
            await ws.send_str("Someone joined")
        request.app["sockets"].append(resp)

        await news_draw(resp)

        async for msg in resp:
            if msg.type == web.WSMsgType.TEXT:
                for ws in request.app["sockets"]:
                    if ws is not resp:
                        await ws.send_str(msg.data)
            else:
                return resp
        await asyncio.sleep(3)
        return resp

    finally:
        request.app["sockets"].remove(resp)
        print("Someone disconnected.")
        for ws in request.app["sockets"]:
            await ws.send_str("Someone disconnected.")


async def news_draw(resp):
    while True:
        news = await news_data()
        for i in iter(news):
            await resp.send_str(news[i])
        await asyncio.sleep(5)


async def news_data():
    async with aiohttp.ClientSession() as session:
        url = 'http://localhost:8080/news'
        async with session.get(url) as ans:
            news = await ans.json()
    return news


async def checkconnect():
    while True:
        client_session = aiohttp.ClientSession(raise_for_status=True)
        resp = await client_session.get('http://localhost:8080', raise_for_status=False)
        async with resp:
            if resp.status == 200:
                print("ping!")
                await client_session.close()
        await asyncio.sleep(5)


async def on_startup(app):
    app.loop.create_task(checkconnect())
    pass


async def on_shutdown(app: web.Application):
    for ws in app["sockets"]:
        await ws.close()


async def handle(request):
    return web.json_response(NEWS)


async def post_file(request):
    data = await request.post()
    for i in iter(data):
        NEWS[i] = data[i]
    return web.Response(text='ok', content_type="text/html")


def init():
    app = web.Application()
    app["sockets"] = []
    app.on_startup.append(on_startup)
    app.add_routes(
        [
            web.get("/", wshandler),
            web.get("/news", handle),
            web.post("/post", post_file)
        ]
    )
    app.on_shutdown.append(on_shutdown)
    return app


web.run_app(init())




