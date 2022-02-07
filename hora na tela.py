s1_inicial = int(input('Deseja iniciar que horas'))
s2_final = int(input('Deseja terminar que horas'))
while s1_inicial > s2_final or s1_inicial < 0 or s2_final > 23 or s2_final < 0 or s2_final > 23:
    s1_inicial = int(input('Quer começar que horas:'))
    s2_final = int(input('Quer começar terminar que  horas:'))
for h in range(s1_inicial, s2_final + 1, 1):
    for m in range(0, 60, 1):
        for s in range(0, 60, 1):
            print(h, ':', m, ':', s, ':', 'h')


