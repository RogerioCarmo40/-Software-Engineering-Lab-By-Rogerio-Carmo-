# 🏗️ Software Engineering Learning Lab: Do Conceito à Prática

Este repositório foi desenvolvido como parte de um desafio prático da **DIO (Digital Innovation One)**, focado no uso de Inteligência Artificial (**NotebookLM**) como ferramenta de aprendizagem ativa em Engenharia de Software.

> **Status do Projeto:** Concluído ✅
> **Foco:** Capítulo 1 - Natureza da Engenharia de Software, Produtos e Métricas.

---

## 🎯 Contexto e Objetivos

O objetivo deste projeto é transitar da "programação por hobby" para a **Engenharia de Software Profissional**. Utilizei o NotebookLM para processar fontes de alta autoridade e extrair os fundamentos que regem a criação de sistemas robustos, focando especialmente no equilíbrio entre **Prazo, Custo e Qualidade**.

**Objetivos de Estudo:**
* Diferenciar Ciência da Computação de Engenharia de Software.
* Compreender o impacto dos requisitos na viabilidade financeira de um projeto.
* Implementar ferramentas de automação (Python) para suporte à produtividade.

---

## 📚 Curadoria de Fontes

Para garantir a maturidade técnica do caderno temático, foram utilizadas as seguintes fontes reais e consagradas na indústria:

1.  **IEEE SWEBOK v3.0**: O Guia para o Corpo de Conhecimento de Engenharia de Software.
2.  **Manifesto Ágil (2001)**: Princípios fundamentais para o desenvolvimento moderno.
3.  **Software Engineering (Ian Sommerville)**: Referência acadêmica sobre processos e ciclos de vida.
4.  **The Mythical Man-Month (Fred Brooks)**: Ensaio clássico sobre gestão de prazos e o "fator humano".
5.  **Relatório Chaos (Standish Group)**: Dados estatísticos sobre sucessos e falhas em projetos de software.

---

## 🧠 Engenharia de Prompts e "Cicatrizes" (Troubleshooting)

Nesta seção, documento o raciocínio por trás da interação com a IA. O mercado valoriza quem entende o processo, não apenas o resultado.

### A Evolução do Prompt
* **Problema:** Inicialmente, a IA gerava resumos genéricos (estilo Wikipedia).
* **Solução:** Implementei a técnica de **Persona de Mentor Sênior** e adicionei a restrição do **Triângulo de Ferro**. Forcei a IA a explicar cada conceito técnico através da lente do custo e do risco de negócio.

### Dificuldades e Soluções (Troubleshooting)
* **Fidelidade às Fontes:** Identifiquei que a IA tentava generalizar conceitos. Ajustei o prompt para exigir citações diretas dos documentos carregados, garantindo precisão científica.
* **Desenvolvimento de Ferramenta (Python):** Ao criar o *Timer de Produtividade* (disponível no histórico de chat), houve um conflito no loop da interface gráfica. A correção exigiu o uso de threads para que o contador de "páginas" funcionasse sem travar a interface de ponteiros.

---

## 📖 Miniguia de Estudo (Consolidado)

### 1. Resumo Estruturado: Natureza da Engenharia de Software e o Triângulo de Ferro
A Natureza da Engenharia de Software: Ciência vs. Engenharia
A Engenharia de Software é definida como uma disciplina de engenharia que se preocupa com todos os aspectos da produção de software, desde a concepção inicial até a manutenção
. A principal distinção entre ela e a Ciência da Computação reside no foco: enquanto a ciência foca em teorias e fundamentos, a engenharia concentra-se nas praticidades de desenvolver e entregar softwares úteis
. Embora a engenharia de software utilize a base da ciência da computação e da matemática, ela lida com problemas não lineares de escalonamento industrial e com a complexidade do comportamento humano
.
"A ciência da computação foca a teoria e os fundamentos; engenharia de software preocupa-se com o lado prático do desenvolvimento e entrega de softwares úteis."
O Triângulo de Ferro: Prazos, Custos e Qualidade
O sucesso de um projeto está intrinsecamente ligado ao equilíbrio entre escopo, custo e tempo, elementos que compõem o chamado Triângulo de Ferro
. A gestão eficiente busca realizar o trade-off (compensação) entre esses fatores para entregar valor aos stakeholders
. Nas abordagens tradicionais, o escopo costuma ser fixo, tornando o tempo e o custo flexíveis; já nas metodologias ágeis, o custo e o tempo são fixos, enquanto o escopo é flexível para garantir a qualidade
.
"Fatores como escopo, custo e tempo têm um impacto direto no sucesso e na qualidade do projeto, e é comum a utilização da ilustração triângulo de ferro [...] para representar a singularidade das abordagens tradicionais e ágeis."

