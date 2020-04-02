import pandas as pd
import numpy as np

def get_rating_matrix(df):
    # indexes
    users = df['comment_user_id'].unique()
    galaxies = df['comment_focus_id'].unique()
#     print(len(users), len(galaxies))
    ratings = np.zeros((len(users), len(galaxies)))
    print(ratings.shape)
    
    for _, row in df.iterrows():
        try:
            cell_indices = get_rating_cell(row, users, galaxies)
            ratings[cell_indices] += 1
        except IndexError:
            print(row, cell_indices)
            raise IndexError
    return ratings


def get_rating_cell(response, users, galaxies):
    user_index = int(np.nonzero(users.squeeze() == response['comment_user_id'])[0])
    galaxy_index = int(np.nonzero(galaxies.squeeze() == response['comment_focus_id'])[0])
    return user_index, galaxy_index