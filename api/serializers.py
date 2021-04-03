from rest_framework import serializers
from student.models import Student

class ResultSerialiver(serializers.Serializer):
    board = serializers.CharField()
    roll = serializers.IntegerField()


class StudentRegiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"