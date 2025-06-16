## 📝 Descrição

Este projeto implementa um mini sistema de arquivos simulado em Python, inspirado em sistemas de arquivos modernos como EXT4. Ele oferece operações básicas de gerenciamento de arquivos e diretórios, simulando algumas funcionalidades fundamentais de um sistema de arquivos real.

## ✨ Funcionalidades

- **Gerenciamento de diretórios**:
  - Criar diretórios (`mkdir`)
  - Navegar entre diretórios (`cd`)
  - Listar conteúdo (`ls`)

- **Operações com arquivos**:
  - Criar arquivos (`touch`)
  - Escrever conteúdo (`write`)
  - Ler conteúdo (`read`)
  - Remover arquivos (`rm`)
  - Mover/renomear (`mv`)
  - Ver metadados (`stat`)

## 🛠️ Como Executar

1. Certifique-se de ter Python instalado (versão 3.6 ou superior)
2. Copie o código para um arquivo chamado `miniExt.py`
3. Execute o programa com o comando:

```bash
python microExt.py
```

4. Use os comandos disponíveis para interagir com o sistema de arquivos simulado

## 📋 Comandos Disponíveis

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `mkdir` | Cria um novo diretório | `mkdir pasta` |
| `cd`    | Muda o diretório atual | `cd pasta` ou `cd ..` |
| `ls`    | Lista conteúdo do diretório | `ls` |
| `touch` | Cria um novo arquivo vazio | `touch arquivo.txt` |
| `write` | Escreve conteúdo em um arquivo | `write arquivo.txt "conteúdo"` |
| `read`  | Lê o conteúdo de um arquivo | `read arquivo.txt` |
| `rm`    | Remove um arquivo | `rm arquivo.txt` |
| `mv`    | Move/renomeia um arquivo | `mv antigo.txt novo.txt` |
| `stat`  | Mostra metadados de um arquivo | `stat arquivo.txt` |
| `exit`  | Sai do programa | `exit` |

## 🧠 Estrutura Interna

O sistema simulado mantém as seguintes estruturas de dados:

- `current_dir`: Armazena o diretório atual
- `directories`: Dicionário que representa a hierarquia de diretórios
- `files`: Dicionário que armazena os arquivos e seus metadados:
  - `content`: Conteúdo do arquivo
  - `created`: Data de criação
  - `modified`: Data de modificação
  - `size`: Tamanho em bytes

## 🚀 Melhorias Futuras

1. Implementar permissões de arquivos (leitura/escrita/execução)
2. Adicionar suporte a links simbólicos
3. Implementar journaling para recuperação após falhas
4. Adicionar sistema de logs para operações
5. Implementar alocação de blocos com estratégias diferentes
6. Adicionar compactação de arquivos

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores

[Ravi Freitas e Roberto Xavier]

---

**Disciplina**: Projeto de Sistemas Operacionais (T303)  
**Professor**: MSc. Felipe Jucá dos Santos  
**Instituição**: [Universidade de Fortaleza]  
**Data**: [16/06/2025]