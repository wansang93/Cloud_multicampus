from todoMgrSystem.view import template_view
from todoMgrSystem.controller import todo_controller


# menu 번호 고정값 할당
REGISTER = "1"
DISPLAY = "2"
UPDATE = "3"
REMOVE = "4"
REMOVE_ALL = "5"


def start_app():
    # 1. 앱의 시작을 알립니다.
    template_view.display_start_app()
    # TODO: 2. 파일을 연결합니다.
    # 3. 모델을 불러옵니다.
    controller = todo_controller.TodoController()
    # 4. 메인 컨트롤러의 무한 루프를 들고 옵니다.
    loop(controller)


def loop(controller):
    while True:
        template_view.display_menu()
        
        menu = template_view.select_menu()
        
        if menu == REGISTER:  # 등록
            todo_object = template_view.display_register()
            controller.register(todo_object)
        elif menu == DISPLAY:  # 보기
            pass
        elif menu == UPDATE:  # 수정
            pass
        elif menu == REMOVE:  # 삭제
            pass
        elif menu == REMOVE_ALL:  # 삭제
            pass
        else:
            # menu 가 x(종료)일 경우 종료
            if is_button_x(menu):
                # 앱의 종료를 알립니다.
                template_view.display_exit_app()
                break
            # x(종료)가 아닐 경우 다시 입력
            else:
                # 
                template_view.display_reinput()


def is_button_x(x):
    if x in ["x", "X"]:
        return True
    else:
        return False
