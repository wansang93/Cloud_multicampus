class Todo():

    # 생성자: todo_num, todo_what
    def __init__(self, todo_num, todo_what):
        self.todo_num = todo_num
        self.todo_what = todo_what

        print(f"Todo 객체 생성 완료: {self.todo_num} {self.todo_what}")

    def __str__(self):
        return f"todo_num: {self.id}, todo_what: {self.todo_what}"
