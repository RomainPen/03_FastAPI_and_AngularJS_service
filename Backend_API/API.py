from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="API Todo List")

# Configuration CORS pour permettre les requêtes depuis le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://172.18.0.3:4200", "http://127.0.0.1:4200", "http://51.158.116.93:4200", "http://frontend2:4200"],  # Origine du frontend Angular.cli
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"API_message": "Bienvenue sur l'API Opensearch"}


list_dict_data = [
    {"id": 1, "description": "Red apple on a wooden table, romain"},
    {"id": 2, "description": "Blue sky with white clouds"},
    {"id": 3, "description": "A cat sleeping on a couch"},
    {"id": 4, "description": "Mountain landscape during sunrise"},
    {"id": 5, "description": "City skyline at night with bright lights"},
    {"id": 6, "description": "A cup of coffee with steam rising"},
    {"id": 7, "description": "A stack of books on a desk"},
    {"id": 8, "description": "A river flowing through a forest"},
    {"id": 9, "description": "A bicycle parked near a tree"},
    {"id": 10, "description": "A person walking in the rain with an umbrella"},
    {"id": 11, "description": "A dog playing in a park"},
    {"id": 12, "description": "A beach with waves crashing on the shore"},
    {"id": 13, "description": "A plate of sushi on a table"},
    {"id": 14, "description": "A bridge over a calm lake"},
    {"id": 15, "description": "A train passing through a countryside"},
    {"id": 16, "description": "A group of friends having a picnic"},
    {"id": 17, "description": "A bookshelf filled with colorful books"},
    {"id": 18, "description": "A street market with fresh fruits and vegetables"},
    {"id": 19, "description": "A lighthouse standing on a rocky shore"},
    {"id": 20, "description": "A farmer working in a rice field, romain"},
]


@app.get("/searchdocument/{key_word}")
def return_document(key_word : str):

    output_list_dict = [dict_id for dict_id in list_dict_data if dict_id["description"].find(key_word) != -1]
    return {"API_message": output_list_dict}

