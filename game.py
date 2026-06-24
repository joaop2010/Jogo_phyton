import random

print('--- Bem-vindo ao jogo... A LENDA DO HERÓI! ---')
print('')
print('--- Iniciar jogo ---')
print('')
print('--- Você acorda na entrada de uma caverna escura ---')
nome = input('--- Qual é o seu nome? --- ')
print('')
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
print('')
print('--- Você saiu em segurança ---')
vida_player = 120
dano_player = 25
vida_monstro1 = 60
dano_monstro1 = 15
vida_drag = 200
dano_drag1 = 40
sequela_monstro = 10
print('')    
print('\n---  ⚠️  ALERTA! ALERTA! ALERTA!  ⚠️  ---')
print('--- Um monstro apareceu e está se aproximando! Prepare-se! ---')
print('')
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
vida_player += 15
dano_player += 10
vida_player -= sequela
print(f'\n--- Você sofreu uma sequela de {sequela} pontos de vida por conta da batalha. Vida restante: {vida_player} ---')

print('\n--- Você continua sua jornada e encontra um mago misterioso! ---')
print('')
print('--- O mago lhe oferece duas poções misteriosas. Qual você escolhe? (poção vermelha(1)/poção azul(2)) ---')
escolha_pocao = input('--- Você escolhe a poção vermelha ou a poção azul? --- ')

if escolha_pocao == '1':
    vida_player += 70
    print('\n--- Você bebeu a poção vermelha e recuperou 70 pontos de vida! ---')
elif escolha_pocao == '2':
    dano_player += 30
    print('\n--- Você bebeu a poção azul e aumentou seu dano em 30 pontos! ---')
else:
    print('Opção inválida. Você não bebeu nenhuma poção. ---')

print(f'\n--- Vida atual: {vida_player} | Dano atual: {dano_player} ---')

print('\n--- Você continua sua jornada e encontra um castelo abandonado! ---')
print('--- Dentro do castelo, você avista um dragão adormecido! ---')

while vida_player > 0 and vida_drag > 0:
    print(f'--- Sua vida: {vida_player} | Vida do dragão: {vida_drag} ---')
    acao_dragao = input('--- O que você quer fazer? (atacar/defender) --- ')

    if acao_dragao == 'atacar':
        ataque_sorteado = random.choice(['fogo', 'garras', 'cauda'])
        print(f'O dragão usou {ataque_sorteado}!')
            
        if ataque_sorteado == 'fogo':
                dano_drag1 = 40
        elif ataque_sorteado == 'garras':
                dano_drag1 = 30
        elif ataque_sorteado == 'cauda':
                dano_drag1 = 25
        vida_drag -= dano_player
        vida_player -= dano_drag1 - 15
        print(f'\n--- Você atacou o dragão e causou {dano_player} de dano! ---')
    elif acao_dragao == 'defender':
        print("Você se defendeu! O dragão está escolhendo o ataque...")

        vida_player -= dano_drag1 - 25
        print('\n--- Você se defendeu e perdeu 15 de vida! ---')
    else:
        print('\n--- Opção inválida. Por favor, escolha "atacar" ou "defender". ---')

