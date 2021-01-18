from controller_view.student_controller import StudentController
from view_template.template_view import menu_display, menu_select, message_display
from view_template.template_view import input_display, update_display,delete_display


controller = StudentController()


controller.file_read()
while True:
    menu_display()

    menu = menu_select()
    if menu =="1" :
        student = input_display()
        controller.register(student)
       
    elif menu =="2" :
        controller.getAllStudents()

    elif menu =="3" :
        id, major = update_display()
        controller.update(id, major)
                   
    elif menu=="4" :
        id = delete_display()
        controller.remove(id)
      
    elif menu=="0" :
        message_display("수강생 관리 프로그램을 종료합니다.")
        controller.file_write()
        break
    else :
        print()
        message_display("1,2,3,4,0 번 중 선택하세요" )

#todo_functionio 버전 refactoring
#todoMgrSystem 폴더 생성
#view, entity, controller, service, dao, exception package 생성 :폴더생성 __init__.py파일 생성
#entity, controller, service,exception class 선언 역할별로 구현
#todoMgrSystem / main.py 테스트
# todoMgrSustem
#       |-- main.py
#       |--view
#            |-- view.py (menu_display, input_display, list_display, .......)
#       |--entity
#            |-- todo.py(class Todo)
#       |--controller
#            |-- todo_contoller.py(class TodoController)
#       |--service 
#            |--todo_service.py(class TodoService)
#       |--dao
#            |-- todo_file.py(file_read, file_write) 