from dao import file_dao


class TodoService():
    
    todos = []

    @classmethod
    def register(cls, todo_obj):
        cls.todos.append(todo_obj)
    
    @classmethod
    def get_todos(cls):
        return cls.todos

    @classmethod
    def update(cls, index, what):
        cls.todos[index].set_what(what)

    @classmethod
    def delete(cls, index):
        del cls.todos[index]

    @classmethod
    def delete_all(cls):
        cls.todos.clear()

    @classmethod
    def read_file(cls):
        cls.todos = file_dao.init_data_load()

    @classmethod
    def save_file(cls):
        file_dao.exit_data_save(cls.todos)
