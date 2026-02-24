import uuid
import random
from locust import HttpUser, task, between

CHAT_QUESTIONS = [
    # Basic
    "Who is Aayushmaan?",
    "What is your tech stack?",
    "Tell me about your AI projects",
    "What is your work experience?",
    "Where did you study?",
    "What is Aayushmaan's age?",
    "What sports did Aayushmaan play?",
    "What is your experience with RAG?",
    "How can I contact Aayushmaan?",
    "What is Aayushmaan's personal bot?",
    # Multi-hop / complex
    "Compare your work at Annalect vs Stoik — what was different?",
    "What specific tools did you use to build your Voice RAG app and how does it work end to end?",
    "How does your experience with table tennis relate to your engineering career?",
    "Can you explain the architecture of your MCP Leave Manager server?",
    "What makes you different from other AI engineers applying for jobs right now?",
    "Walk me through your RAG evaluation pipeline — what metrics do you track?",
    "How did your Master's at UNSW shape your focus on applied AI?",
    "If I wanted to hire you for a RAG project, what would you bring to the table?",
    "What's your experience with multi-agent systems and when would you use them over single agents?",
    "Tell me about your family background and how it influenced your career",
]


class AayushBotUser(HttpUser):
    wait_time = between(10, 20)

    @task(1)
    def health_check(self):
        self.client.get("/health", timeout=10)

    @task(5)
    def chat(self):
        question = random.choice(CHAT_QUESTIONS)
        thread_id = f"load-test-{uuid.uuid4().hex[:8]}"

        self.client.post(
            "/chat",
            json={"message": question, "thread_id": thread_id},
            timeout=120,
        )
