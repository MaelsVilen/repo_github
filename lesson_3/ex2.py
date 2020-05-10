def user_data(first_name, second_name, year, city, email, phone):
    print(f"Пользователь {first_name} {second_name}, {year} года рождения, проживающий в городе {city}.", end=' ')
    print(f"Электронная почта: {email}, телефон: {phone}")


user_data(first_name=input("введите имя >> "),
          second_name=input("введите фамилию >> "),
          year=int(input("введите год рождения >> ")),
          city=input("введите город проживания >> "),
          email=input("введите почту >> "),
          phone=input("введите контактный телефон >> "))
