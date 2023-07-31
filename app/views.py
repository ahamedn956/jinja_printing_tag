from django.shortcuts import render

# Create your views here.

def data(request):

    d={'name' : 'MADARA UCHIHA', 'name2': 'OBITO UCHIHA'}

    return render(request,'data.html',context=d)
 