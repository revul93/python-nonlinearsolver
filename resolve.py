import numpy
def f(x):
    return (x ** 2) - numpy.log(x) - 2


def wrap_resolve(a, b, epsilon):
    if f(a) * f(b) > 0:
        print("This function can't be solved using this method")
    start = end = 0

    def domain_halving(a, b, epsilon, num_of_iteration):
        num_of_iteration += 1
        print("--- Iteration " + str(num_of_iteration) + " ---")
        print("a = " + str(a) + ", b = " + str(b)) 
        if f(a) > 0:
            start = a
            end = b
        else:
            start = b
            end = a

        guess = (start + end) / 2
        print("guess = " + str(guess))
        print ("f(" + str(guess) + ") = " + str(f(guess)))
        if abs(f(guess)) < epsilon:
            print("THE ANSWER IS: " + str(guess))
            return guess
        else:
            if f(guess) > 0:
                start = guess
            else:
                end = guess
            return domain_halving(start, end, epsilon, num_of_iteration)

    def cutters(a, b, epsilon, num_of_iteration):
        num_of_iteration += 1
        print("--- Iteration " + str(num_of_iteration) + " ---")
        print("a = " + str(a) + ", b = " + str(b)) 
        if f(a) > 0:
            start = a
            end = b
        else:
            start = b
            end = a

        guess = ((start * f(end))-(end * f(start))) / (f(end) - f(start)) 
        print("guess = " + str(guess))
        print ("f(" + str(guess) + ") = " + str(f(guess)))
        if abs(f(guess)) < epsilon:
            print("THE ANSWER IS: " + str(guess))
            return guess
        else:
            if f(guess) > 0:
                start = guess
            else:
                end = guess
            return domain_halving(start, end, epsilon, num_of_iteration)

    print("**** DOMAIN HALVING *****")
    domain_halving(a, b, epsilon, 0)

    print("\n**** CUTTERS ****")
    cutters(a, b, epsilon, 0)
