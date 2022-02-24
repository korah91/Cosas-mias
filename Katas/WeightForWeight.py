'''"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes:

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:''
'''
def sum_digits(number):
    number = int(number)
    if number==0:
        return 0
    if number < 10:
        return number
    return number%10 + sum_digits(number//10)

def order_weight(strng):
    if len(strng) == 0:
        return strng
    list = strng.split()
    sum_dict = {}

    for numero in list:
        suma = sum_digits(numero)
        if not suma in sum_dict:
            sum_dict[suma] = [numero]
        else:
            sum_dict[suma].append(numero)
    list = []
    for key in sum_dict:
        list.extend(sorted(sum_dict[key], key=str))
    list.sort(key = sum_digits)

    return ' '.join(list)

if __name__ == '__main__':
    print(order_weight('103 123 4444 99 2000'))
    print(order_weight('11 11 2000 10003 22 1234000 44444444 9999 123'))
    print(order_weight('2000 11 11 10003 22 123 1234000 44444444 9999'))
# 2000 11 11
# 11 11 2000
# diccionario['2'] = [2000, 11, 11]
'''
2 {
   2000
   11
   11
}
{
    11
    11
    2000
}'''
# hago un diccionario: la key es la suma y el valor es una lista con los numeros que tengan esa suma
# hago un sort para cada entrada del diccionario
