decimal_number = int(input())


def decimal_para_binario(decimal_number):
    if decimal_number == 0:
        return 0
    else:
        return (decimal_number % 2 + 10 *
                decimal_para_binario(int(decimal_number // 2)))


print(decimal_para_binario(decimal_number))
