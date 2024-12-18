from collision.CorrectRect import isCorrectRect , RectCorrectError
from collision.CollisionRect import isCollisionRect
def main():
    while True:
     number = int(input("Выбор: 1 - isCorrectRect, 2 - intersectionAreaRect, 3 - isCollisionRect , 4 - intersectionAreaMultiRect , 5 - Выход"))
     if  number == 1:
         rectangles=[]
         x1 = float(input('Введите x1: '))
         y1 = float(input('Введите y1: '))
         x2 = float(input('Введите x2: '))
         y2 = float(input('Введите y2: '))
         rectangles.append([(x1, y1), (x2, y2)])
         try:
            print(isCorrectRect(rectangles))
         except ValueError as w:
                print(w)
     elif number == 2:
         x1 = float(input('Введите x1: '))
         y1 = float(input('Введите y1: '))
         x2 = float(input('Введите x2: '))
         y2 = float(input('Введите y2: '))
         x3 = float(input('Введите x3: '))
         y3 = float(input('Введите y3: '))
         x4 = float(input('Введите x4: '))
         y4 = float(input('Введите y4: '))
         rectangles = [(x1, y1), (x2, y2)],[(x3, y3), (x4, y4)]

         print(isCollisionRect(rectangles))
main()