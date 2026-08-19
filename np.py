def f_p_g(grades, threshold):
    numbers = []
    for number in grades:
        if number > threshold:
            numbers.append(number)
    return numbers


a = [10, 20, 30, 70, 90]
b = [50, 70, 40, 90, 67]

print(f_p_g(a, 50))
print(f_p_g(b, 50))



        