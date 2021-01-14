#입력데이터 valid 체크, service에 비즈니스 로직 호출, data 저장, view(template) 선택
from service.student_service import StudentService
from view_template.template_view import message_display,list_display

class StudentController :
    
    # service = StudentService()

    def register(self, student) :
        #만약 id가 email형식인 경우  email 맞는지 student.id valid 체크
        service = StudentService()
        message = service.register(student)  #비즈니스 메서드 호출 
        message_display(message)   #View select

    def getAllStudents(self):
        service = StudentService() 
        students = service.getAllStudents() #비즈니스 메서드 호출
        list_display(students)   #데이터 저장해서 view select

    def update(self, id, major) :
        #id, major valid check
        if id=="" or major=="" : 
            message_display("아이디와 전공 데이터 입력이 필요합니다.")
        service = StudentService()
        message = service.update(id, major)
        message_display(message)        

    def remove(self, id) :
        if id == "" :
             message_display("아이디와 전공 데이터 입력이 필요합니다.")
        service = StudentService()
        message = service.remove(id)
        message_display(message)

    def file_read(self):
        service = StudentService()
        service.file_read()

    def file_write(self):
        service = StudentService()
        service.file_write()


