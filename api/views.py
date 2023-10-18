from django.contrib.auth.models import Group
from . import models
from rest_framework import viewsets, permissions, status, serializers as rest_framework_serializers,parsers
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    # permission_classes = [permissions.IsAdminUser]
    lookup_field="username"


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser]
    


class FilePrintViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows fileprint to be viewed or edited.
    """
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    queryset = models.FilePrint.objects.all()
    serializer_class = serializers.FilePrintSerializer
    permission_classes = [permissions.IsAdminUser]


class ContactForm(rest_framework_serializers.Serializer):
    # simple serializer for emails
    email = rest_framework_serializers.EmailField()
    message = rest_framework_serializers.CharField()


class SendEmail(APIView):
    # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)
    # this is where the drf-yasg gets invoked

    @swagger_auto_schema(request_body=ContactForm)
    def post(self, request):
        # serializer object
        serializer = ContactForm(data=request.data)
        # checking for errors
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response(data={"status": "OK", "message": "gege"},
                        status=status.HTTP_201_CREATED,)
