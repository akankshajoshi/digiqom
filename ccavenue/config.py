from django.contrib.sites.models import Site
# CCAvenue Post URL to which the form has to be posted
POST_URL = "https://www.ccavenue.com/shopzone/cc_details.jsp"

# CCAvenue Test Post URL to which the form has to be posted
POST_TEST_URL = "https://www.ccavenue.com/shopzone/cc_details.jsp"

# CCAvenue Merchant ID
MERCHANT_ID = "M_Firefly_17167"

# CCAVenue Working Key
WORKING_KEY = "p44918hdjb2pohvvq9"

# Return URL, to which user redirected after payment processing on CCAvenue.
# Needs to be url name, given in urls.py
RETURN_URL = "ccavenue_payment_status"

# Site Domain
#DOMAIN = "http://www.shine.com"
DOMAIN= Site.objects.get_current().domain

