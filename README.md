# Python em evolução

Repositório de estudos de **Erick Capassi**, com exercícios e pequenos projetos em Python. O objetivo é registrar meu aprendizado e as melhorias feitas nos códigos ao longo do tempo.

Estou estudando fundamentos de programação e praticando a construção de soluções simples. Os exercícios representam minha etapa atual de aprendizado.

## Exercícios disponíveis

| Exercício | O que faz | Conceitos praticados |
| --- | --- | --- |
| [Subtotal](exercicios/01_subtotal.py) | Multiplica quantidade por preço unitário | Parâmetros e retorno de funções |
| [Desconto](exercicios/02_desconto.py) | Retorna o preço após aplicar um desconto percentual | Porcentagem, variáveis locais e return |
| [Subtotal e desconto](exercicios/03_subtotal_e_desconto.py) | Usa o resultado de uma função como entrada de outra | Composição de cálculos com funções |
| [Mini banco](projetos/mini_banco.py) | Consulta saldo, faz depósitos e saques em uma simulação no terminal | Menu, condicionais, while, continue e tratamento de ValueError |
| [Cadastro de pedidos](projetos/cadastro_de_pedidos.py) | Cadastra vários produtos e exibe subtotais e total geral | Listas, append, laços aninhados, índices e acumuladores |

## Como executar

É necessário ter Python 3 instalado. Não há dependências externas.

Na pasta do projeto, execute:

```bash
python exercicios/03_subtotal_e_desconto.py
python projetos/mini_banco.py
python projetos/cadastro_de_pedidos.py
```

Dependendo do sistema, utilize `python3` ou `py` no lugar de `python`.

Exemplo: preço unitário `30`, quantidade `3` e desconto `20` resultam em subtotal `90` e preço final `72`.

Execute um comando por vez. Para valores decimais, use ponto: `29.90`.

## O que já pratiquei

- Entrada e saída de dados, conversões e cálculos.
- Decisões com `if`, `elif` e `else`.
- Repetições com `while` e `for`, incluindo `break` e `continue`.
- Validações básicas e `try/except ValueError` nos projetos.
- Listas, acesso por índice e soma de subtotais.
- Funções, parâmetros e valores retornados.

## Próximas melhorias

- [ ] Validar preço e quantidade maiores que zero.
- [ ] Validar desconto entre 0 e 100.
- [ ] Tratar entradas que não sejam números.
- [ ] Melhorar nomes de variáveis e a apresentação dos valores.
- [ ] Praticar dicionários e listas de produtos.
- [ ] Separar o cadastro de pedidos em funções.
- [ ] Simplificar os laços e padronizar os nomes das variáveis.
- [ ] Aprender a salvar e ler dados em arquivos.

Os exercícios de funções ainda não validam as entradas. Os projetos têm validações básicas, mas ainda não tratam valores especiais como `nan` e `inf`, nem nomes vazios. Os dados ficam apenas na memória e são perdidos ao encerrar. Os cálculos usam `float` para praticar fundamentos; o mini banco é uma simulação educativa. Essas limitações serão trabalhadas conforme avanço nos estudos.

## Registro do aprendizado

Veja [EVOLUCAO.md](EVOLUCAO.md) para acompanhar os conceitos praticados. O histórico de commits registrará as alterações realizadas, com mensagens que expliquem cada mudança.

Os exercícios são desenvolvidos por mim durante os estudos, com apoio de IA para explicações, revisão e organização do repositório.

Esta publicação reúne códigos já escritos nos estudos. O histórico começa na data da publicação; as etapas anteriores são descritas no registro de evolução, sem simular commits antigos.

## Perfil

- [LinkedIn](https://www.linkedin.com/in/erick-capassi)
- [GitHub](https://github.com/ErickCapassi)
