from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Madflix_Bots")




# Developer 
# Don't try🥺
# Telegram Channel @
# Backup Channel @
# Developer @
