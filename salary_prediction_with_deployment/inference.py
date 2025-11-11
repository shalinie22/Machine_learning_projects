import joblib

model = joblib.load("salary.pkl")
res = model.predict([[1,10]])

print(res)