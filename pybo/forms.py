from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content'] # QuestionForm에서 사용 할 Question 모델의 속성
        labels = {
            'subject': '제 목',
            'content': '내 용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답 변 내 용',
        }