from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from config.exceptions import BusinessRuleError


def custom_exception_handler(exc, context):
    print(type(exc))
    response = exception_handler(exc, context)


    if isinstance(exc, ValidationError):
        return Response(
            {
                "error": "Validation Error",
                "fields": exc.detail
            },
            status=status.HTTP_400_BAD_REQUEST
        )  

    if isinstance(exc, BusinessRuleError):
        return Response(
            {"error": str(exc)},
            status=status.HTTP_400_BAD_REQUEST
        )
        
    if response is not None:
        return Response(
            {
                "error": response.data,
            },
            status=response.status_code
        )
                
    return Response(
        {"error": "Internal Server Error"}, 
        status=status.HTTP_500_INTERNAL_SERVER_ERROR 
    )