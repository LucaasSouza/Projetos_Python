listTasks = []

class Tasks:
    def __init__(self, task = None):
        self.task = task

    def addTask(self):
        listTasks.append(self.task)
        print('Tarefa adicionada!')

    def findTask(self, id):
        return print('Tarefa não encontrada!') if (id <= 0) or ((id - 1) >= len(listTasks)) else True

    def editTask(self, id, newTask):
        taskFinded = self.findTask(id)
        if taskFinded:
            listTasks[id - 1] = newTask
            print('Tarefa editada!')

    def deleteTask(self, id):
        taskFinded = self.findTask(id)
        if taskFinded:
            print('Tarefa excluída!')
            del listTasks[id - 1]