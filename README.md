# 🤖 Agente de IA com OpenRouter e Function Calling

Este projeto é um assistente interativo que utiliza a API do OpenRouter e implementa o recurso de **Function Calling** (chamada de funções/ferramentas) para consultar dados dinâmicos do computador, como a hora atual.

## 🚀 Funcionalidades

- **Persona customizada:** configurado como um assistente de estudos focado em explicações simples e didáticas.
- **Function Calling:** capacidade da IA de solicitar a execução de funções locais escritas em Python (`obter_hora_atual`).
- **Loop interativo:** permite uma conversa contínua via terminal até que o usuário digite `sair`.

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Biblioteca `openai` (compatível com a API do OpenRouter)
- OpenRouter API (usando modelos gratuitos, como `openrouter/free`)

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```
git clone https://github.com/seu-usuario/agente-ia-openrouter.git
cd agente-ia-openrouter
```

### 2. Instalar as dependências

```
pip install openai
```

### 3. Configurar a chave da API (OpenRouter)

Para manter sua chave segura, use uma variável de ambiente:

**Linux / macOS:**

```
export OPENROUTER_API_KEY="sua_chave_aqui"
```

**Windows (Prompt de Comando):**

```
set OPENROUTER_API_KEY=sua_chave_aqui
```

**Windows (PowerShell):**

```
$env:OPENROUTER_API_KEY="sua_chave_aqui"
```

> ⚠️ Nunca suba sua chave verdadeira para o GitHub.

### 4. Executar o assistente

```
python agenteIA.py
```

## 📚 Exemplo de uso no terminal

```
Assistente de Estudos pronto.
Digite 'sair' para encerrar.

Você: Olá, você pode me ajudar a organizar meus estudos?
Assistente: Olá! Com certeza. Posso te ajudar a planejar sua rotina...

Você: Que horas são agora?
Assistente: Agora são 14:35.
```
