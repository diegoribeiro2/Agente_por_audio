from dotenv import load_dotenv, find_dotenv
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import pandas as pd

from langchain.agents.agent_types import AgentType

load_dotenv(find_dotenv())

df = pd.read_csv("df_rent.csv")

prompt= """
    Você se chama Didico, atua como um analista de dados profissional e está trabalhando com dataframe pandas no Python. O nome do Dataframe é `df`.
     """

agent = create_pandas_dataframe_agent(
    ChatOpenAI(model='gpt-3.5-turbo-0125'),
    df,
    prefix=prompt,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS
)

def chat_loop():
    while True:
        print("\n🤖 Digite a sua mensagem ou digite 'sair' para encerrar.")
        user_input = input("👉 ")
        
        if user_input.lower() == 'sair':
            print("Encerrando o chat...")
            break
            
        try:
            resposta = agent.invoke(user_input)
            print(f"\n🤖 Didico: {resposta['output']}")
        except Exception as e:
            print(f"\n❌ Erro: {e}")


# Inicia o loop de chat
if __name__ == "__main__":
    chat_loop()