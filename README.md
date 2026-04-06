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

### 1. Resumo: A Natureza da Engenharia
Diferente da Ciência da Computação (focada em teorias e algoritmos), a Engenharia de Software é uma disciplina de **compromisso**. Ela busca a solução técnica ideal dentro das limitações de **orçamento** e **tempo**.

### 2. Glossário de Conceitos Chave
* **Dívida Técnica:** O custo implícito de escolher uma solução rápida agora em vez de uma abordagem melhor que levaria mais tempo.
* **Stakeholders:** Todas as partes interessadas que influenciam os requisitos do produto.
* **SLA (Service Level Agreement):** O compromisso de nível de serviço, essencial para a métrica de Qualidade.

### 3. Prompts Reutilizáveis para Revisão
> *"Atue como um Mentor Sênior. Com base no SWEBOK, explique como um requisito mal definido no início do projeto pode triplicar o custo final na fase de manutenção."*

---

## 🛠️ Ferramenta de Apoio: Timer de Ciclos em Python
Como parte do aprendizado prático, desenvolvi um script Python (Tkinter) que gerencia ciclos de trabalho:
* Contador de segundos customizável.
* Geração de log automático em `.txt` com métricas de horas, minutos e "páginas" produzidas.
* Interface com ponteiros analógicos para foco visual.

---

## 👤 Autor
**ROGERIO CARMO**
*Consultor e Desenvolvedor "One-Man Team"*
[[[Seu LinkedIn]](https://www.linkedin.com/in/rogeriocarmo40/)]| [Seu Portfólio]
