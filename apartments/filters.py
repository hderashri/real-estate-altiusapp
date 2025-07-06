import django_filters
from .models import Apartment

class ApartmentFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    bedrooms = django_filters.MultipleChoiceFilter(
        field_name='bedrooms',
        choices=[(1, '1'), (2, '2'), (3, '3')],
        conjoined=False
    )
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')

    class Meta:
        model = Apartment
        fields = ['min_price', 'max_price', 'bedrooms', 'location']
