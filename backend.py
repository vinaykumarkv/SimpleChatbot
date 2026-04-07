import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 1. Setup Examples
examples = [
    {"input": "How to implement Retrieval-Augmented Generation (RAG) for production?",
     "output": "Thanks! For your query, here is a technical implementation plan: 1. Optimize document chunking strategies, 2. Select a scalable Vector Database, 3. Implement a semantic caching layer to reduce latency, 4. Integrate an evaluation framework like RAGAS, and 5. Orchestrate the deployment using Kubernetes for high availability."},
    {"input": "What are the steps for deploying a fine-tuned Large Language Model?",
     "output": "Thanks! For your query, here is a technical implementation plan: 1. Apply model quantization (such as AWQ or GPTQ) to reduce memory footprint, 2. Utilize high-throughput serving engines like vLLM, 3. Containerize the application using Docker, 4. Configure GPU autoscaling policies, and 5. Establish monitoring for model drift and hallucinations."},
    {"input":"When should a team choose Fine-tuning over RAG?",
     "output":"Thanks! For your query, here is a technical implementation plan: 1. Use RAG when the model needs access to real-time or proprietary external data, 2. Choose Fine-tuning when the objective is to change the model's behavior, tone, or specific vocabulary, 3. Evaluate the cost-to-performance ratio of managing specialized infrastructure versus vector search, and 4. Consider a hybrid approach for complex enterprise applications."}
]

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}"
)

# 2. Create FewShotPromptTemplate (Added {history} to the suffix)
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="You are a technical expert in building end-to-end AI systems in big tech.\n\nRelevant Conversation History:\n{history}",
    suffix="\nInput: {input}\nOutput:",
    input_variables=["history", "input"]
)


def demo_chatbot():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # Use "gemini-1.5-flash" unless you have specific 2.0 access
        temperature=0.5,
        google_api_key=api_key
    )


def demo_memory():
    llm = demo_chatbot()
    # ConversationBufferMemory uses the key 'history' by default
    return ConversationBufferMemory(llm=llm, max_token_limit=500)


def demo_conversation(input_text, memory):
    llm_instance = demo_chatbot()

    # 3. Pass the few_shot_prompt to the ConversationChain
    conversation_chain = ConversationChain(
        llm=llm_instance,
        memory=memory,
        prompt=few_shot_prompt,  # This connects your few-shot logic to the chain
        verbose=True
    )

    chat_reply = conversation_chain.predict(input=input_text)
    return chat_reply, memory
