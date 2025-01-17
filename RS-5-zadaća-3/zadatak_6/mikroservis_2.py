from aiohttp import web
import asyncio

async def pozdrav_handler(request):
    await asyncio.sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})

app = web.Application()
app.router.add_get('/pozdrav', pozdrav_handler)

if __name__ == "__main__":
    web.run_app(app, port=8082)
