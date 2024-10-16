
def confirmando_cpf(cpf):
    str_cpf = str(cpf)
    if len(str_cpf) > 11:
        print(f'cpf com {len(cpf)} digitos, cpf possui  apenas 11 digitos')
    elif len(str_cpf) < 11 :
        print(f'Erro! você digitou apenas{len(cpf)}')
    else:
        print('Cpf está correto')
    return cpf
     
cpf = input('Me fala seu cpf: ')
leia_cpf = confirmando_cpf(cpf)
