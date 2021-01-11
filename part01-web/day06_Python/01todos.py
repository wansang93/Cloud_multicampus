# todos.py 작성해보기

# todos = [{"todo_num": 1, "title": title}]

# 등록, 수정, 삭제, 일정 목록, 전체 삭제

todos = [
    {"todo_num": 1, "title": "title"},
    {"todo_num": 2, "title": "tttttttt"},
    {"todo_num": 3, "title": "aaaaaaa"}
]

while True:
    print("종료: x, 등록: 1, 수정: 2, 삭제: 3, 목록: 4, 전체 삭제: 5")
    menu = input("메뉴를 선택하세요: ")
    if menu == "x":
        print("todo 관리 프로그램을 종료합니다.")
        break
    elif menu == "1":  # 등록
        todo_num = input("숫자로 입력해 주세요: ")
        while not todo_num.isdecimal():
            todo_num = input("숫자로 다시 입력해 주세요: ")
        title = input("제목을 입력해 주세요: ")

        todos.append({"todo_num": int(todo_num), "title": title})
    elif menu == "2":  # 수정
        while True:
            modified_num = input("(뒤로 가기: x), num을 입력하세요: ")
            if modified_num == "x":
                break
            while not modified_num.isdecimal():
                print("(뒤로 가기: x) 숫자가 아닙니다. 숫자로 입력해주세요")
                modified_num = input("num을 입력하세요: ")
                if modified_num == "x":
                    break
            if modified_num == "x":
                break
            for todo in todos:
                if todo["todo_num"] == int(modified_num):
                    modified_title = input("바꾸실 제목을 입력해 주세요: ")
                    todo["title"] = modified_title
                    print(f"해당 정보가 다음과 같이 변경되었습니다. \n {todo}")
                    break
            else:
                print("해당하는 번호가 없습니다. 번호 목록은", end=" ")
                for todo in todos:
                    print(todo["todo_num"], end=" ")
                print("입니다.")
                break
    elif menu == "3":  # 삭제
        del_num = input("삭제할 숫자를 입력해 주세요: ")
        while not del_num.isdecimal():
            del_num = input("숫자로 다시 입력해 주세요(뒤로 가기: x): ")
            if del_num == "x":
                break
        for todo in todos:
            if todo["todo_num"] == int(del_num):
                delete = input(f"{todo}을 삭제하시겠습니까?[y/n]: ")
                while True:
                    if delete in ['y', 'Y']:
                        todos.remove(todo)
                        print(f"{del_num}번의 정보가 삭제되었습니다.")
                        break
                    elif delete in ['n', 'N']:
                        print(f"{del_num}번의 정보가 삭제되지 않았습니다.")
                        break
                    else:
                        print("y/n 으로 대답해 주세요")
                break
        else:
            print("해당 번호는 없습니다.")
                

    elif menu == "4":  # 목록 보기
        print("===== todo 목록 보기 =====")
        if not todos:
            print("등록된 todo가 없습니다.")
        else:
            for todo in todos:
                print(todo)
        print("===== todo 목록 보기 =====")

    elif menu == "5":  # 전부 삭제
        delete = input("Todos를 전부 삭제하시겠습니까?[y/n]: ")
        while True:
            if delete in ['y', 'Y']:
                todos = []
                print(f"Todos가 전부 삭제되었습니다.")
                break
            elif delete in ['n', 'N']:
                print(f"Todos 전부 삭제를 취소했습니다.")
                break
            else:
                print("y/n 으로 대답해 주세요")
