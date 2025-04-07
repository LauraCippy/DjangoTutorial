from django.db import models

class Question(models.Model):
    domanda = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self): # Ritorna gli attributi del model come stringa
        return self.domanda, self.pub_date

class Choice(models.Model):
                        # Definisce la relazione(one-to-one) che c'è tra Choice e Question
    domanda = models.ForeignKey(Question, on_delete=models.CASCADE)
    scelta = models.CharField(max_length=200)
    voti = models.IntegerField(default=0)

    def __str__(self): # Ritorna gli attributi del model come stringa
        return self.domanda, self.scelta, self.voti
