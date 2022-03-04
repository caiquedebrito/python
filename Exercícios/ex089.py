boletin = list()
alunos = list()
notas = list()

while True:
	nome = str(input('Nome: '))
	n1 = float(input('Nota 1: '))
	n2 = float(input('Nota 2: '))
	notas.append(n1)
	notas.append(n2)
	alunos.append(nome)
	alunos.append((n1+n2)/2)
	alunos.append(notas[:])
	boletin.append(alunos[:])
	notas.clear()
	alunos.clear()
	res = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
	if res == 'N':
		break

print('-='*15)
print(f'{"Boletin Escolar"}')
print('=-'*15)
print(f"{'N°':<5}{'Aluno':<20} Média")
print('--'*20)
for p, aluno in enumerate(boletin):
	print(f"{p:<5}{aluno[0]:<20} {aluno[1]}")
	print('--'*20)
	
while True:
	Notas = int(input('Mostrar notas de qual aluno [N°] (999 para sair): '))
	if Notas == 999:
		break
	print(f'Notas de {boletin[Notas][0]}: {boletin[Notas][2]}')
	
print('>>>>>Finalizando<<<<<<')
	
	
