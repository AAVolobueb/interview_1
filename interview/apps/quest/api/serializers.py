from rest_framework import serializers
from rest_framework.response import Response

from ..models import Interview, Question, AnswerOption, Result, ResultAnswer

from django.core.exceptions import ObjectDoesNotExist


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = AnswerOption
        fields = 'id', 'answer_text'


class QuestionSerializer(serializers.ModelSerializer):
    answeroption_set = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = 'id', 'question_text', 'answer_type', 'answeroption_set'


class InterviewSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Interview
        fields = [
            'id', 'interview_title', 'interview_description', 'interview_pub_date', 'interview_end_date', 'question_set'
        ]


class WriteAnswerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = AnswerOption
        fields = 'id', 'answer_text'


class WriteQuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    answeroption_set = AnswerSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Question
        fields = 'id', 'question_text', 'answer_type', 'answeroption_set'


class WriteInterviewSerializer(serializers.ModelSerializer):
    question_set = WriteQuestionSerializer(many=True, required=False)

    class Meta:
        model = Interview
        fields = [
            'id', 'interview_title', 'interview_description', 'interview_pub_date', 'interview_end_date', 'question_set'
        ]


    def create(self, validated_data):
        if 'id' in validated_data:
            validated_data.pop('id')
        if 'question_set' in validated_data:
            question_set_dict = validated_data.pop('question_set')
            interview = Interview.objects.create(**validated_data)
            for question_dict in question_set_dict:
                question_dict['interview'] = interview
                if 'id' in question_dict:
                    question_dict.pop('id')
                if 'answeroption_set' in question_dict:
                    answeroption_set_dict = question_dict.pop('answeroption_set')
                    question = Question.objects.create(**question_dict)
                    for answeroption_dict in answeroption_set_dict:
                        answeroption_dict['question'] = question
                        if 'id' in answeroption_dict:
                            answeroption_dict.pop('id')
                        AnswerOption.objects.create(**answeroption_dict)
                else:
                    Question.objects.create(**question_set_dict)
        else:
            interview = Interview.objects.create(**validated_data)
        return interview


    def update(self, instance, validated_data):
        if 'question_set' in validated_data:
            question_set_dict = validated_data.pop('question_set')
            try:
                interview = Interview.objects.get(pk=instance.pk)
                Interview.objects.filter(pk=instance.pk).update(**validated_data)
            except BaseException:
                return interview
            for question_dict in question_set_dict:
                question_dict['interview'] = interview
                if 'answeroption_set' in question_dict:
                    answeroption_set_dict = question_dict.pop('answeroption_set')
                    try:
                        question = Question.objects.get(id = question_dict['id'])
                        Question.objects.filter(id = question_dict['id']).update(**question_dict)
                    except BaseException:
                        if 'id' in question_dict:
                            question_dict.pop('id')
                        question = Question.objects.create(**question_dict)
                    for answeroption_dict in answeroption_set_dict:
                        answeroption_dict['question'] = question
                        try:
                            answer = AnswerOption.objects.get(id=answeroption_dict['id'])
                            AnswerOption.objects.filter(id=answeroption_dict['id']).update(**answeroption_dict)
                        except BaseException:
                            if 'id' in answeroption_dict:
                                answeroption_dict.pop('id')
                            AnswerOption.objects.create(**answeroption_dict)
                else:
                    try:
                        question = Question.objects.get(id=question_dict['id'])
                        Question.objects.filter(id=question_dict['id']).update(**question_dict)
                    except BaseException:
                        if 'id' in question_dict:
                            question_dict.pop('id')
                        Question.objects.create(**question_dict)
        else:
            try:
                interview = Interview.objects.get(pk=instance.pk)
                Interview.objects.filter(pk=instance.pk).update(**validated_data)
            except BaseException:
                pass
        return interview


class ResultAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultAnswer
        fields = 'id', 'result', 'question_number', 'answer'


class ResultSerializer(serializers.ModelSerializer):
    resultanswer_set = ResultAnswerSerializer(many=True)

    class Meta:
        model = Result
        fields = 'id', 'interview', 'user_id', 'interview_date', 'resultanswer_set'


class WriteResultAnswerSerializer(serializers.ModelSerializer):
    question_number = serializers.IntegerField()
    answer = serializers.CharField()

    class Meta:
        model = ResultAnswer
        fields = 'id', 'result', 'question_number', 'answer'


class WriteResultSerializer(serializers.ModelSerializer):
    interview = serializers.IntegerField()
    user_id = serializers.IntegerField()
    resultanswer_set = WriteResultAnswerSerializer(many=True)

    class Meta:
        model = Result
        fields = 'id', 'interview', 'user_id', 'interview_date', 'resultanswer_set'

    def create(self, validated_data):
        resultanswer_set_dict = validated_data.pop('resultanswer_set')
        validated_data['interview'] = Interview.objects.get(id=validated_data['interview'])
        result = Result.objects.create(**validated_data)
        for resultanswer_dict in resultanswer_set_dict:
            resultanswer_dict['result'] = result
            resultanswer_dict['question_number'] = Question.objects.get(id=resultanswer_dict['question_number'])
            ResultAnswer.objects.create(**resultanswer_dict)
        return result

