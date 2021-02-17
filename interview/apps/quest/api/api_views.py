from drf_rw_serializers.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from rest_framework.response import Response

from .serializers import InterviewSerializer, QuestionSerializer, AnswerSerializer, WriteInterviewSerializer, \
    WriteQuestionSerializer, WriteAnswerSerializer, WriteResultSerializer, ResultSerializer
from ..models import Interview, Question, AnswerOption, Result

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.utils import timezone


class InterviewListView(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class InterviewCreateView(RetrieveUpdateDestroyAPIView, ListCreateAPIView):
    queryset = Interview.objects.all()
    write_serializer_class = WriteInterviewSerializer
    read_serializer_class = InterviewSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class QuestionDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    write_serializer_class = WriteQuestionSerializer
    read_serializer_class = QuestionSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class AnswerDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = AnswerOption.objects.all()
    write_serializer_class = WriteAnswerSerializer
    read_serializer_class = AnswerSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class InterviewUserListView(generics.ListAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

    def get(self, request, *args, **kwargs):
        interviews = Interview.objects.filter(interview_end_date__gte = timezone.now())
        if 'pk' in kwargs:
            interviews = interviews.filter(id = kwargs['pk'])
            pass
        serializer = InterviewSerializer(interviews, many=True)
        if serializer.data == []:
            return Response({"Message": "Interview not found or currently unavailable."})
        return Response(serializer.data)


class ResultUserCreateView(ListCreateAPIView):
    queryset = Result.objects.all()
    write_serializer_class = WriteResultSerializer
    read_serializer_class = ResultSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            results = Result.objects.filter(user_id=kwargs['pk'])
        else:
            return Response({"Message": "Write user_id in URL 'user/results/***/'."})
        serializer = ResultSerializer(results, many=True)
        if serializer.data == []:
            return Response({"Message": "Results not found."})
        return Response(serializer.data)