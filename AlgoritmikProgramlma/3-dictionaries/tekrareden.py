#stringteki tekrarli harf:
    
#tekrar et
def a(sl):
    sl_={}
    tekr=[]
    
    for harf in sl:
        if harf not in sl_:
            sl_[harf]=1 # o harf bir defa var
        else:
            tekr.append(harf)
    return tekr
        
        #o(n)de calisir ama donguyle cozersek o n^2 de cikabilir.