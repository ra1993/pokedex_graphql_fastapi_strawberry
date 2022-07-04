import strawberry
from typing import List, Union

@strawberry.type
class Num_Points:
    points: Union[int, None]

@strawberry.type
class GenPieChart:
    generation:Union[str, None]
    chart_data: List[Num_Points]