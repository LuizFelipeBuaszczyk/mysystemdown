from rest_framework.exceptions import APIException

class BusinessRuleError(APIException):
    status_code = 400
    default_detail = "Businnes rule violated"
    default_code = "business_error"