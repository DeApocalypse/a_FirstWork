import random 
question_number=0
score=0

def f(n):		#단어 입력 및 결과 출력
    word=[]

    for i in range(n):
        word.append(input("단어입력:"))
    for i in range(n):
        g(word[i])
    print()
    print("점수 : ",score,"/",n*30)
    if score>n*30/2:
        print("********** 축하합니다! **********")
        print("[상품지급]")
    else:
        print("고생하셨습니다!")
        print("#상품을 받기 위해서는 과반 이상의 점수를 얻으셔야 됩니다.")
    print()
    print("게임을 종료합니다.")




def g(word):            #단어 섞고 출력 및 점수 계산

    L=[]
    number_try=0

    for i in range(len(word)):
        L.append(i)
    random.shuffle(L)
    WORD=[]
    for i in range(len(word)):
        WORD.append(word[L[i]])
    print()
    global question_number
    question_number+=1
    print(question_number,"번 문제: ",WORD,sep='')
    while number_try<3:
        print()
        print("남은 기회: ",3-number_try,"회",sep='')
        user_answer=input("정답을 입력해 주세요: ")
        if user_answer == word:
            print("정답입니다.")
            if number_try==0:
                global score
                score+=30
            elif number_try==1:
                score+=10
            else:
                pass
            break
        else:
            print("오답입니다.")
            number_try+=1

while True:			#프로세스 시작 및 종료
    print("********** 영단어 배열 게임  **********",'\n')
    sc=int(input("게임에 사용할 단어 수를 적어주세요: "))
    f(sc)
    break
