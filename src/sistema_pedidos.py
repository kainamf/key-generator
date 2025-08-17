import json
import os
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class SistemaPedidos:
    def __init__(self, arquivo_pedidos="pedidos.json"):
        self.arquivo_pedidos = arquivo_pedidos
        self.data_atual = datetime.now().date()
        self.pedidos = self._carregar_pedidos()

    def _carregar_pedidos(self):
        if os.path.exists(self.arquivo_pedidos):
            with open(self.arquivo_pedidos, "r") as f:
                dados = json.load(f)
                if dados["data"] == str(self.data_atual):
                    return dados["pedidos"]
        return []

    def _salvar_pedidos(self):
        dados = {
            "data": str(self.data_atual),
            "pedidos": self.pedidos
        }
        with open(self.arquivo_pedidos, "w") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def _gerar_senha(self):
        agora = datetime.now()
        senha_base = int(f"{agora.hour:02d}{agora.minute:02d}")
        senha = senha_base
        senhas_existentes = {p["senha"] for p in self.pedidos}
        while senha in senhas_existentes:
            senha += 1
        return senha

    def novo_pedido(self, conteudo: dict):
        senha = self._gerar_senha()
        pedido = {
            "senha": senha,
            "hora": datetime.now().strftime("%H:%M:%S"),
            "conteudo": conteudo
        }
        self.pedidos.append(pedido)
        self._salvar_pedidos()
        return pedido

    def exibir_painel(self, pedido):
        console.clear()
        console.print(
            Panel.fit(f"[bold yellow]{pedido['senha']}[/bold yellow]",
                      title="[bold green]Senha Atual[/bold green]",
                      width=30)
        )

        tabela = Table(title="Últimos Pedidos")
        tabela.add_column("Senha", justify="center")
        tabela.add_column("Itens", justify="left")
        tabela.add_column("Valor", justify="right")

        for p in sorted(self.pedidos, key=lambda x: x["senha"], reverse=True)[:5]:
            itens = ", ".join(p["conteudo"].get("itens", []))
            valor = f"R$ {p['conteudo'].get('valor', 0):.2f}"
            tabela.add_row(str(p["senha"]), itens, valor)

        console.print(tabela)
