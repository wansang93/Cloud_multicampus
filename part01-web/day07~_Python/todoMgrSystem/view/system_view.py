### System ###
# display start app
def display_start_app():
    print('시스템 컨트롤러에서 Todo 앱을 실행합니다.')


# display exit app
def ask_exit_app():
    print('시스템 컨트롤러에서 Todo 앱을 종료합니다.')
    text = input('정말로 나가시겠습니까? [y/n]: ')
    while True:
        if text in ['y', 'Y', 'n', 'N']:
            break
        print('y 또는 n 으로 입력해 주세요.')
        text = input()
    return text


def ask_save():
    text = input('저장 하시겠습니까? [y/n]: ')
    while True:
        if text in ['y', 'Y', 'n', 'N']:
            break
        print('y 또는 n 으로 입력해 주세요.')
        text = input()
    return text


def display_msg(msg):
    print(msg)
