import os

from time import sleep

import random

#projeto de conta bancaria

#atributos: nome, saldo

#métodos: mostrar saldo, sacar, depositar

#histórico de deposito e saque

#taxas para saque

#limite o saque após sacar o valor x

#trasnferencias entre contas

class ContaBancaria:

    def __init__(self, nome, saldo, carteira, xp):

        self.nome = nome

        self.saldo = saldo

        self.historicSaqs = [ ]

        self.historicDep = [ ]

        self.historicGast = [ ]

        self.carteira = carteira

        self.xp = xp

    def mostrar_saldo(self):

         print(f"\nSaldo de {self.nome}: {vrd}${self.saldo:.1f}{rt}\n")

         print(f"XP: {bl}{self.xp}{rt}")

         print(f"\nNa carteira: {vrd}${self.carteira:.1f}{rt}")

    def sacar(self, saque):

        if saque > self.saldo:

            print("Você não tem isso tudo!")

        else:

            print(f"Você sacou ${saque}")

            #print(f"Com as taxas: ${taxa:.1f}")

            self.saldo -= saque

            self.carteira += saque

            self.mostrar_saldo()

            self.historicSaqs.append(saque)

    def depositar(self, deposito):

        if deposito > 1+self.carteira:

            print(f"Você não tem {deposito} na carteira!")

        else:

            print(f"Você depositou ${deposito}")

            self.saldo += deposito

            self.carteira -= deposito

            self.mostrar_saldo()

            self.historicDep.append(deposito)

    def historico(self):

        print(f"Historico de {self.nome}\n")

        print("\nSaques:")

        for saqs in self.historicSaqs:

            print(f"+ ${saqs}")

        print("\nDepósitos:")

        for dep in self.historicDep:

            print(f"= ${dep}") 

        print("\nGastos:")

        for gasts in self.historicGast:

            print(f"- ${gasts}")      

    def trans(self, nome_trans, transido):

        nome.saldo += transido

        self.saldo -= transido

        print(f"\n{self.nome} transferiu {transido}$ para {nome_trans.nome}")   

        self.mostrar_saldo()    

        nome.mostrar_saldo()

    def func_loja(self, item_loja):   

        self.carteira -= itens[f"preço{item_loja}"]

        self.historicGast.append(itens[f"preço{item_loja}"])

    def emprego(self):

        os.system("clear")

        print(f"Lista de empregos:               {bl}XP: {self.xp}{rt}\n") 

        print(f"1 — {estudante}                    \n2 — {frontend}      \n3 — {freelancer}              \n4 — {backend}      \n5 — {fullstack}    ")  

    def checar_preco(self):

        if itens[f"preço{item_loja}"] > self.carteira:

            #os.system("clear")

            print("Você não tem $", itens[f"preço{item_loja}"], "na carteira!")

        else:

            main.func_loja(item_loja)

    def estudos(self):

        os.system('clear')

        print(f"Você estudou {bl}{aleatorio}{rt} durante a noite e adquiriu 1xp!")

        self.xp += 1

        print(f"\nXP atual:\n— {self.xp}")

    def trabaio(self, empresa, ocupacao, acoes):

        os.system("clear")

        print(f"Você trabalhou para {bl}{empresa}{rt} como um programador {bd}{ocupacao}{rt} fazendo {acoes} e obteve {vrd}${ganho}{rt}")

rt = "\033[0;0m"

bd  = "\033[;1m"

rs = "\033[;7m"

bl  = "\033[1;34m"

vrd = "\033[0;32m"

itens = {1: "Banana", "preço1": 5,

         2: "Bujão de gás", "preço2": 70,

         3: "Coca latão", "preço3": 10}

range = range(1, 6)

ganho = 0

emprego_choose = 0

empresa = "site do lucas"

estudante = f"Estudante                      {bl}1xp{rt}"

frontend = f"Program. Frontend (5xp)        {vrd}$50{rt}"

freelancer = f"Freelancer (10xp)              {vrd}$80{rt}"

backend = f"Program. Backend (15xp)        {vrd}$110{rt}"

fullstack = f"Program. Fullstack (20xp)      {vrd}$150{rt}"

saldo = 0

while True:

    try:

        os.system("clear")

        nome = str(input("Digite seu nome:\n"))

        testar = nome[0]

        os.system("clear")

        break

    except:

        os.system("clear")

        print("Digite algo!")

        sleep(2)

        continue

