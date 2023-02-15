import pickle
import os

def predict(df, model_type) :
    try :
        with open(os.path.join(os.path.abspath('project/model'), model_type), 'rb') as f:
            model = pickle.load(f)

        return {'prediciton' : model.predict(df), 'status_code' : 0}
    except :
        return {'prediciton' : 0, 'status_code' : 1}
