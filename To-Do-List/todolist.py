from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
menu = """
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
"""

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


if __name__ == '__main__':
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    today = datetime.today().date()

    option = ""
    while option != '0':
        option = input(menu)

        if option == '1':
            tasks = session.query(Task).filter(Task.deadline == today).all()
            print("Today {} {}:".format(today.day, today.strftime('%b')))

            if len(tasks) == 0:
                print("Nothing to do!")
            else:
                for num, task in enumerate(tasks):
                    print("{}. {}".format(num, task.task))

        if option == '2':
            for dates_ago in range(7):
                date = today + timedelta(days = dates_ago)
                tasks = session.query(Task).filter(Task.deadline == date).all()

                print("{} {} {}:".format(date.strftime('%A'), date.day, date.strftime('%b')))
                if len(tasks) == 0:
                    print("Nothing to do!")
                else:
                    for num, task in enumerate(tasks):
                        print("{}. {}".format(num, task.task))
                print()

        if option == '3':
            tasks = session.query(Task).all()
            print("All tasks:")

            if len(tasks) == 0:
                print("Nothing to do!")
            else:
                for num, task in enumerate(tasks):
                    print("{}. {}. {} {}".format(num, task.task, task.deadline.day, task.deadline.strftime('%b')))

        if option == '4':
            tasks = session.query(Task).filter(Task.deadline < today).all()
            print("Missed tasks:")

            if len(tasks) == 0:
                print("Nothing is missed!")
            else:
                for num, task in enumerate(tasks):
                    print("{}. {}. {} {}".format(num, task.task, task.deadline.day, task.deadline.strftime('%b')))

        if option == '5':
            task_def = input("Enter task: ")
            date_def = input("Enter deadline: ").strip(" ")

            deadline = datetime.strptime(date_def, '%Y-%m-%d')

            new_task = Task(task=task_def, deadline=deadline)
            session.add(new_task)
            session.commit()
            print("The task has been added!")

        if option == '6':
            tasks = session.query(Task).all()

            if len(tasks) == 0:
                print("Nothing to do!")
            else:
                for num, task in enumerate(tasks):
                    print("{}. {}. {} {}".format(num, task.task, task.deadline.day, task.deadline.strftime('%b')))

            delete = int(input("Chose the number of the task you want to delete: "))
            session.delete(tasks[delete])
            session.commit()

            print("The task has been deleted!")
            print()


    print("Bye!")