import sqlite3
def create_database():
    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()

    # Создание таблицы пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            student_id INTEGER,  
            teacher_id INTEGER,  
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        );
    ''')

    # Создание таблицы студентов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            group_id INTEGER,
            FOREIGN KEY (group_id) REFERENCES groups(id)
        );
    ''')

    # Создание таблицы преподавателей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            post TEXT NOT NULL
        );
    ''')

    # Создание таблицы групп студентовs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL,
            group_course TEXT NOT NULL
        );
    ''')

    # Создание таблицы предметов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL
        );
    ''')

    # Создание таблицы аудиторий
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classrooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            classroom_name TEXT NOT NULL
        );
    ''')

    # Создание таблицы расписания звонков
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bell_schedule (
            pair_number INTEGER PRIMARY KEY,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        );
    ''')

    # Создание таблицы расписания
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT,
            date TEXT, 
            pair_number INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            teacher_id INTEGER NOT NULL,
            classroom_id INTEGER NOT NULL,
            group_id INTEGER,
            FOREIGN KEY (pair_number) REFERENCES bell_schedule(pair_number),
            FOREIGN KEY (subject_id) REFERENCES subjects(id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(id),
            FOREIGN KEY (classroom_id) REFERENCES classrooms(id),
            FOREIGN KEY (group_id) REFERENCES groups(id)
        );
    ''')

    # Добавление тестовых данных
    cursor.execute('''
        INSERT INTO users (login, password, role, teacher_id, student_id)
        VALUES
        ('admin', 'password', 'администратор', NULL, NULL),
        ('teacherIvan', 'password123', 'преподаватель', 1, NULL),
        ('teacherPetr', 'password123', 'преподаватель', 2, NULL),
        ('teacherVas', 'password123', 'преподаватель', 3, NULL),
        ('teacherVasnec', 'password123', 'преподаватель', 4, NULL),
        ('teacherSmirn', 'password123', 'преподаватель', 5, NULL),
        ('teacherLeb', 'password123', 'преподаватель', 6, NULL),
        ('teacherKlem', 'password123', 'преподаватель', 7, NULL),
        ('teacherNik', 'password123', 'преподаватель', 8, NULL),
        ('studentSt', 'student123', 'студент', NULL, 1),
        ('studentMat', 'student123', 'студент', NULL, 2),
        ('studentIv', 'student123', 'студент', NULL, 3),
        ('studentSok', 'student123', 'студент', NULL, 4),
        ('studentPet', 'student123', 'студент', NULL, 5),
        ('studentIgn', 'student123', 'студент', NULL, 6),
        ('studentMaks', 'student123', 'студент', NULL, 7),
        ('studentKuch', 'student123', 'студент', NULL, 8),
        ('studentEg', 'student123', 'студент', NULL, 9),
        ('studentVlas', 'student123', 'студент', NULL, 10);
    ''')

    cursor.execute('''
        INSERT INTO groups (group_name, group_course)
        VALUES
        ('101ИС', 1),
        ('201ИС', 2),
        ('202ИС', 2),
        ('301ИС', 3),
        ('401ИС', 4);
    ''')

    cursor.execute('''
        INSERT INTO students (name, group_id)
        VALUES
        ('Студентов Михаил Иванович', 1),
        ('Матюшенко Анатолий Евгеньевич', 1),
        ('Иванов Алексндр Юрьевич', 2),
        ('Соколов Михаил Александрович', 2),
        ('Петрова Анна Владимировна', 3),
        ('Игнатов Владимир Павлович', 3),
        ('Максимова Наталья Евгеньевна', 4),
        ('Кучарёва Евгения Андреевна', 4),
        ('Егорова Светлана Васильевна', 5),
        ('Власова Виктория Алексеевна', 5);
    ''')

    cursor.execute('''
        INSERT INTO subjects (subject_name)
        VALUES
        ('Элементы высшей математики'),
        ('Физика'),
        ('Основы алгоритмизации и программирования'),
        ('Литература'),
        ('Обществознание'),
        ('Информатика'),
        ('Экология'),
        ('МДК.01.01 Разработка программных модулей'),
        ('МДК.11.01 Технология разработки и защиты баз данных'),
        ('Химия'),
        ('История'),
        ('География'),
        ('Философия');
    ''')

    cursor.execute('''
        INSERT INTO classrooms (classroom_name)
        VALUES
        ('101'),
        ('102'),
        ('103'),
        ('104'),
        ('105');
    ''')

    cursor.execute('''
        INSERT INTO teachers (name, post)
        VALUES
        ('Иванов Иван Иванович', 'Преподаватель математики'),
        ('Петров Пётр Петрович', 'Преподаватель информатики'),
        ('Васильев Владимир Львович','Преподаватель обществознания'),
        ('Васнецова Инга Николаевна', 'Преподаватель литературы'),
        ('Смирнов Сергей Алексеевич', 'Преподаватель физики'),
        ('Лебедев Алексей Николаевич', 'Преподаватель химии'),
        ("Клеменко Владимир Николаевич", "Преподаватель географии"),
        ('Николаев Вячеслав Андреевич', 'Преподаватель информатики');
    ''')

    cursor.execute('''
        INSERT INTO bell_schedule (pair_number, start_time, end_time)
        VALUES
        (1, '09:00', '10:30'),
        (2, '10:45', '12:15'),
        (3, '12:30', '14:00'),
        (4, '14:40', '16:10'),
        (5, '16:30', '18:00');
    ''')

    # Заполнение таблицы расписания на неделю для разных групп
    cursor.execute('''
        INSERT INTO schedule (day, date, pair_number, subject_id, teacher_id, classroom_id, group_id)
        VALUES
        ("Понедельник", "2024-11-04", 1, 1, 1, 1, 1),
        ("Понедельник", "2024-11-04", 2, 1, 1, 2, 1),
        ("Понедельник", "2024-11-04", 3, 3, 2, 3, 2),
        ("Понедельник", "2024-11-04", 4, 9, 8, 4, 3),
        ("Понедельник", "2024-11-04", 3, 3, 8, 4, 3),
        ("Вторник", "2024-11-05", 1, 2, 5, 1, 1),
        ("Вторник", "2024-11-05", 2, 6, 2, 2, 2),
        ("Вторник", "2024-11-05", 3, 5, 3, 3, 3),
        ("Вторник", "2024-11-05", 4, 13, 4, 4, 4),
        ("Среда", "2024-11-06", 1, 2, 5, 1, 2),
        ("Среда", "2024-11-06", 2, 2, 1, 1, 2),
        ("Среда", "2024-11-06", 3, 6, 1, 1, 2),
        ("Среда", "2024-11-06", 2, 10, 6, 2, 1),
        ("Среда", "2024-11-06", 3, 6, 2, 3, 1),
        ("Среда", "2024-11-06", 3, 8, 8, 2, 3),
        ("Среда", "2024-11-06", 4, 9, 8, 2, 3),
        ("Среда", "2024-11-06", 4, 12, 7, 3, 1),
        ("Среда", "2024-11-06", 4, 3, 8, 4, 2),
        ("Четверг", "2024-11-07", 1, 2, 5, 2, 3),
        ("Четверг", "2024-11-07", 2, 6, 1, 1, 3),
        ("Четверг", "2024-11-07", 3, 8, 1, 1, 3),
        ("Четверг", "2024-11-07", 2, 10, 6, 2, 4),
        ("Четверг", "2024-11-07", 3, 12, 7, 3, 5),
        ("Четверг", "2024-11-07", 4, 8, 8, 4, 5),
        ("Четверг", "2024-11-07", 3, 8, 8, 5, 5),
        ("Пятница", "2024-11-08", 1, 1, 1, 1, 1),
        ("Пятница", "2024-11-08", 2, 8, 2, 2, 2),
        ("Пятница", "2024-11-08", 3, 7, 7, 5, 2),
        ("Пятница", "2024-11-08", 3, 11, 3, 3, 3),
        ("Пятница", "2024-11-08", 4, 4, 4, 4, 4);
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("База данных и таблицы успешно созданы!")