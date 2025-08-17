import json
from sistema_pedidos import SistemaPedidos

def main():
    sistema = SistemaPedidos()

    while True:
        print("\nDigite o pedido em JSON ou 'sair':")
        entrada = input().strip()

        if entrada.lower() == "sair":
            break

        try:
            conteudo = json.loads(entrada)
            pedido = sistema.novo_pedido(conteudo)
            sistema.exibir_painel(pedido)
        except json.JSONDecodeError:
            print("Entrada inválida! Digite um JSON válido.")

if __name__ == "__main__":
    main()
