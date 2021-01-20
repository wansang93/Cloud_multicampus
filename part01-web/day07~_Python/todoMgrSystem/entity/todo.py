class Todo():

    # 생성자: id, what
    def __init__(self, id, what):
        self.id = id
        self.what = what

    def __str__(self):
        return f"id: {self.id}, what: {self.what}"

    def set_id(self, id):
        self.id = id

    def set_what(self, what):
        self.what = what

    def get_id(self):
        return self.id
    
    def get_what(self):
        return self.what
