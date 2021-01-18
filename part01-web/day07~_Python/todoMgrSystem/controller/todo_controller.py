from todoMgrSystem.service import todo_service

'''
입력 데이터 valid 체크
service에 비지니스 로직 호출
data 저장
view(template) 선택
'''


class TodoController():
    
    service = todo_service.TodoService()

    def __init__(self):
        print("Todo 컨트롤러 생성")


    def register(todo_object):
        pass