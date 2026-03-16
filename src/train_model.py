import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
data = pd.read_csv(
    "../data/body_data2.csv",
    sep=r"\s+",
    engine="python",
    skiprows=1,
    names=["height", "weight", "gender", "chest", "waist", "shoulder"]
)

data = data.dropna()

# Features and targets
X = data[["height", "weight", "gender"]]
y = data[["chest", "waist", "shoulder"]]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Pipeline: Scaling + Model
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", MultiOutputRegressor(
        GradientBoostingRegressor(
            n_estimators=300,
            max_depth=4,
            learning_rate=0.05
        )
    ))
])

# Train
pipeline.fit(X_train, y_train)

# Predict
predictions = pipeline.predict(X_test)

# Evaluate
error = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", round(error, 2))

# Save model
joblib.dump(pipeline, "body_model.pkl")

print("Model saved!")