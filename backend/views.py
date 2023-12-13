from django.shortcuts import render

from django.contrib.auth.models import User
from rest_auth.models import TokenModel
from django.contrib.auth import authenticate

from rest_framework import viewsets , status
from rest_framework.response import Response

from .serializers import AuthUserSerializer 

class UserViewSet(viewsets.ViewSet):
    print('serializer')
    queryset = User.objects.all()
    serializer = AuthUserSerializer
    def get_queryset(self):
        return User.objects.all()
    def create(self, request):
        serializer = AuthUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        
        serializer.save()
        return Response({"message": "User created successfully."})

    def list(self, request):
        users = self.get_queryset()
        serializer = AuthUserSerializer(users, many=True)
        return Response(serializer.data)



    def login(self, request):
        if request.method != "POST":
            return Response(
                {"message": "Invalid request method. Use POST for login."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )

        # Validate user ID and password presence
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"message": "Please provide both username and password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Authenticate user using Django's authenticate function
        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"message": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        token, created = TokenModel.objects.get_or_create(user=user)

        # Return response with authentication key
        return Response({"key": token.key})

from .models import Question
from .serializers import QuestionSerializer

class QuestionViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset
    # Define actions for different HTTP methods
    def list(self, request):
        # Get all questions
        questions = self.get_queryset()
        g = questions[0].solutions.all()
        print(g)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Create a new question
        try:
            user = User.objects.get(auth_token__key=request.META.get("HTTP_AUTHORIZATION"))
            request.data['created_by'] = user.username
            serializer = QuestionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Question created successfully."})
        except Exception as e :
            return Response({"message": "Question creation failed due Unauth."})

from .models import Solution
from .serializers import SolutionSerializer

class SolutionViewSet(viewsets.ViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    def get_queryset(self):
        queryset = Solution.objects.all()
        return queryset
    # Define actions for different HTTP methods
    def list(self, request):
        # Get all solutions
        solutions = self.get_queryset()
        serializer = SolutionSerializer(solutions, many=True)
        return Response(serializer.data)

    def create(self, request):
        # Create a new solution
        serializer = SolutionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Solution created successfully."})

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get_queryset(self):
        queryset = Profile.objects.all()
        return queryset
    
    def list(self, request):
        profiles = self.get_queryset()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def update(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Profile updated successfully."})