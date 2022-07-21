# Fucntions used to calculate roots
from math import pow, sqrt
def calcular_delta(ValDeA,ValDeB,ValDeC):
        delta=(pow(ValDeB,2))-4*ValDeA*ValDeC
        return delta
    
def calcular_raizes(delta, ValDeA,ValDeB):
    if ValDeA==0:
        text='''ERRO: O valor de A não pode ser zero.'''
        return text
    else:
        if delta<0:
            x_int=(-ValDeB)/(2*ValDeA)
            x_ima=(sqrt(abs(delta)))/(2*ValDeA)
            text='''A função tem raízes Complexas:
        X={:.1f}-{:.1f}i e X={:.1f}+{:.1f}i'''.format(x_int,x_ima,x_int,x_ima)
            return text
        elif delta==0:
            x1=(-ValDeB+sqrt(delta))/2*ValDeA
            text='''A função tem uma raíz:
        X={:.1f}'''.format(x1)
            return text
        elif delta>0:
            x1=(-ValDeB-sqrt(delta))/2*ValDeA
            x2=(-ValDeB+sqrt(delta))/2*ValDeA
            text='''A função tem duas raízes reais distintas:
        X={:.1f} e X={:.1f}'''. format(x1,x2)
            return text
           
    

