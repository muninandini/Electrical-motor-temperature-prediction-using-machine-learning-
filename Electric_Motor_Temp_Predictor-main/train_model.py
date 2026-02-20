import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

from sklearn.metrics import r2_score, mean_squared_error

# ===============================
# 1️⃣ LOAD DATASET
# ===============================
data = pd.read_csv("data/measures_v2.csv")

# ===============================
# 2️⃣ REDUCE DATASET SIZE (30,000)
# ===============================
data = data.sample(n=30000, random_state=42)

# ===============================
# 3️⃣ PREPROCESSING
# ===============================

# Remove profile_id (not useful for prediction)
data = data.drop("profile_id", axis=1)

# Remove missing values if any
data = data.dropna()

# ===============================
# 4️⃣ FEATURES & TARGET
# ===============================

# Target = Permanent Magnet Temperature (pm)
X = data.drop("pm", axis=1)
y = data["pm"]

# ===============================
# 5️⃣ FEATURE SCALING
# ===============================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler
pickle.dump(scaler, open("model/scaler.pkl", "wb"))

# ===============================
# 6️⃣ TRAIN TEST SPLIT
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ===============================
# 7️⃣ MODELS (ONLY REQUIRED FOUR)
# ===============================

models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(),
    "Random Forest": RandomForestRegressor(),
    "SVM": SVR(kernel="linear")   # Faster SVM
}

best_model = None
best_score = -999
best_name = ""

# ===============================
# 8️⃣ TRAIN & SELECT BEST MODEL
# ===============================

for name, model in models.items():

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = mse ** 0.5

    print(f"{name} → R2: {r2:.4f}, RMSE: {rmse:.4f}")

    if r2 > best_score:
        best_score = r2
        best_model = model
        best_name = name

print("\n✅ BEST MODEL:", best_name)

# ===============================
# 9️⃣ SAVE FINAL MODEL
# ===============================

pickle.dump(best_model, open("model/best_motor_model.pkl", "wb"))

print("🎯 Best model saved successfully!")
