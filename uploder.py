
from Seller.models import Store, Brand, Brief, Product
from Administrator.models import Mincategory
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


products = [
    'imani',
    'rmmy',
    'mrosso'
]

store = Store.objects.get(slug = 'dummy')
seller = User.objects.get(username = 'cybergates')
brand = Brand.objects.get(slug = 'dummy')
category = Mincategory.objects.get(slug = 'imani')

upload = 0

for product in products:
    unique = get_random_string(length=25)
    brief = Brief.objects.create( seller = seller , store = store, brand = brand,  category=category , unique = unique)

    if brief:
       product = Product.objects.create( seller = seller, brief = brief, title = product )
       brief = Brief.objects.filter( unique = brief.unique ).update(url = product.slug )
       upload += 1
       print("Product Uploaded: ", upload)



