from django.db import models

class Question(models.Model):
    domanda = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.domanda # Ritorna una STRINGA

class Choice(models.Model):
                        # Definisce la relazione(one-to-one) che c'è tra Choice e Question
    domanda = models.ForeignKey(Question, on_delete=models.CASCADE)
    scelta = models.CharField(max_length=200)
    voti = models.IntegerField(default=0)

    def __str__(self):
        return self.scelta # Ritorna una STRINGA
