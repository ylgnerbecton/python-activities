# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.1
x=1
while x<=100:
    print(x)
    x = x + 1

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.2
x=50
while x<=100:
    print(x)
    x = x + 1

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.3
x=10
while x>=0:
    print(x)
    x = x - 1
print("Fogo!")

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.4
fim=int(input("Digite o ultimo numero a imprimir:"))
x = 0
while x <= fim:
    print(x)
    x = x + 3

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.5
x = 10
while x <= 30:
    print(x)
    x = x + 3

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.6
n = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print("%d x %d = %d" % (n, x, n*x) )
    x = x + 1

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.7
n = int(input("Tabuada de:"))
inicio = int(input("De:"))
fim = int(input("Ate:"))
x = inicio
while x <= fim:
    print("%d x %d = %d" % (n, x, n*x) )
    x = x + 1

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.8
p = int(input("Primeiro numero:"))
s = int(input("Segundo numero:"))
x = 1
r = 0
while x <= s:
    r = r + p
    x = x + 1
print("%d x %d = %d" % (p,s,r)

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.9
dividendo = int(input("Dividendo:"))
divisor = int(input("Divisor:"))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print("%d / %d = %d (quociente) %d (resto)" % (dividendo,divisor,quociente,resto))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.10
pontos = 0
questao = 1
while questao <= 3:
     resposta = input("Resposta da questao %d: " % questao)
     if questao == 1 and (resposta == "b" or resposta == "B"):
         pontos = pontos + 1
     if questao == 2 and (resposta == "a" or resposta == "A"):
         pontos = pontos + 1
     if questao == 3 and (resposta == "d" or resposta == "D"):
         pontos = pontos + 1
     questao += 1
print("O aluno fez %d ponto(s)" % pontos)

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.11
deposito = float(input("Deposito inicial: "))
taxa = float(input("Taxa de juros: "))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print ("Saldo do mes %d e de R$%5.2f." % (mes, saldo))
    mes = mes + 1
print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo - deposito))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.12
deposito = float(input("Deposito inicial: "))
taxa = float(input("Taxa de juros: "))
investimento = float(input("Deposito mensal:"))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print ("Saldo do mes %d e de R$%5.2f." % (mes, saldo))
    mes = mes + 1
print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo - deposito))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.13
divida = float(input("Divida: "))
taxa = float(input("Juros: "))
pagamento = float(input("Pagamento mensal:"))
mes = 1
if (divida * (taxa/100) > pagamento):
    print("Sua divida nao sera paga nunca, pois os juros sao superiores ao pagamento mensal.")
else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print ("Saldo da divida no mes %d e de R$%6.2f." % (mes, saldo))
        mes = mes + 1
    print ("Para pagar uma divida de R$%8.2f, a %5.2f %% de juros," % (divida, taxa))
    print ("voce precisara de %d meses, pagando um total de R$%8.2f de juros." % (mes - 1, juros_pago))
    print ("No ultimo mes, voce teria um saldo residual de R$%8.2f a pagar." % (saldo))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.14
soma = 0
quantidade = 0
while True:
    n = int(input("Digite um numero inteiro:"))
    if n==0:
        break;
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de numeros digitados:", quantidade)
print("Soma: ", soma)
print("Media: %10.2f" % (soma/quantidade))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.15
apagar = 0
while True:
    codigo = int(input("Codigo da mercadoria (0 para sair):"))
    preco = 0
    if codigo == 0:
        break;
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Codigo invalido!")
    if preco != 0:
        quantidade = int(input("Quantidade:"))
        apagar = apagar + (preco * quantidade)
