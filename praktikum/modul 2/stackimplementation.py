from stack import *

def reverseWord(teks):
    s=Stack()
    hasil=""
    for i in range(len(teks)):
        push(s,teks[i])
    for i in range (len(teks)):
        hasil = hasil+ pop(s)
    return hasil

def konversbiner(bil):
    biner= Stack()
    hasil=""
    while bil>0:
        push(biner,bil%2)
        bil//=2
    while not (isEmpty(biner)):
        hasil=hasil+str(pop(biner))
    return hasil

def postfixEval(postfixExpr):
    s= Stack()
    result=0
    for i in postfixExpr:
        if i =="+":
            if (size(s)>2):
                if (peek(s)==" "):
                    pop(s)
                last=int(pop(s))
                if peek(s)==" ":
                    pop(s)
                result=pop(s)+i
                push(s,result)
            else:
                return("operand terlalu sedikit")
        elif i =="-":
            if (size(s)>2):
                if (peek(s)==" "):
                    pop(s)
                last=(pop(s))
                if peek(s)==" ":
                    pop(s)
                result=pop(s)-last
                push(s,result)
            else:
                return("operand terlalu sedikit")
        elif i =="*":
            if (size(s)>2):
                if (peek(s)==" "):
                    pop(s)
                last=(pop(s))
                if peek(s)==" ":
                    pop(s)
                result=pop(s)*last
                push(s,result)
            else:
                return("operand terlalu sedikit")
        #lif i =="/":
            if (size(s)>2):
                if (peek(s)==" "):
                    pop(s)
                elif peek(s)==0:
                    return("error pembagi nol")
                last=(pop(s))
                if peek(s)==" ":
                    pop(s)
                result=pop(s)/last
                push(s,result)
            else:
                return("operand terlalu sedikit")
        elif i ==" ":
            push(s,i)
        else:
            if not(isEmpty(s)):
                if (peek(s)!=" "):
                    sum=(pop(s)*10)+(i)
                    push(s,sum)
                else:
                    push(s,i)
            else:
                push(s,i)
    if size(s)>1:
        return("error terlalu banyak operator")
    else:
        return pop(s)

def parenthesesCheck(teks):
    ck= Stack()
    cek=True
    error="Tidak error"
    for i in (teks):
        if i=="(" or i=="{":
            push(ck,i)
        elif (i==")") and (not(isEmpty(ck))) and (peek(ck)=="("):
            pop(ck)
        elif ((i==")") or (i=="}")) and (isEmpty(ck)):
            error=("kelebihan kurung tutup")
        elif (i=="}") and not(isEmpty(ck)) and (peek(ck)=="{"):
            pop(ck)
        elif ((i==")") and (peek(ck)=="{")) or (i=="}" and (peek(ck)=="(")):
            error=("Kurung buka dan kurung tutup tidak sesuai") 
            pop(ck)
    if not(isEmpty(ck)):
        error="Kelebihan kurung buka"
        cek=False
    elif error!="Tidak error" and isEmpty(ck):
        cek=False
    return cek,error

