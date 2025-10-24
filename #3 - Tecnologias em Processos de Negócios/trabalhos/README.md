###### PT

# Anotações da Disciplina

## Modelagem BPMN

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

---

## 📜 Licença
Este repositório é de uso **educacional e livre**, podendo ser utilizado e modificado conforme necessidade, desde que citada a fonte.


