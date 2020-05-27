#게임.py

import random


#사용자의 기본 정보
job = "무직"
hp = 0
mp = 0
cash = 0

while True:
    print("******Game******")
    print("사용자 정보 출력 ---")
    print("직업: ", job)
    print("hp: ", hp)
    print("mp: ", mp)
    print("cash :", cash)
    print("--------------------")
    print("1. 캐릭터 선택")
    print("2. 몬스터 전쟁")
    print("3. 상점")
    print("4. 끝내기")
    sc = int(input("입력"))
    if sc == 1:
        print("****캐릭터****")
        print("\t직업\tHP\tMP\tCASH")
        print("1. \t마법사\t200\t500\t500$")
        print("2. \t전사\t300\t300\t300$")
        print("3. \t힐러\t500\t200\t700$")
        selChar = int(input("선택:"))
        if selChar == 1:
            job = "마법사"
            hp = 200
            mp = 500
            cash = 500
        elif selChar == 2:
            job = "전사"
            hp = 300
            mp = 300
            cash = 300
        elif selChar == 3:
            job = "힐러"
            hp = 500
            mp = 200
            cash = 700
        else:
            print("잘못입력하셨습니다.")
    elif sc == 2:
        monster_hp = random.randrange(100, 401)
        monster_mp = random.randrange(100, 401)
        while True :
            print("<전쟁선택>")
            print("monster hp: ", monster_hp, "monster mp: ", monster_mp)
            print("user hp: ", hp, "user mp: ", mp)
            print("1. 공격")
            print("2. 수비")
            print("3. 전쟁종료")
            ch = int(input("입력: "))
            if ch == 1:
                monster_hp -= mp
                hp -= monster_mp
                if hp <= 0:
                    print("Game Over")
                    hp = 0
                    break
                elif monster_hp <= 0:
                    print("Win")
                    print("포상금 300$ 획득!")
                    cash += 300
                    break
                elif monster_hp > 0 and hp > 0:
                    print("전쟁 계속~")
            elif ch == 2:
                monster_hp -= mp//2
                hp -= monster_mp//2
                if hp <=0:
                    print("Game Over")
                    hp = 0
                    break
                elif monster_hp <= 0:
                    print("Win")
                    print("포상금 300$ 획득")
                    cash += 300
                    break
                elif monster_hp > 0:
                    print("전쟁 계속~")
            elif ch == 3:
                print("전쟁을 종료하겠습니다.")
                break
        else :
            print("잘못입력하셨습니다.")
    elif sc == 3:
        print("------------상점------------")
        print("\titem\tinfo\tcash")
        print("1.\tHP\t+100hp\t20$")
        print("2.\tMP\t+100mp\t20$")
        buy = int(input("구매할번호:"))
        if buy ==1:
            if cash < 20:
                print("cash가 부족합니다.")
            else:
                hp += 100
                cash -= 20
                print("hp 100 증가")
        elif buy ==2:
            if cash < 20:
                print("cash가 부족합니다.")
            else:
                mp += 100
                cash -= 20
                print("mp 100 증가")
        else :
            print("잘못입력하셨습니다.")
        
    elif sc == 4:
        print("소환사님이 게임을 종료하셨습니다.")
        break
    else:
        print("잘못 입력하셨습니다.")
