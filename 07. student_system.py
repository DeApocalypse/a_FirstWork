class student:
    amount=0
    def __init__(self,name,score):
        self.name=name
        self.score=score
        student.amount+=1
        print("학생 추가가 완료되었습니다")
    def __del__(self): #객체 삭제함수->재정의
        print("학생 삭제완료")
        student.amount-=1
    def show(self):
        print(self.name,"의 성적은",self.score,"입니다.")
    def change(self):
        print("학생의 이름과 성적을 다시 입력합니다.")
        self.name=input("이름입력: ")
        self.score=int(input("성적입력: "))
        print("학생정보 변경 완료")
    

students=list()
while True:
    print()
    print("----학생 프로그램----")
    print("1.학생추가 2.학생삭제 3.성적조회 4.우수학생 5.학생정보수정 6.총 인원수 7.종료")
    act=int(input("번호입력: "))
    if act==1:
        print("학생의 이름과 성적을 입력해주세요.")
        name=input("이름입력: ")
        score=int(input("성적입력: "))
        students.append(student(name,score))
    elif act==2:
        name=input("삭제할 학생의 이름입력: ")
        sw=1
        for v in students:
            if v.name==name:
                students.remove(v)
                sw=0
                del v
        if sw==1:
            print("해당 학생이 존재하지 않습니다!")
    elif act==3:
        for v in students:
            v.show()
    elif act==4:
        Max=0
        maxname=""
        for v in students:
            if v.score>Max:
                Max>v.score
                maxname=v.name
        print("이번 우수학생의 이름은",maxname,"입니다.")
    elif act==5:
        name=input("변경할 학생의 이름입력: ")
        sw=1
        for v in students:
            if v.name==name:
                v.change()
                sw=0
                break
    elif act==6:
        print("총 인원 수는",student.amount,"명 입니다.")
    elif act==7:
        print("학생 프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")
