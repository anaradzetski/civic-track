from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

from .serializers import SignUpSerializer, SignInSerializer, MeSerializer

class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = (permissions.AllowAny,)

class SignInView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        email = serializer.validated_data.get("email")
        user = authenticate(username=username, password=password, email=email)
        if user is None:
            return Response({"error": "Invalid credentials"}, status=400)
        
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })

@extend_schema(
    summary="Retrieve, update, or delete the authenticated user",
    responses=MeSerializer,
    auth=[{"bearerAuth": []}],
)
class MeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
