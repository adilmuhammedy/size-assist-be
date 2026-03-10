import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load whitespace-separated CSV
data = pd.read_csv(
    "../data/body_data2.csv",
    sep=r"\s+",
    engine="python",
    skiprows=1,
    names=["height", "weight", "gender", "chest", "waist", "shoulder"]
)
data = data.dropna()
# Features & target
X = data[["height", "weight","gender"]]
y = data[["chest", "waist", "shoulder"]]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultiOutputRegressor(GradientBoostingRegressor(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05
))
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print("Mean Absolute Error:", round(error, 2))

# Save
joblib.dump(model, "body_model2.pkl")
print("Model saved!")