listTask = []

def list_tasks(): #Mostra as tarefas da lista
    print('----------Lista de Tarefas----------')
    for i in range(len(listTask)):
        print(str(i + 1) + '. ' + listTask[i]) #É concatenado o índice da tarefa mais o seu conteúdo. índice é usado como 'Chave primária' para algumas operações
    print('------------------------------------')

def add_task(): #Adiciona nova tarefa no último índice do array
    task = input('Insira a nova tarefa: ')
    listTask.append(task)
    print('Nova tarefa adicionada com sucesso!')

def edit_task():
    list_tasks() #Chama a função que lista as tarefas
    choice = int(input('Digite o id da tarefa para editá-la: '))
    editedTask = input('Digite a nova tarefa: ')
    try_action('edit', editedTask, choice, 'Tarefa editada com sucesso!') #Chama a função que verifica se o id é válido para continuar a edição

def delete_task():
    list_tasks()
    choice = int(input('Digite o id da tarefa para excluí-la: '))
    try_action('delete', '', choice, 'Tarefa excluída com sucesso!') #Argumentos (Chave de identificação, string vazia, id da tarefa, mensagem)

def verify_length(func):
    if len(listTask) == 0:
        print('Não há tarefas na lista!')
    else:
        return func()

def try_action(func, action, choice, msg): # listTask[choice - 1] = action if func == 'edit' else del listTask[choice - 1]
    try:
        if func == 'edit':
            listTask[choice - 1] = action
        elif func == 'delete':
            del listTask[choice - 1]
        print(msg)
    except:
        print('Id não encontrado')

def menu():
    while True:
        choice = input('\nEscolha um menu: \n1- Ver tarefas da lista \n2- Adicionar tarefas na lista \n3- Editar tarefa da lista \n4- Excluir tarefa da lista \n5- Excluir lista \n6- Sair \n')

        if (choice.isnumeric()) and (int(choice) >= 1) and (int(choice) <= 6):
            choice = int(choice)
            if choice == 1:
                verify_length(list_tasks)
            elif choice == 2:
                add_task()
            elif choice == 3:
                verify_length(edit_task)
            elif choice == 4:
                verify_length(delete_task)
            elif choice == 5:
                listTask.clear()
                print('Lista excluída com sucesso!')
            elif choice == 6:
                print('Até mais!')
                break
        else:
            print('Menu inválido! Tente novamente')

menu()