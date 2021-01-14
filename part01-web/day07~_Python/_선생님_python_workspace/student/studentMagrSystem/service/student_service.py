#비즈니스 로직 처리
from exception.duplicate_exception import DuplicateException
from exception.idnotfound_exception import IDNotFoundException
from dao.file_dao import save_list, init_data_load

class StudentService :

    students=[] #클래스 변수  : 프로그램시작시 파일에서 Student객체 읽어서 한번 초기화

    #수강생 등록 : list students에 id중복체크하고 존재하지 않는 경우 정보 저장하고 message 리턴, 존재하는 경우 DuplicateException 발생
    def register(self, student) :
        index = self.is_exist(student.id)
        if index < 0 : 
            StudentService.students.append(student)
            return "{0}(이)가 등록되었습니다.".format(student.name)
        else :
            try:
                raise DuplicateException(student.id)
            except DuplicateException as inputError:
                return str(inputError)

    #수강생 목록 : list students 목록 리턴
    def getAllStudents(self):
        return StudentService.students

    #수강생 수정 : id를 검색해서 전공정보 수정하고 message 리턴, 존재하지 않는 경우 IDNotFoundException 발생
    def update(self,id, major):
        index = self.is_exist(id)
        if index > -1 :
            StudentService.students[index].major= major 
            return "{0}의 전공 정보가 수정되었습니다.".format(id)
        else :
            try:
                raise IDNotFoundException(id)
            except IDNotFoundException as updateError:
                return str(updateError)

    #수강생 삭제 :id를 검색해서 수강생 정보 삭제 message 리턴 존재하지 않는 경우 IDNotFoundException 발생
    def remove(self,id) :
        index = self.is_exist(id)
        if index > -1 :
            StudentService.students.pop(index)
            return "{0} 정보를 삭제했습니다.".format(id)
        else :
            try:
               raise IDNotFoundException(id) 
            except IDNotFoundException as removeError:
               return str(removeError)

    #수강생 존재여부 : id 검색해서 list students의 index 값 리턴
    def is_exist(self,id):
        for index, student in enumerate(StudentService.students):
            if student.id == id :
                return index
        return -1

    #file read
    def file_read(self) :
        StudentService.students = init_data_load()

    #file write
    def file_write(self) :
        save_list(StudentService.students)