from entity.todo import Todo

"""
Define View
"""


### Menu ###
# show menu
def display_menu():
    print('==================================================')
    print('등록(1) 보기(2) 수정(3) 삭제(4) 모두 삭제(5) 나가기(x)')


# select menu number
def select_menu():
    menu = input()
    return menu


# 메뉴를 다시 입력하라는 문구
def display_reinput():
    print('메뉴를 잘못 입력하였습니다. 다시 입력해 주세요.')


# 메뉴1. 등록하기(Create)
def display_register():

    while True:
        todo_id = input('id를 입력해 주세요(유니크 값으로): ')
        # 사용자 입력 폼에서 에러 체크
        if not todo_id.isdecimal():
            print('id는 숫자를 입력해 주세요.')
        else:
            break
    while True:
        todo_what = input('할 일을 입력해 주세요: ')
        # 사용자 입력 폼에서 에러 체크
        if not todo_what:
            print('공백이 아닌 것으로 입력해 주세요.')
        else:
            break

    return Todo(todo_id, todo_what)


# 메뉴3. 수정하기(Update)
# 해당하는 id가 있는지 확인하기
def check_id_for_update():
    while True:
        todo_id = input('업데이트 할 id를 입력해 주세요: ')
        # 사용자 입력 폼에서 에러 체크
        if not todo_id.isdecimal():
            print('id는 숫자를 입력해 주세요.')
        else:
            break
    return todo_id


def get_what_for_update():
    while True:
        todo_what = input('수정 사항을 입력해 주세요: ')
        # 사용자 입력 폼에서 에러 체크
        if not todo_what:
            print('공백이 아닌 것으로 입력해 주세요.')
        else:
            break
    return todo_what


# 메뉴4. 삭제하기(Delete)
def check_id_for_delete():
    while True:
        todo_id = input('삭제할 할 id를 입력해 주세요: ')
        # 사용자 입력 폼에서 에러 체크
        if not todo_id.isdecimal():
            print('id는 숫자를 입력해 주세요.')
        else:
            break
    return todo_id


# 메뉴5. 전부 삭제하기(Delete All)
def delete_all():
    print('메모를 전부 삭제합니다.')
    text = input('정말로 실행하시겠습니까? [y/n]: ')
    while True:
        if text in ['y', 'Y', 'n', 'N']:
            break
        print('y 또는 n 으로 입력해 주세요.')
    return text
