from entity.student import Student

#menu display
def menu_dispay():
    print("====== Cloud MSA 반 수강생 관리 시스템 ======")
    print("1.수강생 정보 등록")
    print("2.수강생 목록 보기")
    print("3.수강생 정보 수정")
    print("4.수강생 정보 삭제")
    print("0.종료")

#menu select display
def menu_select():
    menu = input("메뉴를 선택하세요 : ")
    return menu

#message display
def message_display(message):
    print(message)


#list display
def list_display(students) :
    print("==== 수강생 목록 ====")
    for student in students :
        print(student)      #Student 재정의한 __str__

#Student input display
def input_display():
    id = input("아이디 : ")
    name = input("이름 : ")
    age = input("나이 :" )
    while not age.isdecimal() :
        print("나이는 숫자로 입력해 주세요.")
        age=input("나이 : ")
    
    major = input("전공 : ")
    return Student(id, name, int(age), major)

#update input display
def update_display():
    id = input("수정할 수강생 번호 : ")
    major = input("수정할 전공 : ")
    return (id, major)

#delete input dispaly
def delete_display():
    id = input("수정할 수강생 번호 : ")
    return id