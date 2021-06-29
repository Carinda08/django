from inspect import GEN_RUNNING
from .models import BookInfo
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

class BookInfoModelSerializerR(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'

#0 all books:GET 
class BookInfoModelViewset(ModelViewSet):
    serializer_class = BookInfoModelSerializerR
    queryset = BookInfo.objects.all()


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label="id", read_only=True)
    title = serializers.CharField(max_length=20, label="Name")
    date = serializers.DateField(label="Date")
    readCnt = serializers.IntegerField(default=0, label="TotalRead")
    cmntCnt = serializers.IntegerField(default=0, label="TotalComment")
    is_del = serializers.BooleanField(default=0, label="isDel")

class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICE = (
        (0, 'female'),
        (1, 'male')
    )
    id =serializers.IntegerField(label='id', read_only=True)
    name = serializers.CharField(label='Name', max_length=20)
    gender = serializers.ChoiceField(choices=GENDER_CHOICE, label="Gender")
    cmnt = serializers.CharField(label='Information', max_length=20, required=False, allow_null=True)
    book = serializers.StringRelatedField(read_only=True)
