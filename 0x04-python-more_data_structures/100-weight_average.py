#!/usr/bin/python3
def weight_average(my_list=[]):
    temp = []
    score = 0
    weight = 0
    if my_list:
        for i in my_list:
            temp.append(i[0] * i[1])
            weight += i[1]
        for i in temp:
            score += i
        return score / weight
    else:
        return None
