# 🚀 Desafios Infinity School

Este repositório contém a implementação de diversos desafios de programação em Python desenvolvidos durante o curso da Infinity School. Cada desafio aborda conceitos fundamentais de programação e lógica computacional.

## 📋 Lista de Desafios

### 1. 💰 Calculadora de Notas (desafio_aula01.py)
**Objetivo:** Calcular a quantidade mínima de notas necessárias para representar um valor monetário.

**Funcionalidades:**
- Recebe um valor inteiro do usuário
- Calcula quantas notas de cada denominação (100, 50, 20, 10, 5, 2, 1) são necessárias
- Utiliza divisão inteira e operador módulo para otimizar a distribuição

**Exemplo de uso:**
```
Entrada: 1793
Saída: 17 notas de 100, 1 nota de 50, 2 notas de 20, 0 notas de 10, 0 notas de 5, 1 nota de 2, 1 nota de 1
```

### 2. 📊 Sistema de Avaliação de Alunos (desafio_aula04.py)
**Objetivo:** Gerenciar notas de alunos e calcular estatísticas da turma.

**Funcionalidades:**
- Cadastro de alunos com 3 notas cada
- Cálculo automático de média individual
- Identificação de aprovados (média ≥ 7) e reprovados
- Determinação da maior e menor média da turma
- Cálculo da média geral da turma

**Recursos implementados:**
- Loop infinito com condição de parada ("fim")
- Controle de aprovação/reprovação
- Tracking de melhor e pior desempenho

### 3. 📦 Controle de Estoque (desafio_aula04-2.py)
**Objetivo:** Sistema de gerenciamento de produtos em estoque.

**Funcionalidades:**
- Cadastro de produtos com preço unitário e quantidade
- Cálculo de valor total por produto
- Identificação do produto com maior/menor valor total em estoque
- Determinação do produto mais caro/barato unitariamente
- Cálculo do valor total do estoque
- Contagem total de itens em estoque

**Recursos implementados:**
- Validação de entrada (preço negativo encerra o programa)
- Comparações para encontrar extremos
- Acumuladores para totalizações

### 4. 📋 Desafio Complementar 1: Organização de Caixas (desafio_complementar01.py)
**Objetivo:** Otimizar o armazenamento de itens em diferentes tipos de caixas.

**Funcionalidades:**
- Calcula a distribuição ótima de itens em caixas de diferentes tamanhos
- Prioriza o uso de caixas maiores para economizar espaço
- Tipos de caixas: Grande (100 itens), Média (50 itens), Pequena (10 itens), Mini (1 item)

**Algoritmo:**
- Utiliza divisão inteira para maximizar o uso de caixas grandes
- Aplica o conceito de "algoritmo guloso" para otimização

### 5. 🔢 Desafio Complementar 2: Análise de Números (desafio_complementar01-2.py)
**Objetivo:** Extrair e analisar dígitos de um número de três dígitos.

**Funcionalidades:**
- Extração individual dos dígitos (centena, dezena, unidade)
- Cálculo da soma dos dígitos
- Demonstração de manipulação numérica com operadores matemáticos

**Conceitos aplicados:**
- Divisão inteira e módulo para extração de dígitos
- Decomposição numérica

### 6. 📞 Agenda de Contatos (agenda.py)
**Objetivo:** Sistema completo de gerenciamento de contatos.

**Funcionalidades:**
- ✅ Adicionar novos contatos
- 🔍 Pesquisar contatos existentes
- ✏️ Alterar informações de contatos
- 🗑️ Excluir contatos
- 📋 Listar todos os contatos
- 🚪 Sair do sistema

**Recursos implementados:**
- Interface de menu interativo
- Uso de dicionários para armazenamento
- Validação de entradas
- Tratamento de casos de erro (contato não encontrado)

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Conceitos fundamentais:
  - Estruturas condicionais (if/elif/else)
  - Loops (while, for)
  - Estruturas de dados (dicionários, variáveis)
  - Operadores matemáticos (divisão inteira, módulo)
  - Manipulação de strings
  - Entrada e saída de dados

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/samyllemaria/desafios_infinity_school.git
```

2. Navegue até o diretório:
```bash
cd desafios_infinity_school
```

3. Execute qualquer desafio:
```bash
python desafio_aula01.py
python agenda.py
# ... outros arquivos
```

## 📚 Conceitos Aprendidos

- **Lógica de Programação:** Estruturação de algoritmos e resolução de problemas
- **Estruturas de Controle:** Uso eficiente de loops e condicionais
- **Manipulação de Dados:** Trabalho com diferentes tipos de dados e estruturas
- **Validação de Entrada:** Tratamento de dados do usuário
- **Otimização:** Algoritmos eficientes para problemas específicos
- **Interface de Usuário:** Criação de menus e interação com o usuário

## 🎯 Objetivos de Aprendizado

Cada desafio foi desenvolvido para consolidar conhecimentos específicos:
- Operadores matemáticos e lógicos
- Estruturas de repetição e condição
- Manipulação de coleções de dados
- Desenvolvimento de interfaces simples
- Resolução de problemas do mundo real

## 👨‍💻 Autor

**Samylle Maria**
- GitHub: [@samyllemaria](https://github.com/samyllemaria)

---

*Desenvolvido durante o curso da Infinity School - Turma de Programação Python*
