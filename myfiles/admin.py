from django.contrib import admin
from myfiles.models import *# Register your models here.

class Service(admin.ModelAdmin):
    list_display = ['id','nomi','tavsif','rasm']

admin.site.register(home,Service)

class SERVICE(admin.ModelAdmin):
    list_display = ['id','NOMI']

admin.site.register(homeT,SERVICE)

#__________________________________________________
class HOMEABUT(admin.ModelAdmin):
    list_display = ['id','nomi','tavsif','tavsifs','rasm']

admin.site.register(abus,HOMEABUT)

class HOMEANU(admin.ModelAdmin):
    list_display = ['id','NOMI']

admin.site.register(abut,HOMEANU)
#_________________________________________________
class SKILS(admin.ModelAdmin):
    list_display = ['id','nomi','tavsif']

admin.site.register(skills,SKILS)

class SKILSs(admin.ModelAdmin):
    list_display = ['id','rasm']

admin.site.register(skillrasm,SKILSs)

class SKILLS(admin.ModelAdmin):
    list_display = ['id','NOMI']

admin.site.register(skill,SKILLS)
#__________________________________________________
class portfoliorasmlar(admin.ModelAdmin):
    list_display = ['id','nomi','rasm']

admin.site.register(portfoliorasm,portfoliorasmlar)

class portfolio_rasmlar(admin.ModelAdmin):
    list_display = ['id','NOMI']

admin.site.register(portfolio_rasm,portfolio_rasmlar)

class adminM(admin.ModelAdmin):
    list_display = ['id','name','mail','subject','date']

admin.site.register(Message,adminM)
