from django.urls import path, re_path

from .api_views import InterviewCreateView, QuestionDeleteView, AnswerDeleteView, InterviewListView, \
    InterviewUserListView, ResultUserCreateView

urlpatterns = [
    path('admin/interviews/', InterviewListView.as_view()),
    path('admin/interviews/post/', InterviewCreateView.as_view()),
    re_path('^admin/interviews/(?P<pk>.+)/$', InterviewCreateView.as_view()),
    path('admin/questions/', QuestionDeleteView.as_view()),
    re_path('^admin/questions/(?P<pk>.+)/$', QuestionDeleteView.as_view()),
    path('admin/answers/', AnswerDeleteView.as_view()),
    re_path('^admin/answers/(?P<pk>.+)/$', AnswerDeleteView.as_view()),
    path('user/interviews/', InterviewUserListView.as_view()),
    re_path('^user/interviews/(?P<pk>.+)/$', InterviewUserListView.as_view()),
    path('user/results/', ResultUserCreateView.as_view()),
    re_path('^user/results/(?P<pk>.+)/$', ResultUserCreateView.as_view()),
]