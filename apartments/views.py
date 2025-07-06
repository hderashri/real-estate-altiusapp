from django.shortcuts import render

from apartments.filters import ApartmentFilter
from apartments.models import Apartment


def apartment_list(request):
    apartments = Apartment.objects.all().order_by('-created_at')
    apartment_filter = ApartmentFilter(request.GET, queryset=apartments)

    sort_by = request.GET.get('sort')
    if sort_by:
        apartments = apartment_filter.qs.order_by(sort_by)
    else:
        apartments = apartment_filter.qs

    # Fix: Get selected bedrooms for template
    selected_bedrooms = request.GET.getlist('bedrooms')

    context = {
        'filter': apartment_filter,
        'apartments': apartments,
        'selected_bedrooms': selected_bedrooms,
        'request': request,  # optional if you still need request.GET for other fields
    }
    return render(request, 'apartments/apartment_list.html', context)
