print('--- Iniciar jogo ---')
print('--- Você acorda na entrada de uma caverna escura ---')
nome = input('--- Qual é o seu nome? --- ')

while True:
    print(f'\n--- {nome}, você vê uma bifurcação na caverna. Para onde você quer ir? (esquerda/direita) ---')
    escolha = input('--- Digite "esquerda" ou "direita": --- ').lower()

    if escolha == 'esquerda':
        print('--- Você segue pela esquerda e encontra um monstro feroz! Reiniciando... ---')
    elif escolha == 'direita':
        print('\n--- Você segue pela direita e encontra a saída! Parabéns! ---')
        break
    
    else:
        print('--- Opção inválida. Por favor, escolha "esquerda" ou "direita". ---')

print('--- Você saiu em segurança ---')
vida_player = 120
dano_player = 25
vida_monstro1 = 60
dano_monstro1 = 15
vida_drag = 250
dano_drag1 = 55 
dano_drag2 = 35
sequela_monstro = 20
    
print('\n---  ⚠️  ALERTA! ALERTA! ALERTA!  ⚠️  ---')
print('--- Um monstro apareceu e está se aproximando! Prepare-se! ---')

while vida_player > 0 and vida_monstro1 > 0:
    print(f'--- Sua vida: {vida_player} | Vida do monstro: {vida_monstro1} ---')
    acao = input('--- O que você quer fazer? (atacar/defender) --- ')

    if acao == 'atacar':
        vida_monstro1 -= dano_player
        vida_player -= sequela_monstro
        print(f'\n--- Você atacou o monstro e causou {dano_player} de dano! Mas também levou {sequela_monstro} de dano! ---')
    elif acao == 'defender':
        vida_player -= dano_monstro1 - 5
        dano_player += 5
        print('\n--- Você se defendeu e perdeu 10 de vida! ---')
    else:
        print('\n--- Opção inválida. Por favor, escolha "atacar" ou "defender". ---')

    if vida_monstro1 <= 0:
        print('\n--- Parabéns! Você derrotou o monstro! ---')

        print(f'\n--- Vida: {vida_player} Dano: {dano_player} ---')
    elif vida_player <= 0:
        print('\n--- Você foi derrotado pelo monstro! ---')
        break
sequela = 5

vida_player -= sequela
print(f'\n--- Você sofreu uma sequela de {sequela} pontos de vida por conta da batalha. Vida restante: {vida_player} ---')

print('\n--- Você continua sua jornada e encontra um mago misterioso! ---')
print('--- O mago lhe oferece duas poções misteriosas. Qual você escolhe? (poção vermelha(1)/poção azul(2)) ---')
escolha_pocao = input('--- Você escolhe a poção vermelha ou a poção azul? --- ')

if escolha_pocao == '1':
    vida_player += 50
    print('\n--- Você bebeu a poção vermelha e recuperou 50 pontos de vida! ---')
elif escolha_pocao == '2':
    dano_player += 20
    print('\n--- Você bebeu a poção azul e aumentou seu dano em 20 pontos! ---')
else:
    print('Opção inválida. Você não bebeu nenhuma poção. ---')

print(f'\n--- Vida atual: {vida_player} | Dano atual: {dano_player} ---')

print('\n--- Você continua sua jornada e encontra um castelo abandonado! ---')
print('--- Dentro do castelo, você avista um dragão adormecido! ---')

while vida_player > 0 and vida_drag > 0:
    print(f'--- Sua vida: {vida_player} | Vida do dragão: {vida_drag} ---')
    acao_dragao = input('--- O que você quer fazer? (atacar/defender) --- ')

    if acao_dragao == 'atacar':
        vida_drag -= dano_player
        vida_player -= dano_drag1 - 30
        print(f'\n--- Você atacou o dragão e causou {dano_player} de dano! ---')
    elif acao_dragao == 'defender':
        vida_player -= dano_drag1 - 35
        print('\n--- Você se defendeu e perdeu 45 de vida! ---')
    else:
        print('\n--- Opção inválida. Por favor, escolha "atacar" ou "defender". ---')

print(f'Você sofreu um combo surpresa do dragão e perdeu {dano_drag1 - 30} de vida! ---')
vida_player -= dano_drag1 - 30

if vida_drag <= 0:
    print('\n--- Parabéns! Você derrotou o dragão! ---')
elif vida_player <= 0:
    print('\n--- Você foi derrotado pelo dragão! ---')
















