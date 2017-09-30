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
fim=int(input("Digite o último número a imprimir:"))
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
fim = int(input("Até:"))
x = inicio
while x <= fim:
    print("%d x %d = %d" % (n, x, n*x) )
    x = x + 1

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.8
p = int(input("Primeiro número:"))
s = int(input("Segundo número:"))
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
questão = 1
while questão <= 3:
     resposta = input("Resposta da questão %d: " % questão)
     if questão == 1 and (resposta == "b" or resposta == "B"):
         pontos = pontos + 1
     if questão == 2 and (resposta == "a" or resposta == "A"):
         pontos = pontos + 1
     if questão == 3 and (resposta == "d" or resposta == "D"):
         pontos = pontos + 1
     questão += 1
print("O aluno fez %d ponto(s)" % pontos)
       
# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.11
depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))
    mês = mês + 1
print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo-depósito))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.12
depósito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
investimento = float(input("Depósito mensal:"))
mês = 1
saldo = depósito
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print ("Saldo do mês %d é de R$%5.2f." % (mês, saldo))
    mês = mês + 1
print ("O ganho obtido com os juros foi de R$%8.2f." % (saldo-depósito))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.13
dívida = float(input("Dívida: "))
taxa = float(input("Juros (Ex.: 3 para 3%): "))
pagamento = float(input("Pagamento mensal:"))
mês = 1
if (dívida * (taxa/100) > pagamento):
    print("Sua dívida não será paga nunca, pois os juros são superiores ao pagamento mensal.")
else:
    saldo = dívida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print ("Saldo da dívida no mês %d é de R$%6.2f." % (mês, saldo))
        mês = mês + 1
    print ("Para pagar uma dívida de R$%8.2f, a %5.2f %% de juros," % (dívida, taxa))
    print ("você precisará de %d meses, pagando um total de R$%8.2f de juros." % (mês-1, juros_pago))
    print ("No último mês, você teria um saldo residual de R$%8.2f a pagar." % (saldo))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.14
soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro:"))
    if n==0:
        break;
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print("Média: %10.2f" % (soma/quantidade))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.15
apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair):"))
    preço = 0
    if código == 0:
        break;
    elif código == 1:
        preço = 0.50
    elif código == 2:
        preço = 1.00
    elif código == 3:
        preço = 4.00
    elif código == 5:
        preço = 7.00
    elif código == 9:
        preço = 8.00
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade:"))
        apagar = apagar + (preço * quantidade)
print("Total a pagar R$%8.2f" % apagar)

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.16

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.17

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.18
valor = int(input("Digite o valor a pagar:"))
cédulas = 0
atual = 100
apagar = valor
while True:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         print("%d cédula(s) de R$%d" % (cédulas, atual))
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
         cédulas = 0

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.19
valor = float(input("Digite o valor a pagar:"))
cédulas = 0
atual = 100
apagar = valor
while True:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         if atual >=1:
            print("%d cédula(s) de R$%d" % (cédulas, atual))
         else:
            print("%d moeda(s) de R$%5.2f" % (cédulas, atual))
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
         cédulas = 0

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.20

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.21
while True:
    valor = int(input("Digite o valor a pagar:"))
    if valor == 0:
        break
    cédulas = 0
    atual = 50
    apagar = valor
    while True:
         if atual <= apagar:
             apagar -= atual
             cédulas += 1
         else:
             print("%d cédula(s) de R$%d" % (cédulas, atual))
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
             cédulas = 0

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.22
while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção =int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >=1 and opção <5:
        n = int(input("Tabuada de:"))
        x = 1
        while x<=10:
            if opção == 1:
                print("%d + %d = %d" % (n, x, n + x))
            elif opção == 2:
                print("%d - %d = %d" % (n, x, n - x))
            elif opção == 3:
                print("%d / %d = %5.4f" % (n, x, n / x))
            elif opção == 4:
                print("%d x %d = %d" % (n, x, n * x))
            x=x+1
    else:
        print("Opção inválida!")

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.23
n = int(input("Digite um número:"))
if n < 0:
    print("Número inválido. Digite apenas valores positivos")
if n == 0 or n == 1:
    print("%d é um caso especial." % n)
else:
    if n == 2:
        print("2 é primo")
    elif n%2 == 0:
        print("%d não é primo, pois 2 é o único número par primo." %n)
    else:
        x = 3
        while(x < n):
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            print("%d é primo" % n)
        else:
            print("%d não é primo, pois é divisível por %d" % (n, x))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.24
n = int(input("Digite um número:"))
if n < 0:
    print("Número inválido. Digite apenas valores positivos")
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
n=float(input("Digite um número para encontrar a sua raiz quadrada: "))
b=2
while abs(n-(b*b))>0.00001:
    p=(b+(n/b))/2
    b=p
print ("A raiz quadrada de %d é aproximadamente %8.4f" % (n, p))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.26
dividendo = int(input("Dividendo:"))
divisor = int(input("Divisor:"))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print("O resto de %d / %d é %d" % (dividendo,divisor,resto))

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.27
s = input ("Digite o número a verificar, sem espaços:")
i = 0
f = len(s)-1
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print("%s é palíndromo" % s)
else:
    print("%s não é palíndromo" % s)

# INT. PROG. PYTHON CAP. 5 | EXERCÍCIO 5.28
n = int(input ("Digite o número a verificar:"))
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
    print("%d é palíndromo" % n)
else:
    print("%d não é palíndromo" % n)