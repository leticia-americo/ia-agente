# Importa a classe OpenAI da biblioteca openai.
from openai import OpenAI

# Importa datetime para podermos consultar a hora atual do computador.
from datetime import datetime
import os

# Carrega a chave da API do OpenRouter a partir de uma variável de ambiente ou define um valor padrão
api_key = os.getenv("OPENROUTER_API_KEY", "sua-chave-api-aqui")

# Cria um objeto da classe OpenAI configurado para o OpenRouter.
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


# --------------------------------------------------
# FUNÇÃO QUE SERÁ USADA COMO FERRAMENTA (TOOL)
# --------------------------------------------------

def obter_hora_atual():
    """Retorna a hora atual no formato HH:MM."""
    agora = datetime.now()
    return agora.strftime("%H:%M")


# --------------------------------------------------
# DESCRIÇÃO DAS FERRAMENTAS
# --------------------------------------------------

ferramentas = [
    {
        "type": "function",
        "function": {
            "name": "obter_hora_atual",
            "description": "Retorna a hora atual no formato HH:MM.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]


# --------------------------------------------------
# HISTÓRICO DA CONVERSA E PERSONA
# --------------------------------------------------

mensagens = [
    {
        "role": "system",
        "content": (
            "Você é um assistente de estudos.\n"
            "Seu objetivo é ajudar o usuário respondendo perguntas "
            "e utilizando as ferramentas disponíveis quando necessário.\n"
            "Regras:\n"
            "- Explique de forma simples.\n"
            "- Quando precisar de uma informação disponível por uma ferramenta, "
            "utilize essa ferramenta."
        )
    }
]


print("\nAssistente de Estudos pronto.")
print("Digite 'sair' para encerrar.")


# --------------------------------------------------
# LOOP DA CONVERSA
# --------------------------------------------------

while True:
    pergunta = input("\nVocê: ")

    if pergunta.lower() == "sair":
        break

    mensagens.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    # Primeira chamada para a IA (enviando ferramentas)
    resposta = client.chat.completions.create(
        model="openrouter/free",
        messages=mensagens,
        tools=ferramentas
    )

    mensagem = resposta.choices[0].message

    # Verifica se a IA solicitou execução de alguma ferramenta
    if mensagem.tool_calls:
        chamada = mensagem.tool_calls[0]

        if chamada.function.name == "obter_hora_atual":
            resultado = obter_hora_atual()

            # Registra o pedido da IA no histórico
            mensagens.append(
                {
                    "role": "assistant",
                    "content": mensagem.content,
                    "tool_calls": [
                        {
                            "id": chamada.id,
                            "type": "function",
                            "function": {
                                "name": chamada.function.name,
                                "arguments": chamada.function.arguments
                            }
                        }
                    ]
                }
            )

            # Registra o resultado da execução da ferramenta
            mensagens.append(
                {
                    "role": "tool",
                    "tool_call_id": chamada.id,
                    "content": resultado
                }
            )

            # Segunda chamada para a IA processar o resultado da ferramenta
            resposta_final = client.chat.completions.create(
                model="openrouter/free",
                messages=mensagens,
                tools=ferramentas
            )

            texto_final = resposta_final.choices[0].message.content

            mensagens.append(
                {
                    "role": "assistant",
                    "content": texto_final
                }
            )

            print("\nAssistente:", texto_final)

    else:
        texto_resposta = mensagem.content

        mensagens.append(
            {
                "role": "assistant",
                "content": texto_resposta
            }
        )

        print("\nAssistente:", texto_resposta)