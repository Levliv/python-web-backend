import json
from urllib.parse import parse_qs
from answers import error_422, error_400, error_404, result_send
from counter import factorial, fibonacci, mean


async def factorial_route(scope, send):
    value = 0
    try:
        value = int(parse_qs(scope['query_string'].decode())['n'][0])
    except Exception:
        await error_422(send)
    if value < 0:
        await error_400(send)
    else:
        await result_send(send, factorial, value)


async def fibonacci_route(scope, send):
    value = 0
    try:
        value = int(scope['path'].split('/')[2])
    except Exception:
        await error_422(send)
    if value < 0:
        await error_400(send)
    else:
        await result_send(send, fibonacci, value)


async def mean_route(scope, receive, send):
    body = b""
    more_body = True

    while more_body:
        message = await receive()
        body += message.get("body", b"")
        more_body = message.get("more_body", False)
    try:
        values = json.loads(body)
    except Exception:
        await error_422(send)
        return
    if len(values) == 0:
        await error_400(send)
        return
    if not all([isinstance(value, float) or isinstance(value, int) for value in values]):
        await error_422(send)
        return
    await result_send(send, mean, 5)


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    processed = False
    if scope['method'] == 'GET':
        if scope['path'] == '/factorial':
            processed = True
            await factorial_route(scope, send)

        if scope['path'].split('/')[1] == 'fibonacci':
            processed = True
            await fibonacci_route(scope, send)

        if scope['path'] == '/mean':
            processed = True
            await mean_route(scope, receive, send)
    if not processed:
        await error_404(send)
