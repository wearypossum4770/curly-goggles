# ~ from django.http import HttpResponse
import json
from channels.handler import AsgiHandler
from channels import Group
from channels.sessions import channel_session
from urllib.parse import parse_qs
# ~ def http_consumer(message):
    # ~ # Make standard HTTP response - access ASGI path attribute directly
    # ~ response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # ~ # Encode that response into message format (ASGI)
    # ~ for chunk in AsgiHandler.encode_response(response):
        # ~ message.reply_channel.send(chunk)
# ~ def ws_message(message):
    # ~ # ASGI WebSocket packet-received and send-packet message types
    # ~ # both have a "text" key for their textual data.
    # ~ message.reply_channel.send({
        # ~ "text": message.content['text'],
    # ~ })
# Connected to websocket.connect


# Connected to websocket.connect
@channel_session
def ws_connect(message, room_name):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Parse the query string
    params = parse_qs(message.content["query_string"])
    if b"username" in params:
        # Set the username in the session
        message.channel_session["username"] = params[b"username"][0].decode("utf8")
        # Add the user to the room_name group
        Group("chat-%s" % room_name).add(message.reply_channel)
    else:
        # Close the connection.
        message.reply_channel.send({"close": True})

# Connected to websocket.receive
@channel_session
def ws_message(message, room_name):
    Group("chat-%s" % room_name).send({
        "text": json.dumps({
            "text": message["text"],
            "username": message.channel_session["username"],
        }),
    })

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message, room_name):
    Group("chat-%s" % room_name).discard(message.reply_channel)
