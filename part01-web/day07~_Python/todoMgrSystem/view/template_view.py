from todoMgrSystem import entity

"""
Define View
"""

### 앱 관련 문구 ###
# 앱 실행시 나오는 문구
def display_start_app():
    print("Todo 앱을 실행합니다.")


# 앱 종료시나오는 문구
def display_exit_app():
    print("Todo 앱을 종료합니다.")


# 메뉴를 보여주는 문구
def display_menu():
    print("메뉴를 보여줍니다.")


# 메뉴를 입력받는 문구
def select_menu():
    menu = input()
    return menu


# 메뉴를 다시 입력하라는 문구
def display_reinput():
    print("메뉴를 다시 입력해 주세요!")


### 메뉴 관련 문구 ###
# 메뉴1. 등록하기(Create)
def display_register():
    todo_num = input("번호: ")
    while not todo_num.isdecimal():
        print("번호는 숫자로 입력해 주세요.")
    todo_what = input("할 일: ")
    return entity.Todo(todo_num, todo_what)
    

# 메뉴2. 보여주기(Read)
def display_todo():
    print("보여주기")


# 메뉴3. 수정하기(Update)
def display_update():
    print("수정하기")


# 메뉴4. 삭제하기(Delete)
def display_delete():
    print("삭제하기")
