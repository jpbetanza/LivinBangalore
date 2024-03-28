import json
import pickle
import os
import numpy as np

__current_dir =  None
__locations = None
__data_columns = None
__model = None


def get_prediction(location,sqft,bed,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index= __data_columns.index('other')
    print(loc_index)
    x = np.zeros(len(__data_columns))
    x[0]=bed
    x[1]=sqft
    x[2]=bath
    if loc_index>=0:
        x[loc_index]=1
    return __model.predict([x])[0]

def get_locations():
    return __locations

def load_saved_artifacts():
    print('Loading saved artifacts...')
    global __current_dir
    global __data_columns
    global __locations
    global __model

    __current_dir = os.path.dirname(os.path.abspath(__file__))

    print('Loading location columns...')
    with open(os.path.join(__current_dir, 'artifacts', 'model_cols.json'),'r') as f:
        __data_columns = json.load(f)['data_cols']
        __locations = __data_columns[3:]

    print('Loading model...')
    with open(os.path.join(__current_dir, 'artifacts', 'model.pkl'),'rb') as f:
        __model = pickle.load(f)
    
    print('Done loading artifacts!')

if __name__=="__main__":
    load_saved_artifacts()
    print(get_locations())
    print(get_prediction('1st Phase JP Nagar',1000,3,3))
    print(get_prediction('1st Phase JP Nagar',1000,2,2))
    print(get_prediction('1st Block jayanagar',1000,2,2))
    print(get_prediction('kalhalli',1000,2,2))
    print(get_prediction('Ejipura',1000,2,2))