from rest_framework.throttling import AnonRateThrottle


class AnonThrottle(AnonRateThrottle):
    rate = '3/minute'


class CustomAnonThrottle:
    throttle_classes = [AnonThrottle]
