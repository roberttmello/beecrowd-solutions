x_coordinate, y_coordinate = list(map(float, input().split()))

if x_coordinate == 0.0 and y_coordinate == 0.0:
    print("Origem")
elif x_coordinate == 0.0:
    print("Eixo Y")
elif y_coordinate == 0.0:
    print("Eixo X")
elif x_coordinate > 0.0 and y_coordinate > 0.0:
    print("Q1")
elif x_coordinate > 0.0 > y_coordinate:
    print("Q4")
elif x_coordinate < 0.0 < y_coordinate:
    print("Q2")
else:
    print("Q3")
