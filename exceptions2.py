fruits = ["banana", "apple", "watermelon", "pineapple", "strawberries"]

while True:
    user_option = (input("ingrese un número entre el 0 y el 4 para elegir tu fruta, q para salir: "))

    if user_option == "q":
      break
    try:
      print(fruits[int(user_option)])
    except IndexError:
      print("por favor ingresar un número del 0 al 4.")
    except ValueError:
      print("por favor ingresar un número.")
