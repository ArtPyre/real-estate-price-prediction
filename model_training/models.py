from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

def random_forest_model (X, y) :
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=41, test_size=0.2)

    regression = RandomForestRegressor()
    regression.fit(X_train.reshape(-1, 1),y_train)
    return regression.score(X_test.reshape(-1, 1), y_test)


def linear_regression_model (X, y) :
    X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=41, test_size=0.2)  

    regression = LinearRegression()
    regression.fit(X_train.reshape(-1, 1), y_train)
    return regression.score(X_test.reshape(-1, 1), y_test)

