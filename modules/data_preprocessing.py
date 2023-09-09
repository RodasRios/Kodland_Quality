from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

def preprocess_data(df):
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(df_scaled)
    df_scaled.columns = df.columns
    X = df_scaled.drop('Did the parent pay in the TC?',axis = 1)
    y = df_scaled['Did the parent pay in the TC?'].values

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 42)
    return X_train, X_test, y_train, y_test, X