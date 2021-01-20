from view import system_view, menu_view
from controller import todo_controller
from service.todo_service import TodoService


# MENU 번호
CREATE = '1'  # Create
READ = '2'  # Read
UPDATE = '3'  # Update
DELETE = '4'  # Delete
DELETE_ALL = '5'  # Delete All
EXIT = ['x', 'X']

def start_app():
    # 1. 앱의 시작을 알립니다.
    system_view.display_start_app()
    # 2. 파일을 연결합니다.
    TodoService.read_file()
    # 3. todo 컨트롤러를 불러옵니다.
    controller = todo_controller.TodoController()
    # 4. 메인 컨트롤러의 무한 루프를 들고 옵니다.
    while True:
        menu_view.display_menu()
        
        menu = menu_view.select_menu()

        # 1. Create
        if menu == CREATE:
            todo_obj = menu_view.display_register()
            controller.register(todo_obj)
        # 2. Read
        elif menu == READ:
            controller.display_all_todos()
        # 3. Update
        elif menu == UPDATE:
            check_id = menu_view.check_id_for_update()
            # check_id
            index = controller.check_id_for_update(check_id)
            # if valid_id then get what to do
            if index != -1:
                what = menu_view.get_what_for_update()
                controller.update(index, what)
        # 4. Delete
        elif menu == DELETE:
            check_id = menu_view.check_id_for_delete()
            # check_id
            index = controller.check_id_for_delete(check_id)
            # if valid_id then delete
            if index != -1:
                controller.delete(index)
        # 5. Delete All
        elif menu == DELETE_ALL:
            if menu_view.delete_all() in ['y', 'Y']:
                controller.display_all_todos()
                controller.delete_all()
        # Exit
        elif menu in EXIT:
            # ask save
            if system_view.ask_save() in ['y', 'Y']:
                TodoService.save_file()
            # ask exit
            if system_view.ask_exit_app() in ['y', 'Y']:
                break
        # Typo Error
        else:
            # get input again
            menu_view.display_reinput()
