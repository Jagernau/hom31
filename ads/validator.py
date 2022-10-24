from rest_framework import serializers

def check_not_publish(value: bool):
    if value:
        raise serializers.ValidationError("This field not be True")
