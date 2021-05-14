from django.http import HttpResponse,HttpRequest
from django.views.generic import TemplateView
from django.shortcuts import redirect,render
from django.urls import reverse
def index(request):
    return render(request,'index.html')


def en(request):
    return render(request,'en.html')

def de(request):
    return render(request,'de.html')

def cipher(request):
    htext = request.POST.get('text','default')
    hkey = request.POST.get('number','default')
    hidden=" "
    
    for i in range(len(htext)):
        key=int(hkey)
        char = htext[i]
        if(char==" "):
            continue 
        else:
            if (char.isupper()):
                hidden += chr((ord(char)+ key-65)%26 +65)

            
            else:
                hidden += chr((ord(char)+ key-97)%26 +97)



            
        
    params = {'Hidden_text':hidden}

    return render(request,'cipher.html',params)

def dicipher(request):
    htext = request.POST.get('text','default')
    hkey = request.POST.get('number','default')
    hidden=" "
    
    for i in range(len(htext)):
        key=int(hkey)
        char = htext[i]
        if(char==" "):
            continue 
        else:
            if (char.isupper()):
                hidden += chr((ord(char)- key-65)%26 +65)

                
            else:
                hidden += chr((ord(char)- key-97)%26 +97)



            
        
    params = {'Hidden_text':hidden}

    return render(request,'dicipher.html',params)
