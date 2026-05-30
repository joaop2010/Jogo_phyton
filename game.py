print('--- Iniciar jogo ---')
print('--- Você acorda na entrada de uma caverna escura ---')
nome = input('--- Qual é o seu nome? --- ')

while True:
    print(f'--- {nome}, você vê uma bifurcação na caverna. Para onde você quer ir? (esquerda/direita) ---')
    escolha = input('--- Digite "esquerda" ou "direita": --- ').lower()

    if escolha == 'esquerda':
        print('--- Você segue pela esquerda e encontra um monstro feroz! Reiniciando... ---')
    elif escolha == 'direita':
        print('--- Você segue pela direita e encontra a saída! Parabéns! ---')
        break
    
    else:
        print('Opção inválida. Por favor, escolha "esquerda" ou "direita".')

print('\n--- Você saiu em segurança ---')

vida_player = 120
dano_player = 30
vida_monstro1 = 60
dano_monstro1 = 15
vida_monstro2 = 90
dano_monstro2 = 30  
    
print('--- ⚠️ ALERTA! ALERTA! ALERTA! ⚠️ ---')
print('--- Um monstro apareceu e está se aproximando! Prepare-se! ---')

while vida_player > 0 and vida_monstro1 > 0:
    print(f'--- Sua vida: {vida_player} | Vida do monstro: {vida_monstro1} ---')
    acao = input('--- O que você quer fazer? (atacar/defender) --- ')

    if acao == 'atacar':
        vida_monstro1 -= dano_player
        print(f'--- Você atacou o monstro e causou {dano_player} de dano! ---')
    elif acao == 'defender':
        vida_player -= dano_monstro1
        dano_player += 5
        print('--- Você se defendeu e perdeu 10 de vida! ---')
    else:
        print('Opção inválida. Por favor, escolha "atacar" ou "defender".')

    if vida_monstro1 <= 0:
        print('--- Parabéns! Você derrotou o monstro! ---')

        vida_player += 15
        dano_player += 5
        print(f'--- Vida aumentada: {vida_player} Dano aumentado: {dano_player} ---')
    elif vida_player <= 0:
        print('--- Você foi derrotado pelo monstro! ---')
        break
sequela = 5

vida_player -= sequela
print(f'Você sofreu uma sequela de {sequela} pontos de vida por conta da batalha. Vida restante: {vida_player}')







