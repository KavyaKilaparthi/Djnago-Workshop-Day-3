from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def he(request):
	return HttpResponse("<h1>Welcome to Django Workshop</h1>")

def sam(request):
	return HttpResponse("<h2 style=color:white;background-color:red>Sample")

def dynamic(request,a,b):
	return HttpResponse("<h2><center>My roll no is:{} and my name is:{}</h2></center>".format(a,b))

def temp(request):
	return render(request,'temp.html',{})

def table(request):
	return render(request,'table.html',{})

def data(request,id,name):
	return render(request,'details.html',{'i':id,'n':name})

def inline(request):
	return render(request,'inline.html',{})

def internal(request):
	return render(request,'internal.html',{})

def external(request):
	if request.method=="POST":
		na=request.POST['uname']
		mb=request.POST['mbl']
		em=request.POST['email']
		ps=request.POST['psw']
		cps=request.POST['cpsw']
		#print(na)
		#print(mb)
		#print(em)
		#print(ps)
		#print(cps)
		return render(request,'data.html',{'n':na,'m':mb,'e':em,'p':ps,'c':cps})
	return render(request,'external.html',{})
def boot(request):
	return render(request,'boot.html',{})
def offline(request):
	return render(request,'offline.html',{})
