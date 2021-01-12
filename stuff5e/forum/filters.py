import django_filters

from django_filters import CharFilter, OrderingFilter
from .models import *

class SpellFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    o = OrderingFilter(
        fields = ('name', 'level', 'time', 'school', 'concentration', 'range')
    )
    
    class Meta:
        model = Spell
        
        fields = ['name', 'level', 'school', 'custom']
        
class FeatFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    o = OrderingFilter(
        fields = ('name', 'prerequisites', 'bonuses')
    )
    
    class Meta:
        model = Feat
        fields = ['name', 'custom']
        
class RaceFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    o = OrderingFilter(
        fields = ('name', 'bonuses', 'speed', 'size')
    )
    
    class Meta:
        model = Race
        fields = ['name', 'custom' , 'size']
        
class ClassFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    o = OrderingFilter(
        fields = ('name',)
    )
    
    class Meta:
        model = Class
        fields = ['name', 'custom' , 'spellcasting']