if vida_drag <= 0:
    print(f'\n--- Parabéns, {nome}! Você derrotou o dragão! ---')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠈⠨⠐⠅⠂⠆⡐⠄⠤⠠⠄⠄⠄⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠅⠠⢀⠂⡂⠁⠅⢈⠀⠀⡀⠀⠀⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠠⠄⡠⠅⣈⠀⠀⠀⠀⢀⢔⠀⠂⠁⠀⠐⡀⠈⢄⣀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⠀⠨⢀⠄⠊⠀⠀⠑⢄⢀⠐⠡⠂⠀⠀⡠⡡⠉⠈⠄⠈⠄⢠⠁⠀⠀⠀⠀⠀⠀⠀⡀⠂⡨⢀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡖⠄⡀⡀⣅⡀⠬⠔⠊⠀⢀⠀⠀⠀⠄⠀⠢⠨⠄⣀⠀⠐⡐⢀⠀⡀⢀⠀⠀⠑⢄⠒⠈⡂⠀⠀⠀⠀⠎⠀⡒⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠠⢀⠠⠑⠐⠈⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠘⡀⠀⠀⠀⠀⠁⠑⢠⠁⠀⠀⠁⠁⠑⠠⡀⠑⠄⣂⢀⠄⢑⠈⢂⠀⠈⠄⠃⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡄⠂⠁⠀⢀⢀⢀⠀⢀⠆⠢⡀⠀⠨⠀⠀⠀⢠⠁⠀⢀⠄⠀⠀⠀⢈⠀⠀⡐⡀⠀⠀⠀⠀⠀⠀⠀⠑⠤⢀⠂⠌⠀⠈⠀⢀⠤⠌⠢⢀⢀⠀⠀⠠⢀⠰⠠⠀')
    print('⠀⠀⡀⠄⠒⠐⠐⠐⠐⠀⠁⠁⠀⡀⠔⠈⡂⠂⠁⠂⠁⠀⠀⠈⠁⠁⠀⠀⠀⢌⠀⡌⡂⢑⠀⠀⢀⠂⡀⠔⠀⠀⠑⢐⢀⠠⠠⠄⠄⡀⠀⢠⠁⠀⠀⠄⠀⠀⠀⢀⣀⣀⠀⠠⠈⠈⠀⠁⠡⠀')
    print('⠀⠂⠄⠂⠑⠈⠂⠃⠂⠂⠐⠈⠈⠀⠀⠀⡊⡂⠅⠄⠂⠂⠁⠁⠂⠂⠂⠄⠜⠠⠠⠡⡨⠐⠈⠐⠀⢰⠐⠐⠐⢈⡈⡠⠐⠈⠈⠁⠊⠄⠅⠌⢆⠀⠀⠈⠉⡉⡡⠡⠐⠄⢌⢉⠢⠂⠆⠔⠈⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠈⠁⠁⠈⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠑⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
elif vida_player <= 0:  
    print(f'\n--- Você {nome} foi derrotado pelo dragão! ---')

    print('⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢀⢺⠅⠀⠀⠀⠀⠀⠀⢀⢀⣀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠅⠀⠀⠀⠀⢀⢰⣾⠾⢛⠳⢷⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⡀⢀⢀⠠⣿⢅⢀⢀⠀⡀⢐⡿⣡⣞⣧⣭⣷⣧⡆⡤⡂⡠⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠱⠗⠚⠚⢿⣷⣿⠛⠒⠓⠷⠐⣿⡿⣾⣵⣿⣿⣿⣯⢟⣴⣿⡿⣧⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠹⣿⣿⣽⣿⣿⣿⣱⢟⠉⡂⢅⢋⡿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢺⡿⣿⠀⠀⠀⠀⠀⠀⠙⠺⢿⣿⣿⢿⣯⣆⡶⠾⢮⣯⣾⣯⣻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣋⣾⣿⡷⢭⣯⣿⣾⣿⣿⣻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣷⣥⢀⠀⠀⠀⠀⠀⠀⠠⣼⣿⠫⠿⣿⣾⣿⣿⣿⣿⣿⣿⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣷⣕⢢⠠⣠⣰⣄⣽⣿⣃⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠙⠙⠿⣿⣿⣿⣿⣿⣿⢿⢩⡩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⡯⣿⠀⠀⠀⠈⠻⡿⢿⣿⣯⣾⣿⣿⣿⣋⣌⣻⣿⣿⣿⣿⣿⣯⣷⣶⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⣯⣗⠀⠀⠀⠀⠀⠐⣮⢨⡩⣿⣿⣿⣿⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣾⣽⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⡗⠀⠀⠀⠀⠀⠀⣿⣿⣿⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠹⣿⣟⣽⣿⣿⣟⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⡆⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡇⠀⡐⣿⣿⣿⣿⣿⣿⣿⣿⡣⡋⠃⠛⠃⠀⡀⢄⢢⣢⣢⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣯⠀⢸⡟⣿⣿⣿⣿⣿⡗⣿⢘⠠⡠⡠⣦⣵⣮⣷⣿⣿⣿⠄⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣬⣭⢿⣿⣄⠈⡀⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠇⠀⠀⠀⠀⠀⠀⡀⣀⢢⣃⣝⣿⣿⣿⣿⡔⣾⣽⣽⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠈⠉⢻⣿⣿⡇⠀⠀⠀')
    print('⢀⠠⣠⣠⣀⣀⣠⣠⣤⣽⣤⣦⣴⣴⣤⣦⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣯⣧⣦⣦⣴⣴⣤⣦⣨⣾⣿⣟⣠⣠⣀⢀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠁⠉⠈⠉⠈⠁⠉⠈⠁⠁⠉⠈⠁⠁⠁⠉⠈⠈⠈⠁⠁⠁⠉⠈⠈⠀⠀⠀⠀⠀⠀')
elif vida_player <= 0 and vida_drag <= 0:
    print(f'\n--- Você {nome} e o dragão caíram em batalha! ---')

    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠈⠨⠐⠅⠂⠆⡐⠄⠤⠠⠄⠄⠄⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠅⠠⢀⠂⡂⠁⠅⢈⠀⠀⡀⠀⠀⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠠⠄⡠⠅⣈⠀⠀⠀⠀⢀⢔⠀⠂⠁⠀⠐⡀⠈⢄⣀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⠀⠨⢀⠄⠊⠀⠀⠑⢄⢀⠐⠡⠂⠀⠀⡠⡡⠉⠈⠄⠈⠄⢠⠁⠀⠀⠀⠀⠀⠀⠀⡀⠂⡨⢀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡖⠄⡀⡀⣅⡀⠬⠔⠊⠀⢀⠀⠀⠀⠄⠀⠢⠨⠄⣀⠀⠐⡐⢀⠀⡀⢀⠀⠀⠑⢄⠒⠈⡂⠀⠀⠀⠀⠎⠀⡒⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠠⢀⠠⠑⠐⠈⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠘⡀⠀⠀⠀⠀⠁⠑⢠⠁⠀⠀⠁⠁⠑⠠⡀⠑⠄⣂⢀⠄⢑⠈⢂⠀⠈⠄⠃⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡄⠂⠁⠀⢀⢀⢀⠀⢀⠆⠢⡀⠀⠨⠀⠀⠀⢠⠁⠀⢀⠄⠀⠀⠀⢈⠀⠀⡐⡀⠀⠀⠀⠀⠀⠀⠀⠑⠤⢀⠂⠌⠀⠈⠀⢀⠤⠌⠢⢀⢀⠀⠀⠠⢀⠰⠠⠀')
    print('⠀⠀⡀⠄⠒⠐⠐⠐⠐⠀⠁⠁⠀⡀⠔⠈⡂⠂⠁⠂⠁⠀⠀⠈⠁⠁⠀⠀⠀⢌⠀⡌⡂⢑⠀⠀⢀⠂⡀⠔⠀⠀⠑⢐⢀⠠⠠⠄⠄⡀⠀⢠⠁⠀⠀⠄⠀⠀⠀⢀⣀⣀⠀⠠⠈⠈⠀⠁⠡⠀')
    print('⠀⠂⠄⠂⠑⠈⠂⠃⠂⠂⠐⠈⠈⠀⠀⠀⡊⡂⠅⠄⠂⠂⠁⠁⠂⠂⠂⠄⠜⠠⠠⠡⡨⠐⠈⠐⠀⢰⠐⠐⠐⢈⡈⡠⠐⠈⠈⠁⠊⠄⠅⠌⢆⠀⠀⠈⠉⡉⡡⠡⠐⠄⢌⢉⠢⠂⠆⠔⠈⠀')
    print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠉⠈⠁⠁⠈⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠑⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')