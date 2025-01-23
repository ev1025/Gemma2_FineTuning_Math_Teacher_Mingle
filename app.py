import os
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import chainlit as cl
from dotenv import load_dotenv

# .env 파일에서 Hugging Face API 키 로드
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
model_id = 'Envy1025/math_teachear_mingle'

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",
            """
            You are an AI assistant that provides helpful answers to user queries.
            """),
        ("user", "{question}\n"),
    ]
)
    
@cl.on_chat_start
async def main():
    # Hugging Face 엔드포인트 LLM 초기화
    llm = HuggingFaceEndpoint(
        repo_id=model_id, 
        max_new_tokens=500,
        temperature=0.5, 
        token=HF_API_KEY
    )

    # LLM 체인 생성
    llm_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True) # 설명

    # 사용자 세션에 LLM 체인 저장
    cl.user_session.set("llm_chain", llm_chain)

@cl.on_message
async def on_message(message: cl.Message):
    # 사용자 세션에서 LLM 체인 가져오기
    llm_chain = cl.user_session.get("llm_chain")
    
    # 메시지에 대한 응답 생성
    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])
    
    # 응답 메시지 전송
    await cl.Message(content=res["text"]).send()