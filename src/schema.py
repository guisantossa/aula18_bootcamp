from pydantic import BaseModel


class PokemonSchame(BaseModel): #schema de dados, a view da minha api
    name: str
    type: str

    class Config:
        from_attributes = True