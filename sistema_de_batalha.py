import random
from time import sleep

def batalha(jogador_ataque_minimo, jogador_ataque_maximo, nome_inimigo, inimigo_ataque_minimo, inimigo_ataque_maximo):
	vida_jogador = 100
	vida_inimigo = 100
	defendendo = False

	while vida_jogador >= 0 and vida_inimigo >= 0:
		comando_invalido = False

		print(f'Jogador: {vida_jogador}\n{nome_inimigo}: {vida_inimigo}')
		print('1 - Atacar\n2 - Defender\n3 - Fugir')
		entrada_batalha = input('Digite o que fazer: ')

		if entrada_batalha == '1':
			print('Você ataca!')
			chance_erro = random.randint(0, 100)
			sleep(1)

			if chance_erro <= 75:
				dano = random.randint(jogador_ataque_minimo, jogador_ataque_maximo)
				print(f'O inimigo perdeu {dano} P.V.!')
				vida_inimigo -= dano
			else:
				print('Você errou o ataque!')

		elif entrada_batalha == '2':
			defendendo = True
			print('Você se prepara para defender.')

		elif entrada_batalha == '3':
			tentativa_fuga = random.randint(0, 100)
			sleep(1)

			if tentativa_fuga >= 75:
				print('Você fugiu!')
				break
			else:
				print('Você não conseguiu fugir.')
		else:
			print('Digite um comando válido')
			comando_invalido = True
			sleep(1)

		if comando_invalido:
			print('Até o inimigo está confuso...')
			sleep(1)
		else:
			sleep(1)
			print(f'{nome_inimigo} ataca!')
			chance_erro = random.randint(0, 100)
			sleep(1)

			if chance_erro <= 75:
				dano_inimigo = random.randint(inimigo_ataque_minimo, inimigo_ataque_maximo)

				if defendendo:
					dano_inimigo //= 2

				vida_jogador -= dano_inimigo
				print(f'Você perdeu {dano_inimigo} P.V.!')
			else:
				print(f'{nome_inimigo} errou o ataque!')

			esta_defendendo = False
		
		if vida_jogador <= 0:
			print('Você morreu')

		if vida_inimigo <= 0:
			print('Você venceu')