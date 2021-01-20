import os.path

#수강생 관리 시스템
students=[] #global variable

#수강생 등록 : list students에 id중복체크하고 존재하지 않는 경우 정보 저장하고 message 리턴
def register(student) :
    index = is_exist(student["id"])
    if index < 0 : 
        students.append(student)
        return "{0}(이)가 등록되었습니다.".format(student["name"])
    else :
        return "이미 등록된 정보입니다." 

#수강생 목록 : list students 목록 리턴
def getAllStudents():
    return students

#수강생 수정 : id를 검색해서 전공정보 수정하고 message 리턴
def update(id, major):
    index = is_exist(id)
    if index > -1 :
        students[index]["major"] = major 
        return "{0}의 전공 정보가 수정되었습니다.".format(id)
    else :
        return "{0}의 정보가 존재하기 않습니다.".format(id)

#수강생 삭제 :id를 검색해서 수강생 정보 삭제 message 리턴
def remove(id) :
    index = is_exist(id)
    if index > -1 :
        students.pop(index)
        return "{0} 정보를 삭제했습니다.".format(id)
    else :
        return "{0} 정보가 존재하지 않습니다.".format(id)

#수강생 존재여부 : id 검색해서 list students의 index 값 리턴
def is_exist(id):
    for index, student in enumerate(students):
        if student["id"] == id :
            return index
    return -1

#menu display
def menu_dispay():
    print("====== Cloud MSA 반 수강생 관리 시스템 ======")
    print("1.수강생 정보 등록")
    print("2.수강생 목록 보기")
    print("3.수강생 정보 수정")
    print("4.수강생 정보 삭제")
    print("0.종료")

#message display
def message_display(message):
    print(message)


#프로그램 종료시 list students "students.dat" 파일 저장
def save_list() :
    save_file = open("students.dat", "w")
    for index, student in enumerate(students) :
        save_file.write("{0}번째 | {1},{2},{3},{4}\n".format(index, student["id"],student["name"],student["age"],student["major"]))

    save_file.close()

#프로그램 시작시 "students.dat" 파일이 존재하고 정보가 있는 경우  list students초기화
def init_data_load() :
    fileExist = os.path.isfile("students.dat")
    if fileExist :
        read_file = open("students.dat", "r")
        while True:
            data = read_file.readline()
            if len( data.split("|") )==2 :
                student = data.split("|")[1].strip("\n").split(",")
                students.append({"id":student[0].strip(), "name":student[1].strip(),"age":int(student[2].strip()),"major":student[3].strip()})
            if not data : break
        read_file.close()

init_data_load()
while True:
    menu_dispay()

    menu = input("메뉴를 선택하세요 : ")
    if menu =="1" :
        id = input("학번:")
        name = input("이름 : ")
        age = input("나이 : ")
        while not age.isdecimal() :
            print("나이는 숫자로 입력해 주세요.")
            age=input("나이 : ")
        major = input("전공 : ")
        student ={"id":id, "name":name, "age":int(age), "major":major  }
        
        message_display(register(student))
       
    elif menu =="2" :
        print("===== 수강생 목록 보기 =====")
        print(students)
    elif menu =="3" :
        id = input("수정할 수강생 번호 : ")
        major = input("수정할 전공 : ")
        
        message_display( update(id, major) )
       
    elif menu=="4" :
        id = input("삭제할 수강생 번호 : ")
        
        message_display( remove(id) )
      
    elif menu=="0" :
        message_display("수강생 관리 프로그램을 종료합니다.")
        save_list()
        break
    else :
        print()
        message_display("1,2,3,4,0 번 중 선택하세요" )
#github : python_workshop repository  - 02.todos_fileio.py 작성해보기 
#                                          {"todoid":todoid, "title":title}데이터 
#                                          등록, 수정, 삭제, 일정목록, 전체삭제 기능, dispaly 모듈화
#                                          종료시 todos.dat에 저장
#                                          시작시 todos.dat 파일 읽어서 todos list에 초기화  
