### 2. `cadastro-automatico-fornecedor`[cite: 2]

* **Descrição**: Sistema de automação de cadastro de fornecedores com interface gráfica e integração a APIs (Feito para o RODOPAR)[cite: 2].
* **Tecnologias**: Python, PyQt / PySide, APIs[cite: 2].
* **Ficheiros identificados**: `main.py`, `program.py`, `tela.py`, `api.py`, `tela.ui` e recursos visuais (`.png`, `.ico`)[cite: 2].

```markdown
# Cadastro Automático de Fornecedor

Ferramenta desenvolvida em Python com interface gráfica para automatizar o processo de pesquisa e registo/cadastro de fornecedores.

## Tecnologias Utilizadas

- **Python 3.x**
- **PyQt / PySide**
- **Requests / API Client**

## Estrutura do Projeto

- `main.py` / `program.py`: Ficheiros principais de execução da automação e fluxo de dados.
- `api.py`: Módulo responsável pela comunicação com os serviços de API.
- `tela.py` / `tela.ui`: Definição e componentes da interface do utilizador.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install PyQt5 requests
