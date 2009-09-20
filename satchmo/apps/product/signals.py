"""Satchmo product signals

Signals:

 - `discount_validate`: Usage::
 
      discount_validate.send(sender=Discount, discount=self, cart=cart, 
      contact=contact, shipping_choices=shipping_choices, shipping=shipping, success=success)
      
      Listeners should modify the "success" dictionary to veto the discount validity.
      
 - `index_prerender`: Usage::

      index_prerender.send(Sender, request=request, context=ctx, object_list=somelist)
   
 - `satchmo_price_query`: Usage::
 
      satchmo_price_query.send(self, adjustment=PriceAdjustmentCalc) 

 - `satchmo_order_success`
"""

import django.dispatch

discount_validate = django.dispatch.Signal()
index_prerender = django.dispatch.Signal()
satchmo_price_query = django.dispatch.Signal()
subtype_order_success = django.dispatch.Signal()
