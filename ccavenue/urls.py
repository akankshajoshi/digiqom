from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ccavenue.views',
    url(r'^confirm/$', 'order_confirmation', name='ccavenue_order_confirmation'),
    url(r'^status/$', 'payment_status', name='ccavenue_payment_status'))