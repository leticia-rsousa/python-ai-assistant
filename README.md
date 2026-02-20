## Python AI Assistant
**Descrição Geral** 📄<br>
Este projeto apresenta um **assistente de programação em Python**, desenvolvido com **Streamlit** e integrando um modelo de **IA (Groq LLM)**. O sistema permite que usuários façam perguntas sobre **Python, algoritmos e boas práticas de programação**, recebendo respostas com **explicações, exemplos de código e referências**. O projeto demonstra conceitos de **interação com APIs, manipulação de estado e interface web interativa.**

---
**Objetivo** 🎯 <br> 
O objetivo principal do projeto é fornecer um **assistente virtual de programação em Python**, que auxilie iniciantes a compreender código, estruturas de dados e lógica de programação de forma prática e interativa.

---
**Tecnologias Utilizadas** 💻 <br>
* ***Python*** - linguagem principal.
* ***Streamlit*** - criação de interface web interativa.
* ***API Groq / LLM*** - geração de respostas inteligentes com IA.
* ***Manipulação de estado com st.session_state*** - armazenamento do histórico de conversas.
* ***Integração com chat e mensagens*** - captura de input do usuário e exibição das respostas.

---
**Arquitetura e Estrutura do Código** 🧱 <br><br>
***1. Script Principal (python_ai_assistant.py)*** <br>
Responsável por:
* ***Configuração da página do Streamlit.*** 
* ***Captura da API Key da Groq.***
* ***Inicialização do histórico de mensagens com st.session_state.***
* ***Exibição das mensagens do usuário e respostas do assistente.***
* ***Envio de prompts para a API e processamento das respostas.***
* ***Exibição da interface do chat.*** 

***2. Prompt Customizado (CUSTOM_PROMPT)*** <br>
Define as **regras de operação do assistente**, incluindo: 
* ***Foco em programação Python.*** 
* ***Estrutura da resposta (explicação, código, detalhes, documentação).***
* ***lareza e precisão das respostas.***

***3. Barra Lateral (Sidebar)*** <br>
Inclui:
* ***Campo para API Key.*** 
* ***Informações sobre o assistente.***
* ***Links úteis e botões de suporte.***

***4. Exibição de Respostas*** <br>
* ***Mensagens do usuário e do assistente são exibidas em formato de chat.***
* ***Uso de st.spinner para indicar processamento.***
* ***Armazenamento do histórico de mensagens.***

---
**Conceitos e Funcionalidades Demonstradas** 🔍 <br><br>
✅ ***Integração com APIs:*** <br>
Uso da API Groq para geração de respostas inteligentes em Python.

✅***Interatividade Web:*** <br>
Interface responsiva com **Streamlit**, permitindo input do usuário e exibição dinâmica de mensagens.

✅***Gestão de estado:*** <br>
Uso de st.session_state para armazenar e recuperar o histórico de conversas.

✅***Boa prática de prompts:*** <br>
Separação clara entre regras do sistema e mensagens do usuário, estruturando a lógica do assistente.

---
**Como Executar o Projeto** ▶️ <br><br>
***1. Instale as dependências (recomendado via requirements.txt):*** <br>
```pip install -r requirements.txt```
ou manualmente:
```pip install streamlit groq```

***2. Execute o projeto com Streamlit:*** <br>
```streamlit run python_ai_assistant.py```

***3. Insira a sua API Key da Groq na barra lateral para começar a interagir com o assistente.*** <br>

***Exemplo de Uso:*** <br>
```
Usuário: Como criar uma função em Python?
Assistente: Explicação detalhada sobre definição de funções, exemplo de código com def, parâmetros, return e documentação de referência.
```

---
**Conclusão** 📌 <br>
Este projeto demonstra a criação de um **assistente virtual de programação em Python**, integrando **IA, interface web interativa e gerenciamento de estado**. Ele evidencia como construir sistemas interativos, organizados e que fornecem suporte prático a iniciantes em programação.
