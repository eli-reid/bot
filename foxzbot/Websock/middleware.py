from .WebSocketServer.WebSocketServer import WebSocketServer

websocketServer = WebSocketServer()

def StartWebsocketServer():
    websocketServer.run()