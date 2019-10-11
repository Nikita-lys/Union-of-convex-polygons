"""
Лысенко Никита Сергеевич 4.8

11. Объединение выпуклых полигонов
"""

# size of window
size = 100


# функция определяет, с какой стороны от вектора AB находится точка C
# (положительное возвращаемое значение соответствует левой стороне, отрицательное — правой, 0 - принадлежит).
def rotate(A, B, C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])


# find rightest point in polygon
def right_point(points):
    rightest_point = [-1000000, 0]
    for point in points:
        if point[0] > rightest_point[0]:
            rightest_point = point
    return rightest_point


# find leftest point in polygon
def left_point(points):
    leftest_point = [1000000, 0]
    for point in points:
        if point[0] < leftest_point[0]:
            leftest_point = point
    return leftest_point


# сортирует points по уменьшению y
def bubble_biggest_y(true_points):
    points = true_points.copy()
    for i in range(len(points) - 1):
        for j in range(len(points) - i - 1):
            if points[j][1] < points[j+1][1]:
                buff = points[j]
                points[j] = points[j+1]
                points[j+1] = buff
    return points


def find_vr(pointsR, vl, type):
    pointsR_sorted = bubble_biggest_y(pointsR)
    vr = pointsR_sorted[0]
    for cur_point in pointsR_sorted:
        if type == 'upper':
            if rotate(vl, vr, cur_point) > 0:
                vr = cur_point
            for point in pointsR_sorted:
                if rotate(vl, vr, point) > 0:
                    vr = point
                    continue
        else:
            if rotate(vl, vr, cur_point) < 0:
                vr = cur_point
            for point in pointsR_sorted:
                if rotate(vl, vr, point) < 0:
                    vr = point
                    continue
    return vr


def find_vl(pointsL, vr, type):
    pointsL_sorted = bubble_biggest_y(pointsL)
    vl = pointsL_sorted[0]
    for cur_point in pointsL_sorted:
        if type == 'upper':
            if rotate(vr, vl, cur_point) < 0:
                vl = cur_point
            for point in pointsL_sorted:
                if rotate(vr, vl, point) < 0:
                    vl = point
                    continue
        else:
            if rotate(vr, vl, cur_point) > 0:
                vl = cur_point
            for point in pointsL_sorted:
                if rotate(vr, vl, point) > 0:
                    vl = point
                    continue
    return vl


def bridge(pointsL, pointsR, type):
    vl = right_point(points=pointsL)
    vr = left_point(points=pointsR)
    while 2 * 2 == 4:
        vr_new = find_vr(pointsR, vl, type)
        vl_new = find_vl(pointsL, vr, type)
        if vr == vr_new and vl == vl_new:
            break
        vr = vr_new
        vl = vl_new
    return [vl, vr]


def merge(pointsL, pointsR):
    upper_line = bridge(pointsL=pointsL, pointsR=pointsR, type='upper')
    lower_line = bridge(pointsL=pointsL, pointsR=pointsR, type='lower')
    return [upper_line, lower_line]


if __name__ == '__main__':
    pointsL = [
        [1, 1],
        [2, 4],
        [5, 5],
        [6, 2],
        [4, 1],
        [3, 6]
    ]

    pointsR = [
        [10, 1],
        [9, 4],
        [11, 7],
        [14, 6],
        [14, 2],
        [14, 9]
    ]
    
    lines = merge(pointsL=pointsL, pointsR=pointsR)
    print(lines)
