from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pyplot as plt
import pickle
import os


#Create a Random Forest Regressor and take the datas to make a model with this, 
#save a graph on the Linear Regression and return the score
def random_forest_model (X, y) :
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

    rfr = RandomForestRegressor()
    rfr.fit(X_train,y_train)
    y_pred = rfr.predict(X_test)

    pickel_path = os.path.join(os.path.abspath('project/model'), 'RFR_model.pkl')
    with open(pickel_path,'wb') as f:
        pickle.dump(rfr,f)


    plt.scatter(y_test, y_pred) 
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],color='r')
    plt.title("Correlation line")
    plt.ylabel("Price predicted")
    plt.xlabel("Price")
    plt.savefig("./model_training/graphs/RFR_Graph.png")
    plt.show()

    return rfr.score(X_test, y_test)

#Create a Gradient Boosting Regressor and take the datas to make a model with this, 
#save a graph on the Linear Regression and return the score
def gradient_boosting_regression_model (X, y) :
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2) 

    gdr = GradientBoostingRegressor()
    gdr.fit(X_train, y_train)
    y_pred = gdr.predict(X_test)

    pickel_path = os.path.join(os.path.abspath('project/model'), 'GDR_model.pkl')
    with open(pickel_path,'wb') as f:
        pickle.dump(gdr,f)

    plt.scatter(y_test, y_pred) 
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],color='r')
    plt.title("Correlation line")
    plt.ylabel("Price predicted")
    plt.xlabel("Price")
    plt.savefig("./model_training/graphs/GDR_Graph.png")
    plt.show()
    
    return gdr.score(X_test, y_test)


