def cdec(num):
    dec = 0
    for n in range(0,len(num)):
        temp = int(num[n])
        pw=pow(2 , len(num)-n-1)
        dec = dec + temp*pow(2 , len(num)-n-1)
    return dec

def DecBin(decstr):
    decimal=""
    while(decstr>0):
        dec = int(decstr) % 2
        decimal = decimal + str(dec)
        decstr = int(decstr) /2
    decimal = str(decimal)
    temp = list(decimal)
    temp.reverse()
    decimal = ''.join(temp)
    return decimal

def leftshift(str , num):
    str = DecBin(str)
    i=0
    while(i<(64-len(str))):
        str = "0"+str
        i+=1
    for i in range(0,num):
        str = str+"0"
        str = str[1:]
    return cdec(str)

def adler32(adler ,str):
    BASE=65521
    s1 = adler & 0xffff
    s2 = (adler >> 16) & 0xffff
    Ord=()
    for i in range(0,len(str)):
        s1 = (s1 + ord(str[i])) % BASE
        s2 = (s2 + s1) % BASE
    left = leftshift(s2 , 16) + s1
    return leftshift(s2 , 16) + s1

def getchecksum(MerchantId, Amount, OrderId ,URL ,WorkingKey):
    pay_id = "%s|%s|%s|%s|%s" % (MerchantId, OrderId, Amount, URL, WorkingKey)
    adler = 1
    adler = adler32(adler,pay_id)
    return adler

def verifyChecksum(MerchantId,OrderId,Amount,AuthDesc,CheckSum,WorkingKey):
    pay_id = "%s|%s|%s|%s|%s" % (MerchantId, OrderId, Amount, AuthDesc, WorkingKey)
    adler = 1
    adler = adler32(adler,pay_id)
    if int(adler) == int(CheckSum):
        return True
    else:
        return False
