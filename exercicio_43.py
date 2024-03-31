print("Validador de CPF: Implemente um programa que valide um CPF com base nos dígitos verificadores.\n")

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    
    if len(cpf) != 11:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito < 10 else 0
    
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10) % 11
    segundo_digito = segundo_digito if segundo_digito < 10 else 0
    
    return cpf[-2:] == f"{primeiro_digito}{segundo_digito}"

cpf_teste = "123.456.789.09"
print(f"O CPF {cpf_teste} é valido?", validar_cpf(cpf_teste))
