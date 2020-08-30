from django.shortcuts import render,redirect
from app1.models import *
from django.contrib import messages
from django.core.mail import  send_mail
from E_mandi.settings import EMAIL_HOST_USER
from django.http import  HttpResponse

def ShowIndex(request):
    return render(request,"index.html")

def emandiprocess(request):
    return render(request,"emandi.html")

def admin_update(request):
    idno=request.GET.get("idno")
    res=AdminModel.objects.get(id=idno)
    return render(request, "admin_update.html")

def adminlogin(request):
     return render(request,"admin.html")
def admin_login_check(request):
    un = request.POST.get("contact")
    pas=request.POST.get("password")
    try:
        res=AdminModel.objects.get(password=pas,contact=un)
        request.session["user"]=res.id
        return render(request,"adminhome.html",{"data":res})
    except AdminModel.DoesNotExist:
        return render(request,"admin.html",{"error":"Invalid User"})

def adminhome(request):
    return render(request ,"adminhome.html")

def view_all_marchnat(request):
    result1=MerchantModel.objects.all()
    return render(request,"view_all_marchant.html",{"data":result1})

def delete_marchant(request):
    mid=request.GET.get("idno")
    MerchantModel.objects.filter(mid=mid).delete()

    return render(request,"adminhome.html",{"message":"Marchant Deleted Sucessfully"})

def admin_view_product(request):
    result=ProductModel.objects.all()
    return render(request,"Admin_view_product.html",{"data":result})

def view_all_farmer(request):
    result=FormarModel.objects.all()
    return render(request,"view_all_farmer.html",{"data1":result})

def delete_farmer(request):
    fid=request.GET.get("idno")
    FormarModel.objects.filter(fid=fid).delete()
    messages.success(request,"Farmer Deleted")
    return render(request,"adminhome.html",{"message":"Farmer Deleted Sucessfully"})

def farmer_registration(request):
    return render(request,"Former_regstration.html")

def save_farmer(request):
   na=request.POST.get("t1")
   cn=request.POST.get("t2")
   em=request.POST.get("t3")
   ph=request.FILES["t4"]
   date=request.POST.get("t5")
   pas=request.POST.get("t6")
   res=FormarModel(name=na ,contact=cn,email=em,date_of_register=date,photo=ph,password=pas).save()
   messages.success(request, "Former  Registerd Successfully")
   return render(request,"Former_regstration.html")

def farmer_login(request):
    return render(request,"farmerlogin.html")

def farmer_login_check(request):
    cn = request.POST.get("t1")
    up = request.POST.get("t2")
    try:
        res = FormarModel.objects.get(contact=cn,password=up)
        request.session["user"]=res.fid
        return render(request, "farmer_details.html",{"data":res})
    except FormarModel.DoesNotExist:
        return render(request, "farmerlogin.html", {"error": "Invalid User"})

def add_product(request):
    return render(request, "add_product.html")

def save_product(request):
    pn=request.POST.get("p1")
    pr=request.POST.get("p2")
    pq=request.POST.get("p3")
    pp=request.FILES["p4"]
    pd=request.POST.get("p5")
    try:
     ProductModel(pname=pn,price=pr,quantity=pq,photo=pp,date_of_register=pd).save()
     return render(request,"add_product.html",{"message":"Product registerd Successfully"})
    except ProductModel.DoesNotExist:
        return render(request ,"add_product.html",{"message":"Product Already Registered"})


def viewall_product(request):
     result=ProductModel.objects.all()
     return  render(request,"Viewall_product.html",{"data":result})

def merchant_register(request):
    return render(request,"merchant.html")

def save_marchant(request):
   na=request.POST.get("t1")
   cn=request.POST.get("t2")
   em=request.POST.get("t3")
   ph=request.FILES["t4"]
   date=request.POST.get("t5")
   pas=request.POST.get("t6")
   gst=request.POST.get("t7")
   MerchantModel(name=na,contact=cn,email=em,photo=ph,date_of_register=date,password=pas,gst=gst).save()
   messages.success(request, "Marchant  Registerd Successfully")
   return redirect("main")


