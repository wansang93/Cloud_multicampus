from todoMgrSystem.controller import system_controller


if __name__ == "__main__":
    system_controller.start_app()


# # todos = [{"todo_num": 1, "title": title}]
# todo_functionio 버전 refactoring
# todoMgrSystem 폴더 생성
# view, entity, controller, service, dao, exception package 생성: 폴더생성 __init__.py파일 생성
# entity, controller, service, exception class 선언 역할별로 구현
# todoMgrSystem / main.py 테스트
# todoMgrSustem
#       |-- main.py
#       |--view(뷰)
#            |-- view.py(menu_display, input_display, list_display, ...)
#       |--entity(모델 생성)
#            |-- todo.py(class Todo)
#       |--controller(컨트롤러)
#            |-- todo_contoller.py(class TodoController)
#       |--service(모델 관리)
#            |--todo_service.py(class TodoService)
#       |--dao(파일 입출력)
#            |-- todo_file.py(file_read, file_write)
#       |--exception(예외 처리)
#            |-- exception.py(class IDNotFoundException)