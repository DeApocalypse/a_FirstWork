phoneBook={'가길동':'010-1234','가길동1':'010-1111','나길동':'010-3333'}
while True:
    print('☆★☆★Phone Book☆★☆★')
    print('1. 회원 등록')
    print('2. 회원 수정')
    print('3. 회원 검색')
    print('4. 회원 출력')
    print('5. 끝내기')
    sc=int(input('선택:'))
    if sc==1:
        newName=input('이름:')
        newPhone=input('전화번호:')
        if newName in phoneBook:
            p_klist=list(phoneBook.keys())
            print(p_klist)
            p2_klist=list()
            for i in p_klist:
                if i[0:3] == newName:
                    p2_klist.append(i)
            p2_klist.reverse()
            print(p2_klist)
            if len(p2_klist[0])<=3:
                newName=newName+'1'
            else:
                num=int(p2_klist[0][3])
                num+=1
                newName=newName+str(num)
            phoneBook[newName]=newPhone       
        else:
            phoneBook[newName]=newPhone
    elif sc==2:
        #1) 사용자한테 수정할 이름 입력받기
        updateName=input('수정할 이름:')

        #2)입력한 이름이 딕셔너리에 존재하는 키인가?
        if updateName in phoneBook:
            # 3) 만약 존재한다면 수정 가능
            # 수정값=수정할번호입력
            updatePhone=input('수정할 번호:')
            # 딕셔너리[이름]=수정값
            phoneBook[updateName]=updatePhone
        else: #4) 존재x
            print('전화번호부에 없는 이름입니다')
    elif sc==3:
        #1) 사용자한테 검색할 이름 입력
        searchName=input('검색할 이름:')

        #2) 이름이 딕셔너리에 존재한다면,
        if searchName in phoneBook:
            print('찾으시는 번호:',phoneBook[searchName])
            
        #3) 이름이 존재하지 않는다면,
        else:
            print('없는 이름입니다')
    elif sc==4:
        k_list=list(phoneBook.keys())
        idx=1
        for each_key in k_list:
            print(idx,'.',each_key,':',phoneBook[each_key])
            idx+=1
            
    elif sc==5:
        print('종료')
        break
    else:
        print('잘못입력하셨습니다')
