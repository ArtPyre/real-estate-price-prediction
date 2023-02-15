import json
import pandas as pd

def preprocess(datas):
    df = pd.DataFrame.from_dict([datas])

    df = df.replace({"property-type":{"APARTMENT": 1, "HOUSE": 3}})
    df = df.replace({"furnished": {False: 0, "furnished": 1}})
    df = df.replace({"open-fire": {False: 0, "open-fire": 1}})
    df = df.replace({"terrace": {False: 0, "terrace": 1}})
    df = df.replace({"garden": {False: 0, "garden": 1}})
    df = df.replace({"swimming-pool": {False: 0, "swimming-pool": 1}})
    df = df.replace({"building-state":{"" : 0,"NEW": 1, "JUST RENOVATED": 2, "GOOD": 4, "TO RENOVATE": 5, "TO REBUILD": 6}})
    
    df_model = pd.DataFrame()
    df_model['Locality'] = df['zip-code']
    df_model['Type_of_property'] = df['property-type']
    df_model['Number_of_rooms'] = df['rooms-number']
    df_model['Living_Area'] = df['area']
    df_model['Furnished'] = df['furnished']
    df_model['Open_fire'] = df['open-fire']
    df_model['Terrace'] = df['terrace']
    df_model['Terrace_Area'] = df['terrace-area']
    df_model['Garden'] = df['garden']
    df_model['Garden_Area'] = df['garden-area']
    df_model['Surface_area_of_the_plot_of_land'] = df['land-area']
    df_model['Number_of_facades'] = df['facades-number']
    df_model['Swimming_pool'] = df['swimming-pool']
    df_model['State_of_the_building'] = df['building-state']

    return df_model
    