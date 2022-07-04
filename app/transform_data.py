import pandas as pd
import sys
# sys.path.append('../graphql_strawberry_fastapi')
from .schemas.poke_schema import Generation, Pokemon, PokeStats
# from read_data_g_drive import pokemon_df
# from schemas.build_schema import 

__all__=[
    "process_pokedex"
]

class poke_data_transform:
    def __init__(self,filename):
        self.path=f"/home/ra-terminal/Desktop/projects/medium_projects/graphql_strawberry_fastapi/datafiles/{filename}"
        self.poke_df= pd.read_csv(self.path)

    def set_region_name(self):
        generation_names=[]
        gen_names_dict={1: 'kanto',
                        2: 'Johto',
                        3: 'Hoenn',
                        4: 'Sinnoh',
                        5: 'Unova',
                        6: 'Kalos',
                        7: 'Alola',
                        8: 'Galar'}

        for row in self.poke_df.iterrows():
            gen_num = row[1]['generation']
            if gen_num in gen_names_dict.keys():
                generation_names.append(gen_names_dict[gen_num])
        self.poke_df['gen_name'] = generation_names

        def add_points(self, column_name):
            points_column=[]
            for row in self.poke_df.iterrows():
                target_column=row[column_name]
                if not pd.isna(target_column):
                    points_column.append(1)
                else:
                    points_column.append(0)
            self.poke_df[f'{column_name}points'] = points_column
    
        def agg_num_pokemon_region():
            pass

        def groupby_column(self, column_name):
            
            pass

def process_pie_chart():
    pass

def process_pokedex() -> Generation:
    poke_df=poke_df_obj.poke_df
    pokedex_data=[]
    for row in poke_df.iterrows():
        row_data=row[1]
        gen_name=row_data['gen_name']
        pokemon_name=row_data['name']
        japanese_name=row_data['japanese_name']
        pokedex_num=row_data['pokedex_number']
        height=row_data['height_m']
        weight=row_data['weight_kg']
        type_1=row_data['type1']
        type_2=row_data['type2']
        hp=row_data['hp']
        attack=row_data['attack']
        defense=row_data['defense']
        sp_atk=row_data['sp_attack']
        sp_def=row_data['sp_defense']
        speed=row_data['speed']
        #

        pokedex_data.append(
        Pokemon(
            pokemon_name=pokemon_name,
            poke_japanese_name=japanese_name,
            pokedex_number=pokedex_num,
            stats_abilities=[PokeStats(
                hp=hp,
                attack=attack,
                defense=defense,
                sp_attack=sp_atk,
                sp_defense=sp_def,
                speed=speed
            
            )])
        )
    return (
        Generation(
        generation_name=gen_name,
        pokemon=pokedex_data
        )
    )

poke_df_obj=poke_data_transform('pokemon.csv')
poke_df_obj.set_region_name()
poke_df_obj.add_points('gen_name')
# print(process_pokedex())
print(type(process_pokedex()))

if __name__ == "__main__":
    poke_df_obj=poke_data_transform('pokemon.csv')
    poke_df_obj.set_region_name()
    # processed_pokedex=poke_df_obj.process_pokedex()
    # print(process_pokedex())
    # print(processed_pokedex)
    # print(type(processed_pokedex[0]))
    b=10
