class TodoService():
    
    todo = []

    def register(self, todo_object):
        index = self.is_exist(todo_object.todo_num)
