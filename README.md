Agent de IA com OpenRouter e Function Calling
Este projeto é um assistente interativo que utiliza a API do OpenRouter e implementa o recurso de Function Calling (chamada de funções/ferramentas) para consultar dados dinâmicos do computador, como a hora atual.

🚀 Funcionalidades
Persona Customizada: Configurado como um assistente de estudos focado em explicações simples e didáticas.
Function Calling: Capacidade da IA de solicitar a execução de funções locais escritas em Python (obter_hora_atual).
Loop Interativo: Permite uma conversa contínua via terminal até que o usuário decida encerrar digitando sair.
🛠️ Tecnologias Utilizadas
Python 3.x
Biblioteca openai (compatível com a API padrão do OpenRouter)
OpenRouter API (utilizando modelos gratuitos disponíveis, como openrouter/free)
⚙️ Como Executar o Projeto
1. Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Instalar as dependências
Certifique-se de ter o Python instalado e instale a biblioteca da OpenAI:

pip install openai
3. Configurar a Chave da API (OpenRouter)
Para manter sua chave segura e evitar expô-la publicamente no código, utilize uma variável de ambiente:

No Linux / macOS:

export OPENROUTER_API_KEY="sua_chave_aqui"
No Windows (Prompt de Comando):

set OPENROUTER_API_KEY=sua_chave_aqui
No Windows (PowerShell):

$env:OPENROUTER_API_KEY="sua_chave_aqui"
(Nota: Caso prefira, você também pode substituir diretamente a string da chave, mas lembre-se de nunca subir sua chave para o GitHub).

4. Executar o Assistente
python main.py
📚 Exemplo de Uso no Terminal
Assistente de Estudos pronto.
Digite 'sair' para encerrar.

Você: Olá, você pode me ajudar a organizar meus estudos?
Assistente: Olá! Com certeza. Posso te ajudar a planejar sua rotina...

Você: Que horas são agora?
Assistente: Agora são 14:35.
