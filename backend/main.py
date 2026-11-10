from fastapi import FastAPI

klu = FastAPI(title="AI Tutor",
              description="AI Tutor Pbl Project",
              version="1.0.0")


@klu.get("/")
def home():
    return {"message":"Welcome To AI Tutor Project"}

@klu.get("/demo")
def demo():
    return {"message":"KL University"}

@klu.get("/askquestion")
def ask():
    return {"message":"What Is LLM","Answer":"Large Language Model"}

@klu.get("/student")
def student():
    return {"id":1, "name":"Ram", "gender":"Male", "course":"DSA"}

@klu.get("/students")
def getstudents():
    return [{"id":1, "name":"Ram", "gender":"Male", "course":"DSA"},
            {"id":2, "name":"KLU", "gender":"Male", "course":"AI"},
            {"id":3, "name":"Seetha", "gender":"Female", "course":"ML"}]