import numpy as np
import pandas as pd
import Loess

df = pd.DataFrame(columns=['x', 'y'])
res = 50

x = np.linspace(-5, 5, res)
y = np.linspace(-5, 5, res)
xx, yy = np.meshgrid(x, y)
df["x"] = xx.flatten()
df["y"] = yy.flatten()

surfaces = {
    "plane": lambda x, y: -3 * x + y,
    "saddle": lambda x, y: (x**2) - (y**2),
    "cubic": lambda x, y: -(x**3) + y,
    "absolute": lambda x, y: abs(x) + abs(y)
}

def add_surface(df, xx, yy, name, f):
    zz = f(xx, yy)
    df[name] = zz.flatten()
    noise = np.random.normal(0, zz.std() * .5, zz.shape)
    zz = zz + noise
    df[f"{name}_noise"] = zz.flatten()

for name, f in surfaces.items():
    add_surface(df, xx, yy, name, f)

def add_estimations(loess, df, name, f):
    X = df[["x", "y"]]
    estimations_1 = []
    estimations_2 = []
    for i in range(len(X)):
        Y = df[[f"{name}_noise"]]
        loess.reset_yy(Y)
        x = np.array(X.iloc[i])
        loess.reset_degree(1)
        estimations_1.append(loess.estimate(x, f))
        loess.reset_degree(2)
        estimations_2.append(loess.estimate(x, f))
    df[f"estimation_{name}_{f}_1"] = estimations_1
    df[f"estimation_{name}_{f}_2"] = estimations_2

fs = [0.1, 0.5, 1]
X = df[["x", "y"]]
loess = Loess.Loess(X, df[["plane"]], 1)
for f in fs:
    print(f)
    for surface in surfaces:
        print(surface)
        add_estimations(loess, df, surface, f)

df.to_csv("synthetic_data.csv", index=False)