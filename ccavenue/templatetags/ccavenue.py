from django import template

register = template.Library()

@register.inclusion_tag('ccavenue/form.html')
def ccavenue_payment_form(form):
    """
    TemplateTag to render ccavenue payment form.
    Takes ccavenue.forms.PaymentForm instance as argument
    """
    return {'form':form}