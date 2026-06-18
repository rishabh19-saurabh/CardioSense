import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import joblib

print("1. Loading local data...")
df = pd.read_csv('heart.csv')

print("2. Scaling features...")
scal = MinMaxScaler()
feat = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
df[feat] = scal.fit_transform(df[feat])

print("3. Training the model...")
y = df["target"]
X = df.drop('target', axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=0)

Knn_clf = KNeighborsClassifier(n_neighbors=7)
Knn_clf.fit(X_train, Y_train)

print("4. Saving modern heartmodel.pkl...")
joblib.dump(Knn_clf, 'heartmodel.pkl')
print("DONE! You can now run the app.")
