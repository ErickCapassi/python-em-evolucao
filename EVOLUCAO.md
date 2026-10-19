# Evolução dos estudos

## Etapas anteriores — consolidadas em 19/10/2026

Os códigos abaixo foram desenvolvidos antes da criação deste repositório. Esta seção resume a trajetória; as datas individuais das atividades não foram registradas.

### 1. Mini banco: decisões e repetições

Comecei com um menu para consultar saldo, depositar, resgatar e encerrar. Depois acrescentei tratamento de entradas não numéricas, validação de opções, bloqueio de valores negativos e verificação de saldo antes do saque. Pratiquei a função `exibir_menu`, `while`, `if/elif`, `continue` e `try/except`.

### 2. Cadastro de um pedido: validação

Fiz um programa que recebia nome, produto, quantidade e preço. Trabalhei a indentação e passei a repetir a pergunta quando a quantidade ou o preço eram inválidos, usando `while True`, `continue` e `break`.

### 3. Vários produtos: listas e total geral

Evoluí o cadastro para guardar produtos, quantidades e preços em três listas. Usei `append`, `for i in range(len(produtos))` e um acumulador para somar os subtotais. Também pratiquei laços aninhados para decidir se queria cadastrar outro produto.

### 4. Funções: parâmetros e retorno

Criei funções para subtotal e desconto. Entendi que os parâmetros recebem os valores passados na chamada, mesmo quando os nomes dentro e fora da função são diferentes. Depois combinei as duas funções no mesmo programa.

## 19/10/2026 — Funções: subtotal e desconto

### O que pratiquei

- Criar funções que recebem dois parâmetros.
- Retornar um resultado com `return`.
- Guardar o retorno em uma variável.
- Usar o resultado de uma função como argumento de outra.
- Ler preço, quantidade e desconto com `input`, `float` e `int`.

### Fluxo do exercício

O programa calcula o subtotal multiplicando o preço unitário pela quantidade. Depois, passa esse subtotal para a função de desconto, que retorna o preço final.

### Verificação

Preço 30, quantidade 3 e desconto 20%: subtotal 90 e preço final 72.

### Próximo desafio

Adicionar validações e tratamento de entradas inválidas. Esta primeira versão preserva a lógica do exercício enviado, com ajustes apenas de espaçamento e texto dos prompts.

## Como registrar as próximas etapas

Para cada melhoria, anotar a data, o que mudou, o conceito praticado, um exemplo testado e a próxima dificuldade a resolver. Registrar apenas atividades realmente realizadas.

## Revisão para publicação — 19/10/2026

Os códigos foram organizados com apoio de IA, preservando as estruturas usadas nos exercícios. Ajustes desta revisão:

- Mini banco: corrigido `valor <+ 0` para `valor <= 0`, bloqueando saque zero.
- Cadastro: acrescentado o prefixo `f` na segunda parte da mensagem para exibir o nome corretamente.
- Cadastro: removido `str(input(...))`, pois `input` já retorna texto; acrescentada mensagem para opções numéricas diferentes de 1 e 2.
- Ajustados espaçamento, ortografia e textos dos prompts.
- Mantidas as três listas paralelas e o laço simples de leitura do produto para que sua simplificação faça parte de uma próxima etapa.
- Mantidos parâmetros `a` e `b` e o preço inteiro no exercício isolado de desconto, como no código enviado; nomes mais claros e valores decimais ficam como melhorias futuras.

### Verificação antes da publicação

Foram executados cenários de subtotal, desconto de 0%, 20% e 100%, depósito e saque, saldo insuficiente, entradas inválidas, saque zero e pedido com dois produtos. Os arquivos também passaram por verificação de sintaxe. Isso não cobre todos os casos possíveis; as limitações conhecidas estão no README.
