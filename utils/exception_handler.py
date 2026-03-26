from rest_framework import status
from rest_framework.views import exception_handler as drf_exception_handler


def custom_exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:
        return response

    errors = response.data
    message = "error"

    if isinstance(errors, dict):
        if "detail" in errors:
            message = str(errors["detail"])
        else:
            first_value = next(iter(errors.values()), None)
            if isinstance(first_value, list) and first_value:
                message = str(first_value[0])
            elif first_value is not None:
                message = str(first_value)
    elif isinstance(errors, list) and errors:
        message = str(errors[0])
    elif errors:
        message = str(errors)

    response.data = {
        "code": response.status_code,
        "message": message,
        "data": None,
        "errors": errors,
    }
    return response
