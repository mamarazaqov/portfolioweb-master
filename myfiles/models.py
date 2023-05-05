from django.db import models

# Create your models here.

class homeT(models.Model):
    NOMI = models.CharField(max_length=50)
    def __str__(self):
        return self.NOMI

class home(models.Model):
    nomi = models.ForeignKey(homeT,on_delete=models.CASCADE)
    tavsif = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='madia')
    vaqt = models.DateTimeField(auto_now=True)

class abut(models.Model):
    NOMI = models.CharField(max_length=50)
    def __str__(self):
        return self.NOMI

class abus(models.Model):
    nomi = models.ForeignKey(abut,on_delete=models.CASCADE)
    tavsif = models.CharField(max_length=50)
    tavsifs = models.CharField(max_length=50)
    rasm = models.ImageField(upload_to='madia')
    vaqt = models.DateTimeField(auto_now=True)


class skill(models.Model):
    NOMI = models.CharField(max_length=50)
    def __str__(self):
        return self.NOMI

class skillrasm(models.Model):
    rasm = models.ImageField(upload_to='madia')

class skills(models.Model):
    nomi = models.ForeignKey(skill,on_delete=models.CASCADE)
    tavsif = models.CharField(max_length=50)
    vaqt = models.DateTimeField(auto_now=True)

class portfolio_rasm(models.Model):
    NOMI = models.CharField(max_length=50)
    def __str__(self):
        return self.NOMI

class portfoliorasm(models.Model):
    nomi = models.ForeignKey(portfolio_rasm,on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='madia')
    vaqt = models.DateTimeField(auto_now=True)

class Message(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
