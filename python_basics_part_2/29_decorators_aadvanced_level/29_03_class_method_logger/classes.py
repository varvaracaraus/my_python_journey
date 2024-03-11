from decorator import log_methods


@log_methods("%b %d %Y — %H:%M:%S")
class A:
    """ Class A with the method test_sum_1. """

    def test_sum_1(self) -> int:
        """ Performs the calculation of the sum of squares of numbers. """
        print('Here is the method test_sum_1.')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    """ Class B, inheriting from class A, with an additional method test_sum_2. """

    def test_sum_1(self) -> None:
        """ Overrides the test_sum_1 method of class A and adds additional actions. """
        super().test_sum_1()
        print("Here is the method test_sum_1 of the inheritor.")

    def test_sum_2(self) -> int:
        """ Performs the calculation of the sum of squares of numbers with a different initial value. """
        print("Here is the method test_sum_2 of the inheritor.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result
