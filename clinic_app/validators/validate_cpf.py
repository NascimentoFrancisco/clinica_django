from django.core.exceptions import ValidationError

def digit_generator(cpf: str, weight: int) -> int:
    sum_of_digits = 0
    
    for i in range(weight - 1):
        sum_of_digits += int(cpf[i]) * weight
        weight -= 1

    digit = 11 - (sum_of_digits % 11)

    if digit > 9:
        return 0
    
    return digit


def cpf_validate(cpf: str) -> None:

    if len(cpf) != 11 or cpf == (cpf[0] * 11):
        raise ValidationError('O CPF deve conter 11 números e que não sejam todos iguais!', 'invalid')
    
    penultimate_digit = digit_generator(cpf, weight=10)
    last_digit = digit_generator(cpf, weight=11)

    if cpf[9:] != f'{penultimate_digit}{last_digit}':
        raise('CPF inválido!', 'invalid')

