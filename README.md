# 🍔 Sistema de Senhas para Lanchonete

Este projeto é um **gerador de senhas com pedidos atrelados**, pensado para uso em lanchonetes.

## 🚀 Como funciona
- A cada pedido, o sistema gera uma **senha de 4 dígitos** (baseada em hora e minuto).
- Caso já exista uma senha igual, incrementa até encontrar uma disponível.
- O pedido (itens e valor) fica **associado à senha**.
- O sistema mantém um **histórico diário** em arquivo `pedidos.json`.

## 🖥 Exemplo de uso
```bash
python src/main.py
Digite um pedido no formato JSON:

{"itens": ["X-Burger", "Batata"], "valor": 32.50}
Saída no painel:

[ SENHA ATUAL: 1515 ]

Últimos Pedidos:
Senha   Itens                 Valor
1515    X-Burger, Batata      R$ 32.50
```

## 📂 Estrutura do projeto
```
.
├── src/
│   ├── main.py
│   └── sistema_pedidos.py
├── pedidos.json   # gerado automaticamente
├── requirements.txt
└── README.md
```

## 📦 Instalação
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gerador-senhas-lanchonete.git
cd gerador-senhas-lanchonete
```

Crie um ambiente virtual (opcional):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o sistema:

```bash
python src/main.py
```

## 🔮 Melhorias futuras
- Consulta de pedidos por senha
- Painel web para exibir chamadas de pedidos
- Integração com impressão de comprovantes
