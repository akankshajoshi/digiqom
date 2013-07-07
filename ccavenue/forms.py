from django import forms
from django.core.urlresolvers import reverse

from ccavenue import config
from ccavenue.utils import getchecksum

class PaymentForm(forms.Form):
    """
    Form with hidden fields required to be posted to CCAvenue Payment url.
    The form needs to be displayed on final Order Confirmation page before
    directing user to CCAvenue site for payment.
    The Buy or Payment button on Order Confirmation page should submit this
    form to direct user to CCAvenue for payment.
    """
    Merchant_Id = forms.CharField(widget=forms.HiddenInput())
    Order_Id = forms.CharField(widget=forms.HiddenInput())
    Amount = forms.CharField(widget=forms.HiddenInput())
    Redirect_Url = forms.CharField(widget=forms.HiddenInput())
    Checksum = forms.CharField(widget=forms.HiddenInput())
    billing_cust_email = forms.CharField(widget=forms.HiddenInput())
    
    def __init__(self, order_id, amount,
                 merchant_id=config.MERCHANT_ID,
                 customer_email=None,
                 return_url=config.RETURN_URL,
                 form_action=config.POST_TEST_URL,
                 working_key = config.WORKING_KEY,
                 button_value = "Proceed",
                 button_cssclass = None,
                 *args, **kwargs):
        """
        The form can be passed parameters while initializing the form.
        order_id - compulsary
        amount - compulsary
        merchant_id - optional, otherwise set as specified in config
        customer_email - optional, otherwise not passed to ccavenue
        return_url - optional, otherwise set as specified in config
        form_action - optional, otherwise set as specified in config
        working_key - optional, otherwise set as specified in config        
        button_value - the submit button value
        button_cssclass - any classes to be applied to the button
        """
        super(PaymentForm, self).__init__(*args, **kwargs)
        # Set Variable to be used in form rendering
        self.form_action = form_action
        self.button_value = button_value
        self.button_cssclass = button_cssclass
        return_url = "%s%s" % (config.DOMAIN, reverse(return_url))
        
        # Initialize form fields with required values
        self.fields['Merchant_Id'].initial = merchant_id
        self.fields['Order_Id'].initial = order_id
        self.fields['Amount'].initial = amount
        self.fields['Redirect_Url'].initial = return_url
        self.fields['Checksum'].initial = getchecksum(merchant_id, amount, order_id, return_url, working_key)
        if customer_email is not None:
            self.fields['billing_cust_email'].initial = customer_email
        else:
            del self.fields['billing_cust_email']

    