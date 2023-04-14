import pandas as pd
import pymysql
from sqlalchemy import create_engine

DRAFT_DATA_DIR = "../draft_out"
COMBINE_DATA_DIR = "../combine_out"

START_YEAR = 2000
END_YEAR = 2022

def insert_into_sql():
    draft, combine = combine_datasets()

    e = create_engine('mysql+pymysql://root:root@localhost/combine')

    combine = combine[['player_index', 'fourty_yard_dash', 'vertical', 'bench', 'broad_jump', 'cone_drill', 'shuttle']].fillna(0)

    print(combine.head())

    draft.to_sql('draft', con=e, index=False)
    combine.to_sql('combine', con=e, index=False)


def combine_datasets():
    new_draft_df = pd.DataFrame()
    new_combine_df = pd.DataFrame()
    player_idx = 0

    for year in range(START_YEAR, END_YEAR + 1):
        draft_file = f"{DRAFT_DATA_DIR}/{year}_draft.csv"
        combine_file = f"{COMBINE_DATA_DIR}/{year}_combine.csv"

        draft_df = pd.read_csv(draft_file)
        combine_df = pd.read_csv(combine_file)

        for _, row in draft_df.iterrows():
            pred = combine_df.loc[(combine_df["Player"] == row["Player"]) & (combine_df["Pos"] == row["Pos"])]

            if not pred.empty:
                new_draft_row = {
                    'id': player_idx,
                    'name': [row["Player"]], 
                    'position': [row["Pos"]], 
                    'college': [pred["School"].to_string(index=False)],
                    'round': [row["Rnd"]],
                    'pick': [row["Pick"]],
                    'year': year,
                    'age': [row["Age"]],
                    'height': [pred["Ht"].to_string(index=False)],
                    'weight': [pred["Wt"].to_string(index=False)],
                }

                fourty_yd = float(pred["40yd"].to_string(index=False))
                vertical = float(pred["Vertical"].to_string(index=False))
                bench = float(pred["Bench"].to_string(index=False))
                broad_jump = float(pred["Broad Jump"].to_string(index=False))
                cone_drill = float(pred["3Cone"].to_string(index=False))
                shuttle = float(pred["Shuttle"].to_string(index=False))

                new_combine_row = {
                    'player_index': player_idx,
                    'fourty_yard_dash': [fourty_yd],
                    'vertical': [vertical],
                    'bench': [bench],
                    'broad_jump': [broad_jump],
                    'cone_drill': [cone_drill],
                    'shuttle': [shuttle]
                }

                _draft_df = pd.DataFrame(new_draft_row)
                _combine_df = pd.DataFrame(new_combine_row)

                new_draft_df = pd.concat([new_draft_df, _draft_df])
                new_combine_df = pd.concat([new_combine_df, _combine_df])

                player_idx += 1


    return new_draft_df, new_combine_df

if __name__ == '__main__':
    insert_into_sql()
