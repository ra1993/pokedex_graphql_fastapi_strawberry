import strawberry
from typing import List
    

@strawberry.type
class ChartInfo:
    pokemon_name: None or str #Union[str, None]
    poke_japanese_name: None or str # Union[str, None]
    pokedex_number: None or int # Union[int, None]


@strawberry.type
class Generation:
    generation_name: None or str # Union[str, None]
    chart_data: List[ChartInfo]