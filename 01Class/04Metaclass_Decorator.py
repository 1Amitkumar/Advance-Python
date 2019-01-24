class MetaStudents(type):

    def __new__(mcs, name, bases, dict):
        cls = type.__new__(mcs, name, bases, dict)

        def wrapper(*args):
            instance = cls('students')
            instance.students = args[0]
            return instance

        return wrapper


class TopperStudents(metaclass=MetaStudents):

    def __init__(self, name):
        self.name = name


students = TopperStudents(3)
print(students.students, students.name)

