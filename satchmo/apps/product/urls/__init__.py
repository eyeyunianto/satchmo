from category import urlpatterns as catpatterns
from django.conf.urls.defaults import *
from livesettings import config_value
from products import urlpatterns as prodpatterns
import product
from signals_ahoy.signals import collect_urls

catbase = r'^' + config_value('PRODUCT','CATEGORY_SLUG') + '/'
prodbase = r'^' + config_value('PRODUCT','PRODUCT_SLUG') + '/'

urlpatterns = patterns('',
    (prodbase, include('product.urls.products')),
    (catbase, include('product.urls.category')),
)

collect_urls.send(product, section="__init__", patterns = urlpatterns)
