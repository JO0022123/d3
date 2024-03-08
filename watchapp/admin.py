from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(student)

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'image', 'description')
admin.site.register(catagory,CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')
  search_fields=['name','category__name']
admin.site.register(Product,ProductAdmin)
class cardsAdmin(admin.ModelAdmin):
  list_display = ('name', 'vendor')
admin.site.register(product_cards,cardsAdmin)