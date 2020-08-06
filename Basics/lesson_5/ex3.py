"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников."""


with open("text_3.txt", encoding="UTF-8") as salary_rep:
    n, overall_salary = 0, 0
    print('Список сотрудников, получающих менее 20 тыс. в месяц:')
    for item in salary_rep:
        worker_list = item.split()
        salary = float(worker_list[1])
        if salary < 20000:
            print(worker_list[0])
        overall_salary += salary
        n += 1
    print(f'Средняя зарплата в учреждении:\n{overall_salary / n:.2f}')
