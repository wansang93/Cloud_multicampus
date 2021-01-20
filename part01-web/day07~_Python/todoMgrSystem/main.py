from controller import system_controller


if __name__ == "__main__":
    system_controller.start_app()


# todos = [{"todo_id": 1, "todo_what": title}]
# todo_functionio 버전 refactoring
# todoMgrSystem 폴더 생성
# view, entity, controller, service, dao, exception package 생성: 폴더생성 __init__.py파일 생성
# entity, controller, service, exception class 선언 역할별로 구현
# todoMgrSystem / main.py 테스트
# todoMgrSustem
#       |-- main.py
#       |--view(뷰)
#            |-- view.py(menu_display, input_display, list_display, ...)
#       |--entity(프론트단의 모델 정의 + , 객체화)
#            |-- todo.py(class Todo)
#       |--controller(컨트롤러)
#            |-- system_contoller.py(시스템 컨트롤러)
#            |-- todo_contoller.py(class TodoController)(todo 컨트롤러)
#       |--service(모델 관리)
#            |--todo_service.py(class TodoService)
#       |--dao(파일 입출력)
#            |-- todo_file.py(file_read, file_write)
#       |--exception(예외 처리)
#            |-- exception.py(class IDNotFoundException)
