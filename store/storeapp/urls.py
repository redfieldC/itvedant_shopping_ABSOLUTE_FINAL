from django.urls import path
from storeapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    #path('home',views.homepage),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('addition/<x>/<y>',views.addition),
    path('',views.home),
    path('pdetails/<pid>',views.product_details),
    path('about',views.about_page),
    path('cart',views.cart_page),
    path('contact',views.contact_page),
    path('placeorder',views.placeorder_page),
    path('catfilter/<catv>',views.cat_filter),
    path('pricerange',views.pricerange),
    path('sort',views.sort),
    path('cart/<prod_id>',views.addtocart),
    path('removecart/<cid>',views.remove_cart),
    path('changeqty/<cid>',views.changeqty),
    path('removeorder/<oid>',views.removeorder)

]

if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)