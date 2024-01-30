
def riemann(f, a, b, n):
    interval = (b - a) / n

    widths = [a + i * interval for i in range(n)]

    areas = []
    for j in range(len(widths) - 1):
        # area = f(widths[j]) + f(widths[j+1])
        middle = (widths[j] + widths[j + 1]) / 2
        area = f(middle) * interval
        areas.append(area)
    
    return sum(areas)

def riemann2(f, a, b, n):
    interval = (b - a) / n

    area = 0
    for i in range(0, n):
        middle = ((a + i * interval) + (a + (i + 1) * interval)) / 2
        area += f(middle) * interval
    
    return area

def f(x):
    y = x**2 + 2
    return y

def g(x):
    y = x
    return y

'''
Menu to choose which exercise the user want to check
'''
def main():
    options = "1 - Calculate integral of x^2 + 2 from 1 to 2 with n subintervals\n2 - Calculate the area between x^2 + 2 and x from 1 to 2\n3 - Give three numbers that their sum is equal to n\n4 - Exit\n\nPlease, enter an option: "
    
    while True:
        option = int(input(options))

        match (option):
            case 1:
                n = int(input("Enter the number of subintervals: "))
                lim_inf = 1
                lim_sup = 2
                area = riemann2(f, lim_inf, lim_sup, n)
                print("The area under the curve of f(x) = x^2 + 2 is approximately {:.4}\n".format(area))

            case 2:
                n = int(input("Enter the number of subintervals: "))
                lim_inf = 1
                lim_sup = 2
                area = riemann2(f, lim_inf, lim_sup, n)
                area2 = riemann2(g, lim_inf, lim_sup, n)
                print("The area between f(x) = x^2 + 2 and g(x) = x is approximately {:.4}\n".format(area - area2))
            
            case 3:
                num = int(input("Enter a number: "))
            
            case _:
                another = input("Do you want to choose another option? [yes/no]: ")
                if another.lower() == "yes":
                    continue
                elif another.lower() == "no":
                    break

main()

# Example usage:
# lim_inf = 1
# lim_sup = 2
# n = 100000
# area = riemann(f, lim_inf, lim_sup, n)
# print(area)
