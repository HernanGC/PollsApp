from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.question_text

    def get_pub_date(self):
        return self.pub_date.date()

    def get_id(self):
        return self.pk


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.id} - {self.choice_text} - {self.pk}'

    def get_question(self):
        return self.question

    def get_votes(self):
        return self.votes

    def get_question_date(self):
        return self.question.get_pub_date()

    def vote(self):
        self.votes += 1

