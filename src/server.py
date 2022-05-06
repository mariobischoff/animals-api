from typing import List, Optional
from uuid import uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["http://127.0.0.1:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[str]
    name: str
    age: int
    sex: str
    color: str

animals: List[Animal] = []

@app.get("/animals/")
def get_animals() -> List[Animal] or Animal:
    return animals

@app.post("/animals/")
def create_animals(animal: Animal) -> Animal:
    animal.id = str(uuid4())
    animals.append(animal)
    return animal

@app.get("/animals/{id_animal}")
def get_animal_by_id(id_animal: str):
    for animal in animals:
        if animal.id == id_animal:
            return animal
    return {"error": "dont find"}

@app.delete("/animals/{id_animal}")
def remove_animal(id_animal: str):
    for index,animal in enumerate(animals):
        if animal.id == id_animal:
            return animals.pop(index)
    return {"error": "dont find"}
