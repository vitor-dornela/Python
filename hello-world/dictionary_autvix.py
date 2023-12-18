def maletas_possiveis(almoxarife, itens_necessarios): # recebe argumentos dos itens diponíveis no almoxarife e quanto são necessário para montar a maleta
    maletas_possiveis = float('inf')  # Inicialmente, assume-se que é possível criar um número infinito de maletas
    
    # Itera pelos itens necessários e calcula o número mínimo de maletas que podem ser criadas
    for item, quantidade_necessaria in itens_necessarios.items(): #percorre todos itens do segundo dicionário de dados (necessários)
        if item in almoxarife:  # Verifica se o item atual (do dicionário itens_necessarios) também está presente no dicionário almoxarife. 
            quantidade_disponivel = almoxarife[item]  # atribuição obtida do dicionário 'almoxarife'
            if quantidade_necessaria > 0: # evitar divisão por zero
                maletas_possiveis = min(maletas_possiveis, quantidade_disponivel // quantidade_necessaria) #calcula o número mínimo de maletas
        else:   
            # Se algum item necessário não estiver disponível no almoxarife, não é possível criar nenhuma maleta
            return 0
    
    return maletas_possiveis # retorna o valor calculado


# Exemplos de uso
print(maletas_possiveis({'furadeira': 3, 'chave': 10, 'alicate': 4, 'trena': 5},
                       {'furadeira': 1, 'chave': 2, 'alicate': 2, 'trena': 1}))  # Deve retornar 2

print(maletas_possiveis({'furadeira': 3, 'chave': 10, 'alicate': 10, 'trena': 5},
                       {'furadeira': 1, 'chave': 2, 'alicate': 2, 'trena': 1}))  # Deve retornar 3

print(maletas_possiveis({'furadeira': 100, 'chave': 100, 'alicate': 6, 'trena': 100},
                       {'furadeira': 0, 'chave': 0, 'alicate': 0, 'trena': 1}))  # Deve retornar 100

print(maletas_possiveis({'furadeira': 100, 'chave': 100, 'alicate': 0, 'trena': 100},
                       {'furadeira': 1, 'chave': 10, 'alicate': 1, 'trena': 2}))  # Deve retornar 0
