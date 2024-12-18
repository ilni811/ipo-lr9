class RectCorrectError(Exception):  # Класс для ошибки 
    pass
def isCorrectRect(rectangles):
    counter = 0
    for i in rectangles:
        counter += 1
        if i[0][0] > i[1][0] or i[0][1] > i[1][1]:
            raise ValueError(f'Один из прямоугольников некорректный: {counter}')
    return True
