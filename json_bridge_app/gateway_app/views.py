import http
import logging
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from gateway_app.constants import CONSTANTS

logger = logging.getLogger(__name__)


def forward_to_websocket(data):
    async def send_to_websocket():
        channel_layer = get_channel_layer()
        await channel_layer.group_send(
            CONSTANTS["gateway_group_name"],
            {
                "type": "send_message",
                "data": data,
            }
        )
        logger.info('Translated the incoming http requests to the websocket.')

    async_to_sync(send_to_websocket)()


@csrf_exempt
def http_gateway(request):
    log_message = f'The incoming HTTP request is {request.method}.'
    logger.info(log_message)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            log_message = f'Received json data: {data}.'
            logger.info(log_message)

            forward_to_websocket(data)
            logger.info("Success HTTP request.")
            return JsonResponse({"message": data})

        except json.JSONDecodeError:
            log_message = f'{CONSTANTS["json_error"]}, status code:{http.HTTPStatus.BAD_REQUEST}'
            logger.error(log_message)
            return JsonResponse({"error": CONSTANTS["json_error"]}, status=http.HTTPStatus.BAD_REQUEST)
    else:
        log_message = f'{CONSTANTS["invalid_method"]}, status code:{http.HTTPStatus.METHOD_NOT_ALLOWED}'
        logger.warning(log_message)
        return JsonResponse({"message": CONSTANTS["invalid_method"]},
                            status=http.HTTPStatus.METHOD_NOT_ALLOWED)
