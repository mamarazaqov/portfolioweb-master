from django.shortcuts import render
from myfiles.models import *
# Create your views here.
def homes(malumot):
    if malumot.method=="POST":
        ism = malumot.POST.get('name')
        mail = malumot.POST.get('mail')
        subject = malumot.POST.get('subject')
        Message(name=ism,mail=mail,subject=subject).save()
    about = home.objects.all()
    turlar = homeT.objects.all()
    iabuout = abut.objects.all()
    iturlar = abus.objects.all()
    skillsrasm = skillrasm.objects.all()
    skillsdev = skills.objects.all()
    skildev = skill.objects.all()
    portfoliorsm = portfolio_rasm.objects.all()
    portfoliorsmm = portfoliorasm.objects.all()
    return render(malumot, 'index.html', {'about': about, 'turlar': turlar,'iabuout': iabuout, 'iturlar': iturlar, 'skillsrasm': skillsrasm,'skillsdev': skillsdev, 'skildev': skildev,
                                          'portfoliorsm': portfoliorsm, 'portfoliorsmm': portfoliorsmm})
def filter_index(malumot,turi):
    about = portfoliorasm.objects.get(tur_id=turi)
    turlar =portfolio_rasm.objects.all()
    return  render(malumot,'index.html',{'about': about, 'turlar': turlar})



