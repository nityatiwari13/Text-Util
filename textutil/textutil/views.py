from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #dc = {'name':'Nitya', 'age': 20}
    return render(request, 'index.html')

def analyze(request):
    txt = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    capital = request.GET.get('capital', 'off')
    removespace = request.GET.get('removespace', 'off')
    countchar = request.GET.get('countchar', 'off')
    punctuations = '''!()-[]{};:'"/\,.><?@#$%^&*_~`'''
    analyser = ""
    if (removepunc == 'on'):
        for char in txt: 
            if char not in punctuations:
                analyser = analyser + char
    if (capital == 'on'):
        for char in txt:
            if (len(analyser) == 0):
                analyser = analyser +  char.upper()
            else:
                analyser = analyser + char  
    if (removespace == 'on'):
        for char in txt:
            if(char != " "):
                analyser = analyser + char;
    if (countchar == 'on') :
        cnt = 0;
        for char in txt:
            if(char != " "):
                cnt = cnt + 1
        analyser = str(cnt)        

    param = {
        'analysed_text' : analyser
    }
    return render(request, 'analyze.html', param)