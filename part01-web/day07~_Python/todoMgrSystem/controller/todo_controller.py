from service.todo_service import TodoService
from view.system_view import display_msg

''' Controller의 역할
입력 데이터 valid 체크
service에 비지니스 로직 호출
data 저장
view(template) 선택
'''

# 나중에 에러 메시지로 뺄 수 있는 함수들
def is_valid_id(id):
    if id.isdigit():
        return True
    display_msg('id는 숫자를 입력해 주세요!')
    return False


def is_vaild_what(what):
    if what:
        return True
    display_msg('공백이 아닌 것으로 입력해 주세요!')
    return False


def is_not_unique():
    display_msg('해당 id는 유니크가 아닙니다. 다시 실행해 주세요!')


def is_empty_todos():
    display_msg('todo가 없습니다. 새로 만들어 주세요!')


def is_not_match():
    display_msg('매치되는 id가 없습니다. 다시 검색해 주세요!')


def did_well():
    display_msg('성공적으로 처리되었습니다.')


# TodoController 정의
class TodoController():

    def __init__(self):
        display_msg("시스템 컨트롤러에서 TodoController를 생성합니다!")

    # 1. Create
    def register(self, todo_obj):
        # 서버단에서 Type 에러 체크
        if not is_valid_id(todo_obj.get_id()):
            return
        # 서버단에서 Type 에러 체크
        if not is_vaild_what(todo_obj.get_what()):
            return
        # 서버단에서 unique 체크
        todos = TodoService.get_todos()
        check_id = todo_obj.get_id()
        if todos:
            for todo in todos:
                if todo.get_id() == check_id:
                    is_not_unique()
                    return

        TodoService.register(todo_obj)
        did_well()

    # 2. Read
    def display_all_todos(self):
        todos = TodoService.get_todos()

        if not todos:
            is_empty_todos()
            return
        
        for todo in todos:
            display_msg(todo)

    # 3. Update
    # id(id) 체크
    def check_id_for_update(self, check_id):
        # 서버단에서 Type 에러 체크
        if not is_valid_id(check_id):
            return False
        
        todos = TodoService.get_todos()

        if todos:
            for i, todo in enumerate(todos):
                if todo.get_id() == check_id:
                    return i
            else:
                is_not_match()
                return -1
        else:
            is_empty_todos()
            return -1

    def update(self, index, what):
        TodoService.update(index, what)
        did_well()

    # 4. Delete
    # id 체크
    def check_id_for_delete(self, check_id):
        # 서버단에서 Type 에러 체크
        if not is_valid_id(check_id):
            return False
        
        todos = TodoService.get_todos()

        if todos:
            for i, todo in enumerate(todos):
                if todo.get_id() == check_id:
                    return i
            else:
                is_not_match()
                return -1
        else:
            is_empty_todos()
            return -1

    def delete(self, index):
        TodoService.delete(index)
        did_well()

    # 5. Delete All
    def delete_all(self):
        TodoService.delete_all()
        did_well()