import os
from entity.todo import Todo

PATH = 'dao/'
FILE_PATH = PATH + 'todos.dat'


# 프로그램 시작시 "todos.dat" 존재시 불러오기
def init_data_load():
    todos = []

    if os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'r', encoding='utf-8') as fp:
            while True:
                data = fp.readline()
                if not data:
                    break
                todo_info = data.rstrip().split(',')

                if len(todo_info) == 2:
                    todo_obj = Todo(todo_info[0], todo_info[1])
                    todos.append(todo_obj)

    return todos


# 프로그램 종료시 list todo "todos.dat" 파일 저장
def exit_data_save(todos):
    with open(FILE_PATH, 'w', encoding='utf-8') as fp:
        for todo_obj in todos:
            fp.write(f'{todo_obj.get_id()}, {todo_obj.get_what()}')
