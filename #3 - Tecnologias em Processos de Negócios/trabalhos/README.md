###### PT

# Anotações da Disciplina

## Modelagem BPMN

A modelagem BPMN (*Business Process Model and Notation*) é uma metodologia visual usada para representar de forma clara e padronizada os processos de negócio de uma organização. Por meio de diagramas com símbolos específicos, ela facilita o entendimento, a análise e a melhoria dos fluxos de trabalho, promovendo comunicação eficiente entre áreas técnicas e de negócio. Abaixo, tem um exemplo visual de como um processo pode ser representado em BPMN:

<div align="center">
  
| ![Processo de Aprovação de Férias](./processo_de_aprovacao_de_ferias.png) |
|:--:|
| *Processo de Aprovação de Férias* |

</div>

### Gateway

Um *Gateway* é um diamante (losango) no diagrama, ele serve para controlar o caminho que o fluxo do processo vai seguir:

| Tipo de Gateway | Nome Completo | Símbolo Visual (descrição) | Significado / Quando Usar | Exemplo Prático |
|------------------|----------------|-----------------------------|----------------------------|------------------|
| Exclusivo | Gateway Exclusivo (XOR) | Losango com um “X” dentro | Representa uma **decisão exclusiva**, onde **somente um caminho** será seguido entre várias opções. | “Produto em estoque?” → Sim vai para uma tarefa, Não vai para outra. |
| Paralelo | Gateway Paralelo (AND) | Losango com um sinal de “+” dentro | Representa **atividades que ocorrem simultaneamente**. Todos os caminhos são seguidos ao mesmo tempo. | Após aprovar pedido, enviar e-mail ao cliente **e** atualizar sistema de estoque. |
| Inclusivo | Gateway Inclusivo (OR) | Losango com um pequeno círculo dentro | Permite que **um ou mais caminhos** sejam seguidos, dependendo das condições. | “Tipo de cliente?” → Pode precisar gerar cadastro **e** verificar crédito. |
| Baseado em Evento | Gateway Baseado em Evento | Losango com **dois círculos concêntricos** dentro | O caminho seguido depende de **qual evento ocorrer primeiro** (mensagem recebida, tempo, etc.). | Após enviar boleto, o processo aguarda: pagamento confirmado **ou** tempo limite expirado. |
| Complexo | Gateway Complexo | Losango com um asterisco “*” dentro | Usado para **regras de fluxo mais específicas** ou personalizadas, quando a lógica não é apenas simples ou/and. | Prosseguir quando **2 de 3 condições** forem atendidas. |


### Nomeando atividades

* o nomeamento das atividades precisa iniciar com verbo no infinitivo (ex: "Acessar", "Verificar", "Conferir")

### AS IS e TO BE

No contexto do BPMN, **“As Is”** representa o modelo do processo **como ele funciona atualmente**, mostrando suas etapas reais, gargalos e falhas existentes. Já o **“To Be”** descreve o processo **como ele deve funcionar no futuro**, após melhorias, automações ou reestruturações. Essa comparação entre o As Is e o To Be é essencial para identificar oportunidades de otimização e planejar transformações eficientes nos processos de negócio.

<div align="center">

| Aspecto                  | As Is (Estado Atual)                              | To Be (Estado Futuro)                              |
|---------------------------|---------------------------------------------------|----------------------------------------------------|
| Objetivo                 | Descrever como o processo funciona hoje           | Mostrar como o processo deve funcionar             |
| Foco                     | Identificar problemas, gargalos e ineficiências   | Propor melhorias, automações e otimizações         |
| Base de informação        | Observação e documentação da prática atual        | Planejamento e modelagem de novas práticas         |
| Nível de detalhamento     | Detalhado e fiel à realidade                      | Simplificado e orientado à eficiência              |
| Finalidade                | Entendimento e diagnóstico                        | Implementação de mudanças e melhorias              |
| Uso no BPMN               | Mapeamento do processo existente                  | Modelagem do processo redesenhado                  |

</div>

---

## 📜 Licença
Este repositório é de uso **educacional e livre**, podendo ser utilizado e modificado conforme necessidade, desde que citada a fonte.


