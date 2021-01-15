from todoMgrSystem.view import template_view
import todoMgrSystem.controller.todo_controller


def start_app():
    # 1. 앱의 시작을 알립니다.
    template_view.display_start_app()
    # TODO: 2. 파일을 연결합니다.
    # 3. 모델을 불러옵니다.
    controller = todoMgrSystem.controller.todo_controller.TodoController()
    # 4. 메인 컨트롤러의 무한 루프를 들고 옵니다.
    loop(controller)


def loop(controller):
    while True:
        template_view.display_menu()
        
        menu = template_view.select_menu()
        
        if menu == "1":  # 등록
            todo_object = template_view.display_register()
            controller.register(todo_object)
        elif menu == "2":  # 보기
            pass
        elif menu == "3":  # 수정
            pass
        elif menu == "4":  # 삭제
            pass
        else:
            # menu 가 x(종료)일 경우 종료
            if is_button_x(menu):
                template_view.display_exit_app()
                break
            # x(종료)가 아닐 경우 다시 입력
            else:
                template_view.display_reinput()


def is_button_x(x):
    if x in ["x", "X"]:
        return True
    else:
        return False