main = ContaBancaria(nome, saldo, 0, 0)

cb1 = ContaBancaria("Muriel", 0, 0, 0)

banana = "Banana $5.00(1)"

bujao = "Butijão gaseificado $70.00(2)"

latao = "Coca lãtão $10.00(3)"

while True:

    while True:

        try:

            os.system('clear')

            main.mostrar_saldo()

            print("\n")

            print("Selecione seu método:")

            print("Dinheiro(1)")

            print("Trabalho(2)")

            print("Informações(3)")

            escolha = int(input())

            os.system("clear")

            break

        except:

            os.system("clear")

            print("Digite um número dentro de 1 e 2")

            sleep(2)

            os.system("clear")

            continue

    if escolha == 1:

            while True:

                try:             

                    print(10*"- ", "Dinheiro ", 10*"- ")

                    print("Mostrar saldo(1)")

                    print("Sacar(2)")

                    print("Depositar(3)")

                    print("Histórico(4)")

                    print("Comprar(5)")

                    print("Sair(enter)")

                    metodo = input()

                    teste = len(int(metodo))

                    continue

                    os.system("clear")

                except:

                    break

                    print("oxi")

            if metodo == "1":

                os.system("clear")

                main.mostrar_saldo()

                sleep(2.5)

                input(f"\n\n{rs}{bd}(enter){rt}\n")

            elif metodo == "2":

                while True:

                    try:

                        os.system("clear")

                        saque = float(input(f"Selecione quanto sacarás de {main.saldo:.1f}\n\n(enter para sair)\n\n"))

                        os.system("clear")

                        main.sacar(saque)

                        sleep(2.5)

                        input(f"\n\n{rs}{bd}(enter){rt}\n")

                        break

                    except:

                        break

            elif metodo == "3":

                while True:

                    try:

                        os.system("clear")

                        deposito = float(input(f"Selecione quanto depositará de {main.carteira:.1f}\n\n(enter para sair)\n\n"))

                        os.system("clear")

                        main.depositar(deposito)

                        sleep(2.5)

                        input(f"\n\n{rs}{bd}(enter){rt}\n")

                        break

                    except:

                        break

            elif metodo == "4":

                os.system("clear")

                main.historico()

                sleep(2.5)

                input(f"\n\n{rs}{bd}(enter){rt}\n")

            elif metodo == "5":

                while True:

                    os.system("clear")

                    print("Itens da loja :D\n>>>>>>>>>>>>>>>>\n\n(eles não ajudam em nada, é so um addcional)\n")

                    print(f"{banana}\n{bujao}\n{latao}\n\nDigite enter para sair")

                    try:

                        item_loja = int(input())

                        if int(item_loja) > 3 or int(item_loja) < 1:

                            print("Selecione um número entre 1 e 3")

                            continue

                        else: 

                            if itens[f"preço{item_loja}"] > 1+main.carteira:

                                os.system("clear")

                                print("Você não tem $", itens[f"preço{item_loja}"], "na carteira!")

                                sleep(1)

                                input(f"\n\n{rs}{bd}(enter){rt}\n")

                            else:

                                os.system("clear")                     

                                if int(item_loja) == 1:

                                    if banana == "— Banana adquirido! —":

                                        print("Você já comprou isso!")

                                    else:

                                        banana = "— Banana adquirido! —"   

                                        main.func_loja(item_loja)  

                                        print(itens[item_loja] + " adquirido!")              

                                elif int(item_loja) == 2:

                                    if bujao == "— Bujão adquirido! —":

                                        print("Você já comprou isso!")

                                    else: 

                                        bujao = "— Bujão adquirido! —"   

                                        main.func_loja(item_loja)   

                                        print(itens[item_loja] + " adquirido!")         

                                elif int(item_loja) == 3:

                                    if latao == "— Latão dquirido! —":

                                        print("Você já comprou isso!")

                                    else:

                                        latao = "— Latão dquirido! —"

                                        main.func_loja(item_loja)  

                                        print(itens[item_loja] + " adquirido!") 

                                else:

                                    pass

                                sleep(1)

                                input(f"\n\n{rs}{bd}(enter){rt}\n")                                

                                break

                    except ValueError:

                        break

                        print("oi")

    elif escolha == 2:

        while True:

            try:

                print(10*"- ", "Trabalho", 10*" -")

                print("Selecionar ocupação(1)")

                print("Trabalhar(2)")

                print("Sair(enter)")

                metodoem = input()

                break

            except:

                print("Digite algo entre 1 e 2")

                continue

        if metodoem == "1":

            while True:

                try:

                    main.emprego()

                    emprego_choose = int(input())

                    os.system("clear")

                    break

                except ValueError:

                    print("Digite algo entre 1 e 5")

                    sleep(1.5)

                    os.system('clear')

               #estudante

            if emprego_choose == 1:

                if estudante == "Estudante (atual)":

                    print("Você já é um estudante!")

                else:

                    print("Você agora é um estudante!!!!")

                    estudante = f"Estudante (atual)              {bl}1xp{rt}"     

                    ganho = ganho

              #fronten

            elif emprego_choose == 2:

                if main.xp < 5:

                    print("Sua experiência como estudante ainda não é igual á 5")

                else:

                    print("Você agora é um programador frontend!!!")

                    frontend = f"Programador frontend (atual)   {vrd}$50{rt}"

                    freelancer = f"Freelancer (10xp)              {vrd}$80{rt}"

                    backend = f"Program. Backend (15xp)        {vrd}$110{rt}"

                    fullstack = f"Program. Fullstack (20xp)      {vrd}$150{rt}"

                    empresa = "site do lucas"

                    ganho = 50

                    ocupacao = "Frontend"

                    acoes_choose = ["telas de login", "uma tela inicial", "uma scrollbar decente"] if main.xp < 10 else ["uma animação de tela", "uma transição de divs", "uma tela inicial animada"]

               #freelancer

            elif emprego_choose == 3:

                if main.xp < 10:

                    print("Sua experiência como estudante não é igual á 10")

                else:

                    print("Você agora é um Freelancer!!!")

                    freelancer = f"Freelancer (atual)             {vrd}$80{rt}"

                    frontend = f"Program. Frontend (5xp)        {vrd}$50{rt}"

                    backend = f"Program. Backend (15xp)        {vrd}$110{rt}"

                    fullstack = f"Program. Fullstack (20xp)      {vrd}$150{rt}"

                    ganho = 80

                    ocupacao = "Freelancer"

                    acoes_choose = ["um mini game", "uma tela interativa"]

            elif emprego_choose == 4:

                if main.xp < 15:

                    print("Sua experiência como estudante não é igual á 15")

                else:

                    print("Você agora é um programador backend!!!")

                    backend = f"Backend (atual)                {vrd}$110{rt}"

                    frontend = f"Program. Frontend (5xp)        {vrd}$50{rt}"

                    freelancer = f"Freelancer (10xp)              {vrd}$80{rt}"

                    fullstack = f"Program. Fullstack (20xp)      {vrd}$150{rt}"

                    ganho = 110

                    ocupacao = "Backend"

                    acoes_choose = ["uma tela responsiva", "um armazenador de dados", "uma calculadora de informaçoes"]

            elif emprego_choose == 5:

                if main.xp < 20:

                    print("Sua experiência como estudante não é igual á 20")

                else:

                    print("Você agora é um programador FULLSTACK!!!")

                    fullstack = f"Fullstack (atual)              {vrd}$150{rt}"

                    frontend = f"Program. Frontend (5xp)        {vrd}$50{rt}"

                    freelancer = f"Freelancer (10xp)              {vrd}$80{rt}"

                    backend = f"Program. Backend (15xp)        {vrd}$110{rt}"

                    ganho = 150

                    ocupacao = "Fullstack"

                    acoes_choose = ["uma interface completamente funcional", "uma automação de dados"]

            else:

                continue

            sleep(0.5)

            input(f"\n\n{rs}{bd}(enter){rt}\n")

        elif metodoem == "2":

                if emprego_choose in range:

                    while True:

                        try:

                            os.system("clear")

                            print("Estudar por 1xp (1)\n")        

                            print(f"Trabalhar por ${ganho} (2)")

                            ocup = int(input())

                            if ocup > 2 or ocup < 1:

                                print("Selecione apenas uma das 2 opçoes!")

                                sleep(1)

                                input(f"\n\n{rs}{bd}(enter){rt}\n")

                            else:

                                break

                        except:

                            os.system("clear")

                            print("Selecione sua meio de ocupação!")

                            sleep(1)

                            continue

                    if ocup == 1:

                        estudos = ["logica da programação", "funcionamento de banco de dados", "como centralizar uma div", "propriedades do css"]

                        aleatorio = random.choice(estudos)

                        main.estudos()   

                        sleep(1)

                        input(f"\n\n{rs}{bd}(enter){rt}\n")

                    elif ocup == 2:

                        if ganho == 0:

                            os.system("clear")

                            print("Você não possui um trabalho!\nSelecione um na lista passada com os XP necessários!")

                        else:

                            locais = ["de uma pizzaria", "de uma hamburgueria", "do lucas"]

                            if main.xp > 19:

                                locais = ["do google", "da apple", "da tesla"]

                            elif main.xp > 14:

                                locais = ["do mercado livre", "da shoppe"]

                            elif main.xp > 9:

                                locais = ["do ifood", "de um empresario"]    

                            local = random.choice(locais)

                            empresa = f"o site {local}"

                            acoes = random.choice(acoes_choose)

                            main.trabaio(empresa, ocupacao, acoes)

                            main.saldo += ganho

                            print("\nSaldo: ")

                            print(int(main.saldo))

                            print("\nCarteira: ")

                            print(int(main.carteira))

                            main.historicSaqs.append(ganho)

                        sleep(1)

                        input(f"\n\n{rs}{bd}(enter){rt}\n")

                else:

                    os.system("clear")

                    print("Você não possui nenhuma ocupação nenhuma ocupação")

                    sleep(1)

                    input(f"\n\n{rs}{bd}(enter){rt}\n")

                    os.system("clear")

    elif escolha == 3:

          basco = "Simulador básico experimental\nFiz como um meio de estudo sobre classes python.\n\nComo funciona:\n"

          while True:

              print(basco)

              duvida = input("Qual sua dúvida?\nDinheiro(1)\nTrabalho(2)\nSair(enter)\n")

              os.system("clear")

              print(basco)

              try:

                  if int(duvida) == 1:

                      duvida_dinheiro = input("Mostrar saldo(1)\nSacar(2)\nDepositar(3)\nHistórico(4)\nComprar(5)\n")

                      os.system("clear")

                      print(basco)

                      if int(duvida_dinheiro) == 1:

                          print("Com essa opção você vê seu saldo, dinheiro na carteira e XP.")

                      elif int(duvida_dinheiro) == 2:

                          print("Você seleciona a quantidade de dinheiro que deseja retirar do seu saldo e passar para sua carteira.")

                      elif int(duvida_dinheiro) == 3:

                          print("Você deposotita o valor que definir da sua carteira de volta para seu saldo.")

                      elif int(duvida_dinheiro) == 4:

                          print("Funcional, serve para mostrar as transições feitas pelo seu dinheiro. Mostra os saques e salário ná primeira linha, seus depósitos na segunda e seu dinheiro gasto em compras.")

                      elif int(duvida_dinheiro) == 5:

                          print("Não muito necessário, pois não agrega á nada. Compras básicas e aleatórias. Você precisa sacar o seu dinheiro antes de comprar para assim então poder gastar de sua carteira.")

                  elif int(duvida) == 2:

                      duvida_trabajo = input("Selecionar ocupação(1)\nTrabalhar(2)\n")

                      os.system("clear")

                      print(basco)

                      if int(duvida_trabajo) == 1:

                          print("Você terá uma lista de ocupações, cuja tais irão lhe beneficiar financeiramente, porém, antes de engressar no seu trabalho, você precisa adquirir xp's através do estudo.")

                          print("Cada estudo lhe dará 1xp. O xp requisitado para cada profissão aparece após á própria profissão, em seguida o valor ganho pelo trabalho.")

                      elif int(duvida_trabajo) == 2:

                          print("Você pode estudar por 1 xp(depois de selecionar sua ocupação de estudante), xp\nesse que é necessário para ser um profissional de sucesso.\nVocê também pode trabalhar, após conseguir uma profissão nova, ganhando seu salário\ne progredindo. Viva o capitalismo (zoando).")

                  input(f"\n\n{rs}{bd}(enter){rt}\n")

                  os.system("clear")

              except ValueError:

                    break
