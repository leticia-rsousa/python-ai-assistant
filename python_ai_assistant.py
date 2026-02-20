# Importes
import os
import streamlit as st
from groq import Groq

# Configuração da página Streamlit
st.set_page_config(
    page_title="Python AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Prompt do sistema para o assistente
CUSTOM_PROMPT = """
Você é o "Python AI Assistant", um assistente de IA especialista em programação, com foco principal em Python. 
Sua missão é ajudar desenvolvedores iniciantes com dúvidas de código, lógica e boas práticas.

REGRAS DE OPERAÇÃO:
1. **Foco em Programação**: 
   Responda apenas a perguntas relacionadas à programação, algoritmos, estruturas de dados, 
   bibliotecas e frameworks. Se o usuário perguntar algo fora desse escopo, oriente-o educadamente a voltar ao tema.
2. **Estrutura da Resposta**: 
   Sempre formate suas respostas da seguinte maneira:
   **Explicação Clara**: 
   Comece com uma explicação conceitual sobre o tópico perguntado. Seja direto e didático.
   **Exemplo de Código**: 
   Forneça um ou mais blocos de código em Python com a sintaxe correta. 
   O código deve ser bem comentado para explicar as partes importantes.
   **Detalhes do Código**: 
   Após o bloco de código, descreva em detalhes o que cada parte do código faz, 
   explicando a lógica e as funções utilizadas.
   **Documentação de Referência**: 
   Ao final, inclua uma seção chamada **"Documentação de Referência"** com um link direto 
   e relevante para a documentação oficial da biblioteca ou função usada, quando houver.
3. **Clareza e Precisão**: 
   Use uma linguagem clara. Evite jargões desnecessários. Suas respostas devem ser tecnicamente precisas.
"""

# Barra lateral
with st.sidebar:
    st.title("🤖 Python AI Assistant")
    st.markdown("Um assistente de IA focado em programação Python para iniciantes.")
    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em: https://console.groq.com/keys",
    )
    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Pyhton. IA pode cometer erros. Sempre verifique as respostas.")
    st.markdown("---")
    st.markdown("Cursos e formações de Python:")
    st.markdown("🔗 [Data Science Academy] - https://www.datascienceacademy.com.br/cursosgratuitos")
    st.link_button("📧 E-mail Para o Suporte DSA no Caso de Dúvidas", "mailto:suporte@datascienceacademy.com.br")

# Títulos principais
st.title("Python AI Assistant")
st.title("Assistente Pessoal de Programação Python 🐍")
st.caption("Faça sua pergunta sobre Python e obtenha códigos, explicações e referências")

# Inicializa histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Inicializa cliente Groq
client = None
if groq_api_key:
    try:
        client = Groq(api_key=groq_api_key)
    except Exception as e:
        st.sidebar.error(f"Erro ao inicializar o cliente Groq: {e}")
        st.stop()
elif st.session_state.messages:
    st.warning("Por favor, insira sua API Key da Groq na barra lateral para continuar.")

# Captura entrada do usuário
if prompt := st.chat_input("Qual sua dúvida sobre Python?"):
    if not client:
        st.warning("Por favor, insira sua API Key da Groq na barra lateral para começar.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    messages_for_api = [{"role": "system", "content": CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    with st.chat_message("assistant"):
        with st.spinner("Analisando sua pergunta..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=messages_for_api,
                    model="openai/gpt-oss-20b",
                    temperature=0.7,
                    max_tokens=2048,
                )
                resposta = chat_completion.choices[0].message.content
                st.markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")

# Footer
st.markdown(
    """
    <div style="text-align: center; color: gray;">
        <hr>
        <p>Python AI Assistant</p>
    <div>
    """,
    unsafe_allow_html=True
)
