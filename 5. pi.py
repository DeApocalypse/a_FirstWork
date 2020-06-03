# 파이(π)로 수렴하는 값 출력
# π=4*(1-1/3+1/5-1/7...)

pie=4
b=1
value=0
    
while True:
    value=4*(-1)**b/(2*b+1)
    pie+=value
    b+=1
    print(pie)
