from forms import PaymentForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import datetime
from dump.models import UserProfileDump, TransactionDetails
from website.utils import fee_calculate
from utils import verifyChecksum
from config import WORKING_KEY
from website.decorator import dump_session_check
from django.shortcuts import render_to_response
from django.template import RequestContext

@dump_session_check
def order_confirmation(request):
    dump_id = request.session.get('userprofiledump')
    dump = UserProfileDump.objects.get(id=dump_id)
    fee_dict=fee_calculate(dump)
    dump.fee = fee_dict['online_fee']
    dump.save()
    order = 'SL%s' % datetime.datetime.now().strftime("%y%m%d%H%M%S")
    form = PaymentForm(order_id=order, amount=fee_dict['online_fee'])
    return render_to_response('ccavenue/form.html', locals(), context_instance=RequestContext(request))


@csrf_exempt
@dump_session_check
def payment_status(request):
    merchant_id = request.POST.get('Merchant_Id')
    order_id = request.POST.get('Order_Id')
    tran_id = order_id.split('SL')[1]
    amt = request.POST.get('Amount')
    authdesc = request.POST.get('AuthDesc')
    checksum = request.POST.get('Checksum')
    checksum = verifyChecksum(merchant_id, order_id, amt, authdesc, checksum, WORKING_KEY)
    if checksum:
        dump_id = request.session.get('userprofiledump')
        dump = UserProfileDump.objects.get(id=dump_id)
        if authdesc == 'Y':
            dump.payment_status = 1
            dump.payment_mode = 'ONLINE'
            dump.status = 'A'
            dump.save()
        TransactionDetails.objects.create(user_profile=dump, amount=amt, transaction_no=tran_id,\
            date_of_transaction=datetime.date.today(), onl_response=authdesc)
    return HttpResponseRedirect('/job/activate/')     
        
