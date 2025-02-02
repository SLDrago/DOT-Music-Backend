from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, EditUserSerializer
from .utils import password_reset_token
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .models import User

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT token for the new user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            user_data = {
                "name": user.name,
                "email": user.email,
                "access_token": access_token,
                "refresh_token": refresh_token,
            }

            return Response(
                {
                    "message": "User registered successfully",
                    "user": user_data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data


            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            return Response(
                {
                    "message": "Login successful",
                    "user": {
                        "email": user.email,
                        "name": user.name,
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUserView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = EditUserSerializer(instance=request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User profile updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RequestPasswordResetView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(str(user.pk).encode())

        reset_url = f"http://localhost:5173/reset-password/?uid={uid}&token={token}"

        # Render the email template with the reset URL
        email_subject = "Password Reset Request"
        email_message = render_to_string(
            'emails/password_reset_email.html',
            {'user': user, 'reset_url': reset_url}
        )

        send_mail(
            subject=email_subject,
            message=email_message,
            from_email="noreply@dotmusic.com",
            recipient_list=[user.email],
            html_message=email_message
        )

        return Response({"message": "Password reset email sent successfully."}, status=status.HTTP_200_OK)
    
class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        password = request.data.get('password')

        if not uid or not token or not password:
            return Response({"error": "UID, token, and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Decode the UID and get the user
            uid = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            return Response({"error": "Invalid token or user"}, status=status.HTTP_400_BAD_REQUEST)

        # Verify the token
        if not default_token_generator.check_token(user, token):
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)

        # Reset the password
        user.set_password(password)
        user.save()
        return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "gender": user.gender,
            "birthday": user.birthday
        }
        return Response(user_data, status=status.HTTP_200_OK)