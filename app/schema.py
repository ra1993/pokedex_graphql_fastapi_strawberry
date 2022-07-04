import strawberry
from app.transform_data import process_pokedex
from app.schemas.poke_schema import Generation
# from app.schemas.poke_schema import Generation, Pokemon, PokeStats


# @strawberry.type
# class Query:
#     @strawberry.field
#     def hello_world(self)-> str:
#         return "Hello world"

@strawberry.type
class Query:
    
    PokeDex: Generation = strawberry.field(resolver=process_pokedex)
schema = strawberry.Schema(query=Query)