--------------------------------------------------------------------------------
### 2. Glossário Técnico (10 Termos Críticos)
Requisitos: Descrições do que o sistema deve fazer, os serviços que oferece e as restrições ao seu funcionamento
.
Stakeholders: Qualquer pessoa ou papel que seja afetado pelo sistema, possuindo necessidades e expectativas que podem ser conflitantes
.
Processo de Software: Um conjunto coerente de atividades relacionadas (especificação, desenvolvimento, validação e evolução) que levam à produção de um produto de software
.
Metodologias Ágeis: Métodos orientados à entrega rápida e incremental de software funcional, minimizando a documentação excessiva e focando nas pessoas e na colaboração
.
Gerenciamento de Configuração (CM): Conjunto de políticas e ferramentas para gerenciar as mudanças e versões de sistemas de software em evolução
.
Sprint: Ciclo de tempo fixo (geralmente de duas a quatro semanas) no framework Scrum, dentro do qual um conjunto de atividades deve ser planejado e executado
.
Manutenibilidade: Atributo de qualidade que indica a facilidade com que o software pode evoluir para atender a novas necessidades do cliente ou ambiente
.
Validação: O processo de verificar se o sistema atende às necessidades reais e expectativas do cliente ("estamos construindo o produto certo?")
.
Verificação: O processo de verificar se o sistema está em conformidade com sua especificação técnica ("estamos construindo o produto da maneira certa?")
.
Propriedade Emergente: Uma característica ou atributo que só se manifesta quando todos os componentes de um sistema são integrados e funcionam em conjunto
.

--------------------------------------------------------------------------------
### 3. Análise de Conflitos: A Medição da Qualidade de Software
As fontes revelam uma divergência fundamental sobre como definir e medir a qualidade.
Visão de Conformidade vs. Adequação: Algumas fontes citam a definição clássica de Phil Crosby como "conformidade com os requisitos", enquanto Watts Humphrey a define como "alcançar excelentes níveis de adequação ao uso"
.
Métricas Internas vs. Atributos Externos: Existe um conflito sobre a eficácia das métricas quantitativas. Enquanto o modelo ISO/IEC 25010 fornece uma taxonomia para rating de produtos
, Sommerville argumenta que métricas internas (como linhas de código ou complexidade ciclomática) não possuem um relacionamento claro e consistente com atributos externos de qualidade, como manutenibilidade ou usabilidade
.
Abordagem Ágil vs. Tradicional: O Manifesto Ágil estabelece que o "software funcional" é a medida primária de progresso e, por extensão, de qualidade
. Isso diverge das abordagens tradicionais que utilizam inspeções rigorosas e processos de QA independentes para garantir a conformidade com padrões organizacionais e documentais

---
## 📝 Simulado de Revisão
## 📝 4. Guia de Revisão: Gestão de Produtos e Problemas

**1. Qual é a medida primária de progresso em um projeto que segue os princípios ágeis?** 

a) O cumprimento rigoroso do cronograma inicial.  
b) A quantidade de documentação técnica produzida.  
c) Software funcional (produtivo).  
d) A ausência total de defeitos reportados.  

> *Gabarito: **c)** Segundo o Manifesto Ágil e as práticas de XP, o software funcional é a única coisa que indica o que realmente foi construído pelas equipes.*

---

**2. No framework Scrum, como é chamada a lista priorizada de trabalhos a serem realizados no projeto?** 

a) Diagrama de Gantt.  
b) Product Backlog.  
c) Sprint Report.  
d) Estrutura Analítica de Projeto (EAP).  

> *Gabarito: **b)** O ponto de partida para o planejamento no Scrum é o backlog do produto, que contém a lista do trabalho a ser feito, revisada com o cliente.*

---

**3. O que caracteriza o processo de "Retrabalho" na gestão de problemas de software?** 

a) A criação de novos requisitos para o próximo release.  
b) O ato de refazer o trabalho devido a mudanças nos requisitos ou falhas detectadas.  
c) A automação de tarefas repetitivas.  
d) O treinamento de novos membros da equipe.  

> *Gabarito: **b)** O retrabalho ocorre quando a mudança aumenta os custos de desenvolvimento, exigindo que partes da análise, projeto ou codificação sejam repetidas.*

---

**4. Qual atividade de gerenciamento de configuração foca em decidir se e quando uma mudança deve ser implementada?** 

a) Gerenciamento de versões.  
b) Construção de sistemas.  
c) Gerenciamento de mudanças.  
d) Gerenciamento de releases.  

> *Gabarito: **c)** O gerenciamento de mudanças envolve acompanhar solicitações, definir custos e impactos, e decidir sobre sua implementação.*

---

**5. Por que é difícil alcançar a "Completude" e "Consistência" nos requisitos de grandes sistemas?** 

a) Porque os engenheiros de software não utilizam ferramentas CASE.  
b) Devido à intangibilidade do software que impede sua visualização.  
c) Por causa da existência de muitos stakeholders com necessidades diferentes e frequentemente inconsistentes.  
d) Porque as metodologias ágeis proíbem a coleta de requisitos.  

> *Gabarito: **c)** Em sistemas complexos, stakeholders diversos possuem expectativas que podem entrar em conflito, dificultando uma especificação única, completa e sem contradições.*


## 🛠️ Ferramenta de Apoio: Timer de Ciclos em Python
Como parte do aprendizado prático, desenvolvi um script Python (Tkinter) que gerencia ciclos de trabalho:
* Contador de segundos customizável.
* Geração de log automático em `.txt` com métricas de horas, minutos e "páginas" produzidas.
* Interface com ponteiros analógicos para foco visual.

![3d-rendering-triangle](https://github.com/user-attachments/assets/044f63a6-0116-424b-b296-7b6ebf57ba8d)

---

## 👤 Autor
**ROGERIO CARMO**
*Consultor e Desenvolvedor "One-Man Team"*

*Back-end Developer -->> Full Stack Developer...*

[[[Seu LinkedIn]](https://www.linkedin.com/in/rogeriocarmo40/)]| [Seu Portfólio]
