from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from pymongo import *
import os

from file_upload import *
from forms import *


####Static declerations ######

media_root = "/Users/vaibhavdesai/Documents/college/research/DAS/audit/media/"

def home(request):
    #the menu of all the operations

    return render(request,"index.html",{})


def SignUp(request,role):

    if role == "DO":
        url = 'dataOwner/DOsignup.html'
    if role == "User":
        url = 'User/UserSignUp.html'

    if request.method == 'POST':

        if role == "DO":
            form = DOSignUpForm(request.POST)
        if role == "User":
            form = UserSignUpForm(request.POST)

        if form.is_valid():
            db = Connection()["Research"][role]

            #To check if username is already taken.
            if db.find_one({"username":request.POST['username']}) != None:
                request.POST['username'] = ''
                return render(request, url, {'form': form,'UsernameError':True,'PasswordError':False})

            #To check the password match during the signup.
            if request.POST['pass1'] != request.POST['pass2']:
                return render(request, url , {'form': form,'PasswordError':True,'Usernameerror':False})

            data = {}
            for key,value in request.POST.items():
                data[key] = value

            db.insert(data)

            #Create a folder for the dataOwner when he sign's up
            if role == "DO":
                try:
                    os.makedirs(media_root+request.POST["username"])

                except:
                    print "[Error]",sys.exc_info()[0]

            return HttpResponseRedirect("/success")
    else:
        if role == "DO":
            form = DOSignUpForm()
            return render(request, url , {'form': form,'Usernameerror':False,'PasswordError':False})
        if role == "User":
            form = UserSignUpForm()
            return render(request, url , {'form': form,'Usernameerror':False,'PasswordError':False})

    
def SignIn(request,role):

    if role == "DO":
        url = "dataOwner/DSignIn.html"
    if role == "User":
        url = "User/USignIn.html"

    if request.method == 'POST':

        form = SignInForm(request.POST)
        if form.is_valid():

            db = Connection()["Research"][role]

            #To check if username is already taken.
            if db.find_one({"username":request.POST['username']}) == None or request.POST['password'] != db.find_one({"username":request.POST['username']})["pass1"]:
                request.POST['username'] = ''
                request.POST['password'] = ''
                return render(request, url, {'form': form,'error':True})

            return HttpResponseRedirect("/DOHome/"+request.POST["username"])
    else:
        form = SignInForm()
        return render(request, url , {'form': form,'error':False})


def DOHome(request,username):
    ##This is for the fileupload link

    return render(request,"dataOwner/DOHome.html",{'username':username})

def UploadFile(request,username):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FileUploadForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            #this is present in file_upload.py
            handle_uploaded_file(request.FILES['docfile'],username)
            return HttpResponseRedirect('/success/')
    else:
        form = FileUploadForm()

    return render(request, 'dataOwner/upload.html', {'form': form,'username':username})

def FileDetails(request,username):

    db = Connection()["Research"]["files"]

    file_details = []
    for item in db.find({"Owner":username}):
        file_details.append(item)

    return render(request,"dataOwner/fileDetails.html",{"details":file_details,"username":username})



    ###########   TPA Code###############

def TPASignIn(request):
    if request.method == "POST":
        form = TPA(request.POST)
        if form.is_valid():
            if request.POST['username'] == "audit" and request.POST['password'] == "pass":
                return render(request,"auditor/AHome.html",{})

            else:
                return render(request,"auditor/ALogin.html",{"error":True,"form":form})

    else:
        form = TPA()

    return render(request,"auditor/ALogin.html",{"error":False,"form":form})

def TPAHome(request):

    return render(request,"auditor/AHome.html",{})

def TPAListFiles(request):
    db = Connection()["Research"]["files"]

    return render(request,"auditor/listFiles.html",{"details":db.find()})

def TPAVerify(request,file_id):
    db = Connection()["Research"]["files"]
    db.update({'FileId':file_id},{'$set':{'verify': True}})
    print file_id
    print db.find()
    
    return render(request,"auditor/viewFile.html",{"file123":db.find_one({"FileId":file_id})})

def TPAVerified(request):
    db = Connection()["Research"]["files"]

    return render(request,"auditor/listFiles.html",{"details":db.find({"verify":True})})




