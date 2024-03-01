from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    day=datetime.datetime.now().weekday()
    time=datetime.datetime.now().time()
    return render(request,'schedule/index.html',{
        'day':day,
        'time':time}
        )
    