def marchantlogin(request):
    return render(request,"marchantlogin.html")

def marchant_login_check(request):
    cn = request.POST.get("t1")
    up = request.POST.get("t2")
    try:
        res = MerchantModel.objects.get(contact=cn,password=up)
        request.session["user"] = res.mid
        return render(request, "marchant_details.html",{"data":res})
    except MerchantModel.DoesNotExist:
        return render(request, "marchantlogin.html", {"error": "Invalid User"})



def new_license(request):
    return render(request,"new_License.html")

def save_license(request):
    na = request.POST.get("t1")
    cn = request.POST.get("t2")
    em = request.POST.get("t3")
    gst = request.POST.get("t4")
    firm=request.POST.get("t5")
    ph = request.FILES["t6"]
    status='Pending'
    Newlicence(name=na,contact=cn,email=em,gst=gst,firm=firm,photo=ph,status=status).save()
    return render(request,"new_License.html",{"message":"Data Save successfully"})


def viewPendingLic(request):
    result = Newlicence.objects.filter(status="Pending")
    print(result)
    return render(request, 'Pendin_lic.html', {"result": result,"key":"Pending"})

def viewAcceptedLic(request):
    result = Newlicence.objects.filter(status="Accepted")
    return render(request, 'Accept_app.html', {"result": result,"key":"Accepted"})

def viewRejectedLic(request):
    result = Newlicence.objects.filter(status="Rejected")
    return render(request, 'Reject.html', {"result": result, "key": "Rejected "})


def save_accept_app(request):
     lid=request.POST.get("lid")
     na=request.POST.get("t1")
     cn=request.POST.get("t2")
     gst=request.POST.get("t4")
     firm=request.POST.get("t5")
     Newlicence.objects.filter(lid=lid,name=na,contact=cn,gst=gst,firm=firm).save()
     return redirect("adminhome")

def reject_app(request):
    idno=request.GET.get("idno")
    Newlicence.objects.filter(lid=idno).delete()
    messages.success(request,"Application Rejected")
    return redirect("adminhome")

def price_list(request):
    return render(request,"price_list.html")

def contact_us(request):
    return render(request,"contactus.html")

def comlaint_feedback(request):
    return render(request, 'feedback.html')

def send_email(request):
    to=request.POST.get("t1")
    subject=request.POST.get("t2")
    message=request.POST.get("t3")
    send_mail(subject,message,EMAIL_HOST_USER,[to])
    return HttpResponse("Email Send")


def viewall_product1(request):
    result = ProductModel.objects.all()
    return render(request, "Viewall_product1.html", {"data": result})


def order_product(request):
    fid=request.POST.get("fid")
    mid=request.POST.get("mid")
    try:
        OrderModel.objects.get(Product=fid,Merchant=mid)
        return render(request,"viewall_product1.html",{"data":ProductModel.objects.all(),"message":"Product Ordered"})
    except OrderModel.DoesNotExist:
     OrderModel(Merchant_id=mid,Product_id=fid).save()
    return  redirect("view_order")

def view_order(request):
    return  render(request,"view_order.html",{"data":OrderModel.objects.filter(Merchant_id=request.session['user'])})


def view_application(request):
    result=Newlicence.objects.all()
    return render(request ,"view_application.html",{"data":result})

def admin_new_lic(request):
    id=request.POST.get("id")
    lid=request.POST.get("lid")
    try:
         result=viewlicense.objects.get(admin=id,newlicence=lid)
         return render(request,"view_application.html",
                       {"data": Newlicence.objects.all(),"message":"Licence Aproved"})
    except viewlicense.DoesNotExist:
         viewlicense(admin_id=id,newlicence_id=lid)
         return redirect("view_lic")


def view_lic(request):
    return render(request,"view_lic.html",{"data":viewlicense.objects.filter(admin_id=request.session["user"])})

     
