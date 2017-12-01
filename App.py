import LeituraEscrita
from Participante import *
import sys

def exibirMenu():
    print("\nParticipantes do Evento \n\n"
          " 1 - Listar participantes de um arquivo Json \n"
          " 2 - Adiciona participante \n"
          " 3 - Sair")

def main(args = []):

    exibirMenu()

    continuar = True

    while continuar:
        try:
            # Continuar a execução do programa.
            opcao = int(input("\nDigite a opção: "))

            if (opcao == 1):
               LeituraEscrita.listarParticipante()

            elif (opcao == 2):
               LeituraEscrita.adicionaParticipante()

            elif (opcao == 3):
               LeituraEscrita.Sair()

            elif (opcao < 1 or opcao > 3):
                print("Ops! Opção inválida!")
                print("")

        except ValueError:
            print("Ops! Digite um valor válido")

if (__name__ == "__main__"):
    main()
