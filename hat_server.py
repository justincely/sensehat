from aiohttp import web

from sense_hat import SenseHat
sense = SenseHat()

async def handle_base(request):
    return web.json_response({"status":"pong"})

async def handle_environment_temp(request):
    data = {"temperature": str(sense.temperature)}
    return web.json_response(data)

async def handle_environment(request):
    data = {"humidity": str(sense.humidity),
            "temperature": str(sense.temperature),
            "pressure": str(sense.pressure)}
    return web.json_response(data)

async def handle_led(request):
    data = {"pixels": sense.get_pixels()}
    return web.json_response(data)

async def handle_imu(request):
    data = {"orientation": sense.get_orientation(),
            "north": sense.get_compass()}
    return web.json_response(data)

app = web.Application()
app.add_routes([web.get('/ping', handle_base),
                web.get('/environment', handle_environment),
                web.get('/environment/temperature', handle_environment_temp),
                web.get('/led', handle_led),
                web.get('/imu', handle_imu)])
web.run_app(app)
