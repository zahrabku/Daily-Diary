from django.shortcuts import render
import datetime
from .models import * 


def form(request):
    if request.method == "GET":
        diarys=diary.objects.all()
        diaryAll={"diary":diarys}
        return render(request, 'home.html',context=diaryAll)
    if request.method == "POST":
        dtext = request.POST.get('diary_text',"")
        date=datetime.datetime.now()
        A=diary.objects.create(diary_text=dtext, pub_date=date)
        diarys=diary.objects.all()
        diaryAll={"diary":diarys}
        return render(request,'home.html',context=diaryAll)
    if request.method == "DELETE" :
        pass
        