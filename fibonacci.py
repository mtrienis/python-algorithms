class Fibonacci:

    def fib(self, i):

        fib_values = {1:1,2:1}

        for x in xrange(3, i+1):
            fib_values[x] = fib_values[x-2] + fib_values[x-1]

            # print fib_values
            if x == i:
                return fib_values[x]


    def fib_recursive(self, i):

        if i == 1:
            return 1
        elif i == 2:
            return 1

        return self.fib_recursive(i-2) + self.fib_recursive(i-1)

