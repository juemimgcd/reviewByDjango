from typing import Any

from rest_framework import status
from rest_framework.response import Response


def success_response(
        *,
        message: str = "success",
        data: Any = None,
        status_code: int = status.HTTP_200_OK,
) -> Response:

    return Response(
        {
            "code": status_code,
            "message": message,
            "data": data,
        },
        status=status_code,
    )
