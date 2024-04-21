from rest_framework.exceptions import APIException


class CantFollowYourSelf(APIException):
    status_code = 403
    default_detail = "You can't follow yourself"
    default_code = "forbidden"
