import strawberry
from app.transform_data import process_pokedex
from app.schemas.poke_schema import Generation
from app.schemas.pie_chart_schema import GenPieChart, Num_Points
from app.transform_data import generation_groupby

# @strawberry.type
# class Query:
#     @strawberry.field
#     def hello_world(self)-> str:
#         return "Hello world"

@strawberry.type
class Query:
    PokeDex: Generation = strawberry.field(resolver=process_pokedex)


def get_pie_chart_data()-> GenPieChart:
    pie_chart_data=[]
    gen_pie=[]
    for idx, row in generation_groupby.iterrows():
        gen_name=row['gen_name']
        points=row['gen_name_points']
        pie_chart_data.append(Num_Points(points=points))
        
        new_data = GenPieChart(
        generation=gen_name,
        chart_data=pie_chart_data
        )
        gen_pie.append(
            GenPieChart(
        generation=gen_name,
        chart_data=pie_chart_data
        )
        )
        return (
        GenPieChart(
        generation=gen_name,
        chart_data=pie_chart_data
        )
    )

@strawberry.type
class Query2:
    GenBreakDown : GenPieChart = strawberry.field(resolver=get_pie_chart_data) 


schema = strawberry.Schema(query=Query2)