from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def random_forest_model (X, y) :
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)

    regression = RandomForestRegressor()
    regression.fit(X_train,y_train)

    regression.predict(X_test)

    return regression.score(X_test, y_test)


def linear_regression_model (X, y) :
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)  
    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)
    regression = LinearRegression()
    regression.fit(X_train, y_train)

    plt.scatter(X_train, y_train)
    plt.plot(X_train,regression.predict(X_train), color='red')
    plt.title("Living_Area VS Price (Training set)")
    plt.ylabel("Living_Area")
    plt.xlabel("Price")
    plt.xlim(0,1001000)
    plt.ylim(0,400)
    plt.savefig("./model_training/graphs/Living_Arae_VS_Price_Linear.png")

    regression.predict(X_test)
    
    return regression.score(X_test, y_test)


