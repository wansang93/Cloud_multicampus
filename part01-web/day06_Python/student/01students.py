# 수강생 관리 시스템
students = [{'id': 1, 'name': '111', 'age': 11, 'major': '11111'}]
id = 1

# TODOS 참고하기

# print("===== Clound MSA 반 수강생 관리 시스템 =====")
# print("1. 수강생 정보 등록")
# print("2. 수강생 목록 보기")
# print("3. 수강생 정보 수정")
# print("4. 수강생 정보 삭제")
# print("0. 종료")
# print("===========================================")

while True:
    print("종료: x, 정보 등록: 1, 목록 보기: 2, 정보 수정: 3, 정보 삭제: 4")
    menu = input("메뉴를 선택하세요: ")
    if menu == "1":
        name = input("이름: ")
        age = input("나이: ")
        while not age.isdecimal():
            print("나이를 숫자로 입력해 주세요")
            age = input("나이: ")
        major = input("전공: ")
        student = {"id": id, "name": name, "age": int(age), "major": major}
        students.append(student)
        print(f"{name}(이)가 등록되었습니다.")
        print()
        id += 1
    elif menu == "2":
        print("===== 수강생 목록 보기 =====")
        if not students:
            print("등록된 수강생이 없습니다.")
        else:
            for student in students:
                print(student)
        print("============================")
    elif menu == "3":
        while True:
            print("(뒤로 가기: x)")
            selected_id = input("id를 입력하세요: ")
            if selected_id == "x":
                break
            while not selected_id.isdecimal():
                print("(뒤로 가기: x) 숫자가 아닙니다. 숫자로 입력해주세요")
                selected_id = input("id를 입력하세요: ")
                if selected_id == "x":
                    break
            if selected_id == "x":
                break
            for student in students:
                if student["id"] == int(selected_id):
                    modified_major = input("바꾸실 전공을 입력해 주세요: ")
                    student["major"] = modified_major
                    print(f"해당 정보가 다음과 같이 변경되었습니다. \n {student}")
                    break
            else:
                print("해당하는 아이디가 없습니다.")
                print("id 목록은", end=" ")
                for student in students:
                    print(student["id"], end=" ")
                print("입니다.")
    elif menu == "4":
        del_num = input("삭제할 id를 입력해 주세요: ")
        while not del_num.isdecimal():
            del_num = input("숫자로 다시 입력해 주세요(뒤로 가기: x): ")
            if del_num == "x":
                break
        for student in students:
            if student["id"] == int(del_num):
                delete = input(f"{student}을 삭제하시겠습니까?[y/n]: ")
                while True:
                    if delete in ['y', 'Y']:
                        students.remove(student)
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
    elif menu == "x":
        print("수강생 관리 프로그램을 종료합니다.")
        break
    else:
        print()
        print("잘못 입력하셨습니다. 다시 선택해 주세요.")
        print("종료: x, 정보 등록: 1, 목록 보기: 2, 정보 수정: 3, 정보 삭제: 4")