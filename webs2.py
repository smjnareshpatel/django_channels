from websocket import create_connection
url = "ws://127.0.0.1:8000/ws"
#ws = create_connection(f"ws://")
ws = create_connection(f"{url}")
print("Sending 'Hello, World'...")
ws.send("NEXT")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close() 