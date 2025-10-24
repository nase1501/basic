# 객체 지향 프로그래밍 (OOP): Object-Oriented Programming

# car.speed , Object.Attribute
# car.stop(), Object.method (객체묶여버린 함수)
#
# import another_module
#
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy =Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkBlue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names =["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu","Electric"],
    ["Squirtle","Water"],
    ["Charmander","Fire"]
])

# table.add_column("Pokemon Name",[])
# table.add_column("Type,[])

table.align = "l"

print(table)

# 추가사항
print(table)