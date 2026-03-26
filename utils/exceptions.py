from rest_framework import status
from rest_framework.exceptions import APIException


class BusinessError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "business error"
    default_code = "business_error"


class NotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "not found"
    default_code = "not_found"
