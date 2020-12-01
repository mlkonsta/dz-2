
first_task=input("Введите ключ(name или account): ").lower()

account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}
user1 = {'name': 'Иван', 'age': '20','account':[account1]}
user2 = {'name': 'Петр', 'age': '25','account':[account2]}
user3 = {'name':'Ольга', 'age': '18','account':[account3]}
user4 = {'name': 'Анна', 'age': '27','account':[account4]}
user_list=[user1, user2, user3, user4]
account_list=[account1, account2, account3, account4]

try:
    print(f"Значение ключа {first_task} для юзера1={user1[first_task]}")
    print(f"Значение ключа {first_task} для юзера2={user2[first_task]}")
    print(f"Значение ключа {first_task} для юзера3={user3[first_task]}")
    print(f"Значение ключа {first_task} для юзера4={user4[first_task]}")
   
except:
    print('Введенный ключ не найден')

try:

    second_task=int(input("Введите порядковый номер: "))
    print(f"Данные по юзеру № {second_task}:\n"
    f"имя = {user_list[second_task-1]['name']}\n"
    f"возраст = {user_list[second_task-1]['age']}\n"
    f"логин = {account_list[second_task-1]['login']}\n"
    f"пароль = {account_list[second_task-1]['password']}\n")
    summ=int(user1['age'])+int(user2['age'])+int(user3['age'])+int(user4['age'])
    result=summ/(len(user_list))
    print("Средний возраст пользователя: "+str(result))
  
except IndexError:
    print('Пользователь с указанным номером не найден')

try:
    third_task=int(input("Введите номер пользователя, которого необходимо поместить в конец: "))
    print ("The original list is : " + str(user_list))
   
    element=user_list.pop(third_task-1)
    user_list.append(element)
    print (user_list)
    
except IndexError:
    print('Пользователь с указанным номером не найден')