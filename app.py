import os
from langchain.chains import LLMChain
from langchain_community.llms import LlamaCpp
from langchain.prompts import ChatPromptTemplate
import chainlit as cl

# LlamaCpp 모델 로드
llm = LlamaCpp(
    model_path=os.path.join(os.path.dirname(__file__), 'unsloth.F16.gguf'),
    n_threads=8
)

# 수학 문제 해결을 위한 프롬프트 설정
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system",
            """
            You are a highly skilled math teacher. Your primary goal is to solve math problems step by step with clear explanations. 
            Avoid discussing unrelated topics. Focus solely on solving the given problem.
            """),
        ("user", "Here is a math problem: {question}\n"),
        ("assistant", "Let's solve this step by step:\n"),
    ]
)

@cl.on_chat_start
async def main():
    # PromptTemplate를 이용한 LLMChain 생성
    llm_chain = LLMChain(prompt=prompt_template, llm=llm, verbose=False)  # 디버깅 시 verbose=True 설정

    # 사용자 세션에 LLM 체인 저장
    cl.user_session.set('llm_chain', llm_chain)

@cl.on_message
async def on_message(message: cl.Message):
    # 사용자 세션에서 LLM 체인 가져오기
    llm_chain = cl.user_session.get("llm_chain")
    
    # 사용자 입력에 대한 응답 생성
    res = await llm_chain.acall({"question": message.content}, callbacks=[cl.AsyncLangchainCallbackHandler()])
    
    # 응답 메시지 전송
    await cl.Message(content=res["text"]).send()
