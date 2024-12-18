from .CorrectRect import isCorrectRect, RectCorrectError


def isCollisionRect(rectangles):
    try:
        isCorrectRect(rectangles)
    except RectCorrectError as e:
        print(e)
        return False
    x1, y1 = rectangles[0][0]
    x2, y2 = rectangles[0][1]

            # Второй прямоугольник
    x3, y3 = rectangles[1][0]
    x4, y4 = rectangles[1][1]

            # Границы пересечения
    left = max(x1, x3)
    top = min(y2, y4)
    right = min(x2, x4)
    bottom = max(y1, y3)

            # Ширина и высота пересечения
    width = right - left
    height = top - bottom

            # Проверяем пересечение
    if width > 0 and height > 0:
        return True  

    return False  