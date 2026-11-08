class Discipline:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Student:
    def __init__(self, sid, name, spec, sem=1):
        self.sid = sid
        self.name = name
        self.spec = spec
        self.sem = sem
        self.grades = {}

class Department:
    def __init__(self, name):
        self.name = name
        self.discs = {}

class Faculty:
    def __init__(self):
        self.students = {}
        self.departments = {}

    def find_student(self, student_id):
        if student_id not in self.students:
            raise ValueError("Студент с таким id нету")
        return self.students[student_id]

    def enrol_student(self, student_id, name, specialty):
        if student_id in self.students:
            raise ValueError("Уже есть такой студент")
        new_student = Student(student_id, name, specialty)
        self.students[student_id] = new_student
        print(" Студент зачислен")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print(" Студент не найден")
            return
        del self.students[student_id]
        print(" Студент отчислен.")

    def add_to_discipline(self, student_id, discipline_name):
        if student_id not in self.students:
            print(" Студента нет")
            return
        student = self.students[student_id]
        found_discipline = None
        for dep in self.departments.values():
            if student.spec in dep.discs:
                for disc in dep.discs[student.spec]:
                    if disc.name.lower() == discipline_name.lower():
                        found_discipline = disc
            if found_discipline:
                break
                
        if found_discipline is None:
            print(" Эта дисциплина не читается")
            return
            
        student.grades[found_discipline] = None
        print(" Студент записан на дисциплину")

    def delete_from_discipline(self, student_id, discipline_name):
        if student_id not in self.students:
            print(" Студента нет")
            return
        student = self.students[student_id]
        
        for disc in list(student.grades.keys()):
            if disc.name.lower() == discipline_name.lower():
                del student.grades[disc]
                print("Студент удален ")
                return
        print(" Студент не записан на эту дисциплину")

    def set_grades(self, student_id, discipline_name, grade):
        if student_id not in self.students:
            print(" Студент нет")
            return
        if grade < 1 or grade > 10:
            print(" Оценка должна быть от 1 до 10")
            return 
            
        student = self.students[student_id]
        for disc in student.grades.keys():
            if disc.name.lower() == discipline_name.lower():
                student.grades[disc] = grade
                print(" Оценка выставлена")
                return
        print("Студент не записан на  предмет")

    def transfer_student(self, student_id):
        if student_id not in self.students:
            print(" Студента нет")
            return 
            
        student = self.students[student_id]
        if not student.grades:
            print(" У студента нет дисциплин")
            return

        for discipline, grade in student.grades.items():
            if grade is None:
                print("Есть задолженности")
                return
                
        student.sem += 1
        student.grades.clear()
        print(f"🎓 Студент переведён в {student.sem} семестр")

    def save_student_report(self, student_id):
        if student_id not in self.students:
            print(" Студента нет")
            return 
            
        student = self.students[student_id]
        filename = f"report_{student_id}.txt"
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Ведомость")
            file.write(f"Студент: {student.name}\n")
            file.write(f"Специальность: {student.spec}\n")
            file.write(f"Семестр: {student.sem}\n")
            file.write("-" * 30 + "\n")
            
            total_grade = 0
            count = 0
            
            for disc, grade in student.grades.items():
                grade_str = grade if grade is not None else "Не сдано"
                file.write(f"{disc.name} (Каф: {disc.department}): {grade_str}\n")
                if grade is not None:
                    total_grade += grade
                    count += 1
                    
            file.write("-" * 30 + "\n")
            if count > 0:
                file.write(f"Средний балл: {total_grade / count:.2f}\n")
            else:
                file.write("Оценок пока нет.\n")
                
        print(f" Ведомость сохранена в файл '{filename}'")


def main():
    my_faculty = Faculty()
    dep_rf = Department("Кафедра радиофизики и цифровых медиа технологий")
    dep_qr = Department("Кафедра квантовой радиофизики и оптоэлектроники")
    dep_fe = Department("Кафедра физической электроники и нанотехнологий")
    dep_ik = Department("Кафедра информатики и компьютерных систем")
    dep_is = Department("Кафедра интеллектуальных систем")
    dep_kb = Department("Кафедра кибербезопасности и информационных технологий")
    dep_sa = Department("Кафедра системного анализа и компьютерного моделирования")
    dep_fa = Department("Кафедра физики и аэрокосмических технологий")

    my_faculty.departments[dep_rf.name] = dep_rf
    my_faculty.departments[dep_qr.name] = dep_qr
    my_faculty.departments[dep_fe.name] = dep_fe
    my_faculty.departments[dep_ik.name] = dep_ik
    my_faculty.departments[dep_is.name] = dep_is
    my_faculty.departments[dep_kb.name] = dep_kb
    my_faculty.departments[dep_sa.name] = dep_sa
    my_faculty.departments[dep_fa.name] = dep_fa

   
    dep_ik.discs["Прикладная информатика"] = [
        Discipline("Программирование", dep_ik.name),
        Discipline("Базы данных", dep_ik.name)
    ]
    dep_sa.discs["Прикладная информатика"] = [
        Discipline("Системный анализ", dep_sa.name)
    ]
    dep_kb.discs["Кибербезопасность"] = [
        Discipline("Криптография", dep_kb.name),
        Discipline("Сетевая безопасность", dep_kb.name)
    ]
    dep_rf.discs["Радиофизика"] = [
        Discipline("Теория радиоволн", dep_rf.name),
        Discipline("Цифровая обработка сигналов", dep_rf.name)
    ]
    dep_qr.discs["Радиофизика"] = [
        Discipline("Квантовая электроника", dep_qr.name)
    ]
    dep_fe.discs["Интеллектуальная электроника"] = [
        Discipline("Микроэлектроника", dep_fe.name),
        Discipline("Нанотехнологии", dep_fe.name)
    ]
    dep_is.discs["Интеллектуальная электроника"] = [
        Discipline("Интеллектуальные системы", dep_is.name)
    ]

    
    while True:
        print("1. Зачислить студента")
        print("2. Отчислить студента")
        print("3. Записать на дисциплину")
        print("4. Удалить с дисциплины")
        print("5. Выставить оценку")
        print("6. Перевести в след. семестр")
        print("7. Сохранить ведомость")
        print("0. Выход")
        print("="*40)

        choise = input("Выбрать действие: ")

        try:
            if choise == "1":
                s_id = input("Введите id: ")
                s_name = input("Введите имя: ")
                s_spec = input("Введите специальность: ")
                my_faculty.enrol_student(s_id, s_name, s_spec)
                
            elif choise == "2":
                s_id = input("Введите id: ")
                my_faculty.delete_student(s_id)
                
            elif choise == "3":
                s_id = input("Введите id: ")
                d_name = input("Введите название дисциплины: ")
                my_faculty.add_to_discipline(s_id, d_name)
                
            elif choise == "4":
                s_id = input("Введите id: ")
                d_name = input("Введите название дисциплины: ")
                my_faculty.delete_from_discipline(s_id, d_name)
                
            elif choise == "5":
                s_id = input("Введите id: ")
                d_name = input("Введите название дисциплины: ")
                g_input = input("Введите оценку: ")
                g = int(g_input) 
                my_faculty.set_grades(s_id, d_name, g)
                
            elif choise == "6":
                s_id = input("Введите id: ")
                my_faculty.transfer_student(s_id)
                
            elif choise == "7":
                s_id = input("Введите id: ")
                my_faculty.save_student_report(s_id)
                
            elif choise == "0":
                print("Выход")
                break
                
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()