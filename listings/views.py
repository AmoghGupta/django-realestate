from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
import json
from django.core import serializers
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    listings = Listing.objects.all()

    # ----we can order by the data----
    # listings = Listing.objects.order_by('-list_date')
    
    # -----we can filter the data------
    # listings = Listing.objects.filter(is_published=True)

    #------we can do pagination for data-----
    # paginator = Paginator(listings,3)
    # page = request.GET.get('page')
    # page_listings = paginator.get_page(page)
    # context = {"listings":page_listings}

    context = {"listings":listings}
    return render(request, 'listings/listings.html',context)

    # data =  serializers.serialize('json',listings)
    # #dump = json.dumps(data)
    # return HttpResponse(data, content_type='application/json')

@login_required(login_url='login')
def listing(request, listing_id):
    print(listing_id)
    return render(request, 'listings/listing.html')


@login_required(login_url='login')
def search(request):
    return render(request, 'listings/search.html')



# Create your views here.
# def index(request):
#     return render(request, 'listings/listings.html', 
#         {
#             'name':'brad'
#         }
#     )