class TaskManager:
    def __init__(self):
        self.tasks = []
        self.users = []

#2) Реализация методов:

#Добавление задачи:

def add_task(self, task):
    self.tasks.append(task)


#Назначение задачи пользователю:

def assign_task(self, task, user):
    task.assign_to(user)


#Пометка задачи как выполненной:

def mark_task_done(self, task):
    task.mark_done()


#Отображение сведений о задачах:

def display_tasks(self):
    for task in self.tasks:
        print(task)


#3) Создание класса User:


class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        self.assigned_tasks = []


#4) Реализация методов:

#Создание учетной записи пользователя:

def create_user(self, name, email, role):
    user = User(name, email, role)
    self.users.append(user)


#Обновление информации о пользователе:

def update_user_info(self, user, name=None, email=None, role=None):
    user.name = name or user.name
    user.email = email or user.email
    user.role = role or user.role


#Просмотр назначенных задач:

def display_assigned_tasks(self, user):
    for task in user.assigned_tasks:
        print(task)


#5) Применение инкапсуляции:

#Ограничение доступа к конфиденциальной пользовательской информации:

class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        self._password = None
        self.assigned_tasks = []

    def set_password(self, password):
        self._password = password

    def __str__(self):
        return f"{self.name} ({self.email})"


#Ограничение доступа к операциям, связанным с задачами, только для авторизованных пользователей:

class Task:
    def __init__(self, description):
        self.description = description
        self.user_assigned_to = None
        self.is_done = False

    def assign_to(self, user):
        self.user_assigned_to = user

    def mark_done(self):
        self.is_done = True

class TaskManager:
    def add_task(self, task, user):
        if user.role == "admin":
            self.tasks.append(task)
        else:
            print("You do not have the permission to perform this operation.")

    def assign_task(self, task, user, assigned_user):
        if user.role == "admin":
            task.assign_to(assigned_user)
        else:
            print("You do not have the permission to perform this operation.")

    def mark_task_done(self, task, user):
        if user.role == "admin" or task.user_assigned_to == user:
            task.mark_done()
        else:
            print("You do not have the permission to perform this operation.")


#6) Использование наследования для создания специализированных пользовательских ролей:


class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email, "admin")

    def assign_task(self, task, assigned_user):
        task.assign_to(assigned_user)

class RegularUser(User):
    def __init__(self, name, email):
        super().__init__(name, email, "regular_user")


#7) Внедрение проверки данных:

#Проверка на допустимость назначения задачи:

def assign_task(self, task, user, assigned_user):
    if user.role == "admin":
        if assigned_user == user:
            print("You cannot assign a task to yourself.")
        elif assigned_user.role == "admin":
            print("You cannot assign a task to another admin.")
        else:
            task.assign_to(assigned_user)
    else:
        print("You do not have the permission to perform this operation.")


#Проверка на допустимость выполнения задачи:

def mark_task_done(self, task, user):
    if user.role == "admin" or task.user_assigned_to == user:
        if task.is_done:
            print("Task is already marked as done.")
        else:
            task.mark_done()
    else:
        print("You do not have the permission to perform this operation.")