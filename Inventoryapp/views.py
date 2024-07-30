from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from Inventoryapp.models import Suppilerdb, Stocksdb, Purchasesdb, Salesdb


# Create your views here.
def indexfn(req):
    stocks = Stocksdb.objects.all()
    latestsales = Salesdb.objects.order_by('-id')[:3]
    recentpurchases = Purchasesdb.objects.order_by('-id')[:3]
    return render(req, "index.html",
                  {'stocks': stocks, 'latestsales': latestsales, 'recentpurchases': recentpurchases})


def addsupplierfn(req):
    return render(req, "add_supplier.html")


def savesupplierfn(req):
    if req.method == "POST":
        a = req.POST.get('sname')
        b = req.POST.get('smobileno')
        c = req.POST.get('semail')
        d = req.POST.get('saddress')
        e = req.POST.get('sGSTIN')
        obj = Suppilerdb(s_name=a, s_mobileno=b, s_email=c, s_address=d, s_gstin=e)
        obj.save()
        return redirect(addsupplierfn)


def viewsupplierfn(req):
    data = Suppilerdb.objects.all()
    return render(req, "view_suppliers.html", {'data': data})


def editsupplierfn(req, sid):
    data = Suppilerdb.objects.get(id=sid)
    return render(req, "edit_supplier.html", {'data': data})


def updatesupplierfn(req, sid):
    if req.method == 'POST':
        a = req.POST.get('sname')
        b = req.POST.get('smobileno')
        c = req.POST.get('semail')
        d = req.POST.get('saddress')
        e = req.POST.get('sGSTIN')
    Suppilerdb.objects.filter(id=sid).update(s_name=a, s_mobileno=b, s_email=c, s_address=d, s_gstin=e)
    return redirect(viewsupplierfn)


def deletesupplierfn(req, sid):
    x = Suppilerdb.objects.filter(id=sid)
    x.delete()
    return redirect(viewsupplierfn)


def addstocksfn(req):
    return render(req, "add_stock.html")


def savestocksfn(req):
    if req.method == "POST":
        a = req.POST.get('stname')
        b = req.POST.get('stquantity')

        obj = Stocksdb(stockname=a, quantity=b)
        obj.save()
        return redirect(addstocksfn)


def inventorylistfn(req):
    data = Stocksdb.objects.all()
    return render(req, "inventory_list.html", {'data': data})


def editstockfn(req, stid):
    data = Stocksdb.objects.get(id=stid)
    return render(req, "edit_stock.html", {'data': data})


def updatestockfn(req, stid):
    if req.method == 'POST':
        a = req.POST.get('stname')
        b = req.POST.get('stquantity')
    Stocksdb.objects.filter(id=stid).update(stockname=a, quantity=b)
    return redirect(inventorylistfn)


def deletestockfn(req, stid):
    x = Stocksdb.objects.filter(id=stid)
    x.delete()
    return redirect(inventorylistfn)


def selectsupplierfn(request):
    data = Suppilerdb.objects.all()
    return render(request, "selectsupplier.html", {'data': data})


def purchasestocksfn(request):
    data = Suppilerdb.objects.all()
    sdata = Stocksdb.objects.all()
    context = {
        'data': data,
        'sdata': sdata
    }
    return render(request, "purchase_stocks.html", context=context)


def purchase_success(request, stock_id):
    return render(request, 'purchase_success.html', {'stock_id': stock_id})

def savepurchasefn(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('suppliername')
        stock_id = request.POST.get('stock')
        stock_price = request.POST.get('stockprice')
        stock_quantity = request.POST.get('stockquantity')
        total_price = request.POST.get('totalprice')

        print("Supplier ID:", supplier_id)
        print("Stock ID:", stock_id)

        if not supplier_id.isdigit() or not stock_id.isdigit():
            return HttpResponse("Invalid supplier ID or stock ID.")

        try:

            supplier_id = int(supplier_id)
            stock_id = int(stock_id)

            supplier = get_object_or_404(Suppilerdb, pk=supplier_id)
            stock = get_object_or_404(Stocksdb, pk=stock_id)

            purchase = Purchasesdb.objects.create(
                suppliername=supplier.s_name,
                suppliermobileno=supplier.s_mobileno,
                suppliergstin=supplier.s_gstin,
                stock=stock,
                stockprice=stock_price,
                stockquantity=stock_quantity,
                totalprice=total_price
            )

            stock.quantity += int(stock_quantity)
            stock.save()

            return redirect('success_page_url')

        except (ValueError, Suppilerdb.DoesNotExist, Stocksdb.DoesNotExist) as e:
            # Handle errors
            return HttpResponse("Error occurred: " + str(e))
    else:

        suppliers = Suppilerdb.objects.all()
        stocks = Stocksdb.objects.all()
        return render(request, 'your_template.html', {'suppliers': suppliers, 'stocks': stocks})


def success_page_url(request):
    return render(request, 'successpage.html')


def purchasebill(req):
    return render(req, "purchasebill.html")


def salesfn(req):
    data = Stocksdb.objects.all()
    context = {
        'data': data
    }
    return render(req, "sales.html", context=context)


def savesalesfn(request):
    if request.method == 'POST':
        c_name = request.POST.get('cname')
        c_mobileno = request.POST.get('cmobileno')
        c_email = request.POST.get('cemail')
        c_address = request.POST.get('caddress')
        c_gstin = request.POST.get('cGSTIN')
        stock_id = request.POST.get('stock')
        stock_price = request.POST.get('stockprice')
        stock_quantity = request.POST.get('stockquantity')
        total_price = request.POST.get('totalprice')

        print("Stock ID:", stock_id)

        if not stock_id.isdigit():
            return HttpResponse("Invalid supplier ID or stock ID.")

        try:

            stock_id = int(stock_id)

            stock = get_object_or_404(Stocksdb, pk=stock_id)

            sale = Salesdb.objects.create(
                cname=c_name,
                cmobileno=c_mobileno,
                cemail=c_email,
                caddress=c_address,
                cgstin=c_gstin,
                stock=stock,
                stockprice=stock_price,
                stockquantity=stock_quantity,
                totalprice=total_price
            )

            stock.quantity -= int(stock_quantity)
            stock.save()

            return redirect('success_page_url')

        except (ValueError, Suppilerdb.DoesNotExist, Stocksdb.DoesNotExist) as e:

            return HttpResponse("Error occurred: " + str(e))
    else:

        stocks = Stocksdb.objects.all()
        return render(request, 'your_template.html', {'stocks': stocks})


def purchaselistfn(req):
    pdata = Purchasesdb.objects.order_by('-id').all()
    return render(req, "purchase_list.html", {'pdata': pdata})


def purchasebillfn(request, purchase_id):
    purchase = Purchasesdb.objects.get(pk=purchase_id)
    return render(request, 'purchasebill.html', {'purchase': purchase})


def saleslistfn(req):
    salesdata = Salesdb.objects.order_by('-id').all()
    return render(req, "sales_list.html", {'salesdata': salesdata})


def salesbillfn(request, sales_id):
    sales = Salesdb.objects.get(pk=sales_id)
    return render(request, 'salesbill.html', {'sales': sales})


def loginfn(req):
    return render(req, "login_page.html")


def adminloginfn(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        up = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=up)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = up
                return redirect(indexfn)
            else:
                return redirect(loginfn)
        else:
            return redirect(loginfn)


def adminlogoutfn(request):
    if 'username' in request.session:
        del request.session['username']
    if 'password' in request.session:
        del request.session['password']
    return redirect(loginfn)
