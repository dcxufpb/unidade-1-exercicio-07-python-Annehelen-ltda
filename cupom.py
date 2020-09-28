# coding: utf-8

def isEmpty(value:str) -> bool:
        return (value == None) or (len(value) == value.count(" "))
def dados_loja_param(nome_loja, logradouro, numero, complemento, bairro,
                     municipio, estado, cep, telefone, observacao, cnpj,
                     inscricao_estadual):
    # Implemente aqui
    if (isEmpty(nome_loja)):
        raise Exception("O campo nome da loja é obrigatório")
    if (isEmpty(logradouro)):
        raise Exception("O campo logradouro do endereço é obrigatório")
    if (numero == 0):
        numero = ("s/n")
    if(isEmpty(cnpj)):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (isEmpty(municipio)):
        raise Exception("O campo município do endereço é obrigatório")
    if (isEmpty(estado)):
        raise Exception("O campo estado do endereço é obrigatório")
    if (isEmpty(inscricao_estadual)):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

    part2 = f"{logradouro}, {numero}"
    if not isEmpty (complemento):
        part2 += f" {complemento}"
    part3 = str()
    if not isEmpty (bairro):
        part3 += f"{bairro} - "
    part3 += f"{municipio} - {estado}"
    part4 = str()
    if not isEmpty (cep):
        part4 = f"CEP:{cep}"
    if not isEmpty(telefone):
        if not isEmpty(part4):
            part4 += " "
        part4 += f"Tel {telefone}"     
    if not isEmpty(part4):
        part4 += "\n"
    part5 = str()
    if not isEmpty(observacao):
        part5 += f"{observacao}"
    
    output = f"{nome_loja}\n"
    output += f"{part2}\n"
    output += f"{part3}\n"
    output += f"{part4}"
    output += f"{part5}\n"
    output += f"CNPJ: {cnpj}\n"
    output += f"IE: {inscricao_estadual}"

    return output
