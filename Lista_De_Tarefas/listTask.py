from classTask import *

def showList():
    print('----- Lista de Tarefas -----')
    for i in range(len(listTasks)):
        print(f'{str(i + 1)}. {listTasks[i]}')
    print('----------------------------')

def verifyLength():
    return True if len(listTasks) > 0 else print('Não há tarefas na lista.')

def menu():
    while True:
        choice = input('\nEscolha um menu: \n1- Ver tarefas da lista \n2- Adicionar tarefa \n3- Editar tarefa \n4- Excluir tarefa \n5- Limpar lista \n6- Sair \n')

        if (choice.isnumeric()) and (int(choice) >= 1) and (int(choice) <= 6):
            if choice == '1': #Mostra lista de tarefas
                if verifyLength():
                    showList()
            elif choice == '2': #Adicionar tarefa
                task = Tasks(input('Digite o nome da tarefa: '))
                task.addTask()
            elif choice == '3': #Editar tarefa
                if verifyLength():
                    showList()
                    Tasks().editTask(int(input('Digite o id da tarefa: ')), input('Digite a nova tarefa: '))
            elif choice == '4': #Excluir tarefa
                if verifyLength():
                    showList()
                    Tasks().deleteTask(int(input('Digite o id da tarefa: ')))
            elif choice == '5': #Limpa lista de tarefas
                listTasks.clear()
                print('Lista zerada!')
            elif choice == '6': #Encerra o sistema
                print('Até mais!')
                break
        else:
            print('Menu inválido! Tente novamente')

menu()