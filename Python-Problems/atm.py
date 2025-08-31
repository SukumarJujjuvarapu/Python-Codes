amt=5000
if amt<100:
    print('amount should be more than 100')
if amt>=2000:
    count2000=amt//2000
    print("2000"+" *",count2000,"=",count2000*2000)
    amt%=2000
if amt>=500:
    count500=amt//500
    print("500"+" *",count500,"=",count500*500)
    amt%=500
if amt>=200:
    count200=amt//200
    print("200"+" *",count200,"=",count200*200)
    amt%=200
if amt>=100:
    count100=amt//100
    print("100"+" *",count2000,"=",count100*100)
    amt%=100
