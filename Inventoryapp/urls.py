from django.contrib import admin
from django.urls import path
from Inventoryapp import views

urlpatterns = [
    path('index/',views.indexfn,name="indexfn"),
    path('addsupplier/',views.addsupplierfn,name="addsupplierfn"),
    path('savesupplierfn/',views.savesupplierfn,name="savesupplierfn"),
    path('viewsupplier/',views.viewsupplierfn,name="viewsupplierfn"),
    path('editsupplierfn/<int:sid>/',views.editsupplierfn,name="editsupplierfn"),
    path('updatesupplierfn/<int:sid>/',views.updatesupplierfn,name="updatesupplierfn"),
    path('deletesupplierfn/<int:sid>/',views.deletesupplierfn,name="deletesupplierfn"),
    path('addstocks/',views.addstocksfn,name="addstocksfn"),
    path('inventorylist/',views.inventorylistfn,name="inventorylistfn"),
    path('savestockfn/',views.savestocksfn,name="savestocksfn"),
    path('editstockfn/<int:stid>/',views.editstockfn,name="editstockfn"),
    path('updatestockfn/<int:stid>/',views.updatestockfn,name="updatestockfn"),
    path('deletestockrfn/<int:stid>/',views.deletestockfn,name="deletestockfn"),
    path('selectsupplierfn/',views.selectsupplierfn,name="selectsupplierfn"),
    path('purchasestocksfn//',views.purchasestocksfn,name="purchasestocksfn"),
    path('savepurchasefn/', views.savepurchasefn, name='savepurchasefn'),
    path('purchase/success/<int:stock_id>/', views.purchase_success, name='purchase_success'),
    path('success_page_url/', views.success_page_url, name='success_page_url'),
    path('purchasebill/', views.purchasebill, name='purchasebill'),
    path('salesfn/', views.salesfn, name='salesfn'),
    path('savesalesfn/', views.savesalesfn, name='savesalesfn'),
    path('purchaselistfn/', views.purchaselistfn, name='purchaselistfn'),
    path('saleslistfn/', views.saleslistfn, name='saleslistfn'),
    path('loginfn/', views.loginfn, name='loginfn'),
    path('adminloginfn/', views.adminloginfn, name='adminloginfn'),
    path('adminlogoutfn/', views.adminlogoutfn, name='adminlogoutfn'),
    path('purchasebillfn/<int:purchase_id>', views.purchasebillfn, name='purchasebillfn'),
    path('salesbillfn/<int:sales_id>', views.salesbillfn, name='salesbillfn'),


]