print("Total a pagar R$%8.2f" % apagar)

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.16

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.17

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.18
valor = int(input("Digite o valor a pagar:"))
cedulas = 0
atual = 100
apagar = valor
while True:
     if atual <= apagar:
         apagar -= atual
         cedulas += 1
     else:
         print("%d cedula(s) de R$%d" % (cedulas, atual))
         if apagar == 0:
               break
         elif atual == 100:
            atual = 50
         elif atual == 50:
            atual = 20
         elif atual == 20:
            atual = 10
         elif atual == 10:
            atual = 5
         elif atual == 5:
            atual = 1
         cedulas = 0

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.19
valor = float(input("Digite o valor a pagar:"))
cedulas = 0
atual = 100
apagar = valor
while True:
     if atual <= apagar:
         apagar -= atual
         cedulas += 1
     else:
         if atual >=1:
            print("%d cedula(s) de R$%d" % (cedulas, atual))
         else:
            print("%d moeda(s) de R$%5.2f" % (cedulas, atual))
         if apagar <0.01:
               break
         elif atual == 100:
            atual = 50
         elif atual == 50:
            atual = 20
         elif atual == 20:
            atual = 10
         elif atual == 10:
            atual = 5
         elif atual == 5:
            atual = 1
         elif atual == 1:
            atual = 0.50
         elif atual == 0.50:
            atual = 0.10
         elif atual == 0.10:
            atual = 0.05
         elif atual == 0.05:
            atual = 0.02
         elif atual == 0.02:
            atual = 0.01
         cedulas = 0

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.20

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.21
while True:
    valor = int(input("Digite o valor a pagar:"))
    if valor == 0:
        break
    cedulas = 0
    atual = 50
    apagar = valor
    while True:
         if atual <= apagar:
             apagar -= atual
             cedulas += 1
         else:
             print("%d cedula(s) de R$%d" % (cedulas, atual))
             if apagar == 0:
                   break
             if atual == 50:
                   atual = 20
             elif atual == 20:
                   atual = 10
             elif atual == 10:
                   atual = 5
             elif atual == 5:
                   atual = 1
             cedulas = 0

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.22
while True:
    print("""

Menu
----
1 - Adicao
2 - Subtracao
3 - Divisao
4 - Multiplicacao
5 - Sair

""")
    opcao =int(input("Escolha uma opcao:"))
    if opcao == 5:
        break
    elif opcao >=1 and opcao <5:
        n = int(input("Tabuada de:"))
        x = 1
        while x<=10:
            if opcao == 1:
                print("%d + %d = %d" % (n, x, n + x))
            elif opcao == 2:
                print("%d - %d = %d" % (n, x, n - x))
            elif opcao == 3:
                print("%d / %d = %5.4f" % (n, x, n / x))
            elif opcao == 4:
                print("%d x %d = %d" % (n, x, n * x))
            x=x+1
    else:
        print("Opcao invalida!")

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.23
n = int(input("Digite um numero:"))
if n < 0:
    print("Numero invalido. Digite apenas valores positivos")
if n == 0 or n == 1:
    print("%d e um caso especial." % n)
else:
    if n == 2:
        print("2 e primo")
    elif n%2 == 0:
        print("%d nao e primo, pois 2 e o unico numero par primo." %n)
    else:
        x = 3
        while(x < n):
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            print("%d e primo" % n)
        else:
            print("%d nao e primo, pois e divisivel por %d" % (n, x))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.24
n = int(input("Digite um numero:"))
if n < 0:
    print("Numero invalido. Digite apenas valores positivos")
else:
    if n >= 1:
        print("2")
        p = 1
        y = 3
        while p<n:
            x = 3
            while(x < y):
                if y % x == 0:
                    break
                x = x + 2
            if x == y:
                print(x)
                p = p + 1
            y = y + 2

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.25
n=float(input("Digite um numero para encontrar a sua raiz quadrada: "))
b=2
while abs(n-(b*b))>0.00001:
    p=(b+(n/b))/2
    b=p
print ("A raiz quadrada de %d e aproximadamente %8.4f" % (n, p))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.26
dividendo = int(input("Dividendo:"))
divisor = int(input("Divisor:"))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print("O resto de %d / %d e %d" % (dividendo,divisor,resto))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.27
s = input ("Digite o numero a verificar, sem espacos:")
i = 0
f = len(s)-1
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print("%s e palindromo" % s)
else:
    print("%s nao e palindromo" % s)

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.28
n = int(input ("Digite o numero a verificar:"))
q = 0
while 10 ** q < n:
    q = q + 1
i = q
f = 0
nf = ni = n
pi = pf = 0
while i > f:
    pi = int(ni / (10 ** (i-1)))
    pf = nf % 10
    if pi != pf:
        break
    f = f + 1
    i = i - 1
    ni = ni - (pi * (10 ** i ))
    nf = int(nf / 10)

if pi == pf:
    print("%d e palindromo" % n)
else:
    print("%d nao e palindromo" % n)
