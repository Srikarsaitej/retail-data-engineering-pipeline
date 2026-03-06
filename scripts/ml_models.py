import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score

# -------------------------
# Load Dataset
# -------------------------
df = pd.read_csv("data/transformed_retail.csv")

# Reduce dataset size for faster training
df = df.sample(20000, random_state=42)

print("Dataset loaded for ML models")

# -------------------------
# Features
# -------------------------
X = df[["Quantity", "Price", "Month"]]

# -------------------------
# Regression Target
# -------------------------
y_reg = df["TotalAmount"]

# -------------------------
# Train/Test Split (Regression)
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)

print("Data split completed")

# -------------------------
# 1️⃣ Linear Regression
# -------------------------
lr = LinearRegression()
lr.fit(X_train, y_train)

pred_lr = lr.predict(X_test)

print("\nLinear Regression")
print("MSE:", mean_squared_error(y_test, pred_lr))
print("R2:", r2_score(y_test, pred_lr))

# -------------------------
# 2️⃣ Decision Tree
# -------------------------
dt = DecisionTreeRegressor()
dt.fit(X_train, y_train)

pred_dt = dt.predict(X_test)

print("\nDecision Tree")
print("MSE:", mean_squared_error(y_test, pred_dt))
print("R2:", r2_score(y_test, pred_dt))

# -------------------------
# 3️⃣ Random Forest
# -------------------------
rf = RandomForestRegressor(n_estimators=100)
rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

print("\nRandom Forest")
print("MSE:", mean_squared_error(y_test, pred_rf))
print("R2:", r2_score(y_test, pred_rf))

# -------------------------
# 4️⃣ Support Vector Machine
# -------------------------
svm = SVR()
svm.fit(X_train, y_train)

pred_svm = svm.predict(X_test)

print("\nSupport Vector Machine")
print("MSE:", mean_squared_error(y_test, pred_svm))
print("R2:", r2_score(y_test, pred_svm))

# -------------------------
# 5️⃣ Naive Bayes (Classification)
# -------------------------

# Convert TotalAmount to categories
df["SalesCategory"] = pd.cut(df["TotalAmount"], bins=3, labels=[0,1,2])

y_class = df["SalesCategory"]

# Train/Test split for classification
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X, y_class, test_size=0.2, random_state=42
)

nb = GaussianNB()
nb.fit(X_train_c, y_train_c)

pred_nb = nb.predict(X_test_c)

print("\nNaive Bayes (Sales Category Prediction)")
print("Accuracy:", accuracy_score(y_test_c, pred_nb))