import numpy as np
from sklearn.preprocessing import PolynomialFeatures

def tricubic(x):
    y = np.zeros_like(x)
    idx = (x >= 0) & (x <= 1)
    y[idx] = np.power(1.0 - np.power(np.abs(x[idx]), 3), 3)
    return y

class Loess:

    @staticmethod
    def standarize_data(data):
        data_mean = data.mean(0)
        data_std = data.std(0)
        return (data - data_mean) / data_std, data_mean, data_std

    def __init__(self, xx, yy, degree):
        xx = np.array(xx)
        yy = np.array(yy)
        self.s_xx, self.mean_xx, self.std_xx = self.standarize_data(xx)
        self.s_yy, self.mean_yy, self.std_yy = self.standarize_data(yy)
        self.degree = degree

    def reset_xx(self, xx):
        xx = np.array(xx)
        self.s_xx, self.mean_xx, self.std_xx = self.standarize_data(xx)

    def reset_yy(self, yy):
        yy = np.array(yy)
        self.s_yy, self.mean_yy, self.std_yy = self.standarize_data(yy)

    def reset_degree(self, degree):
        self.degree = degree

    @staticmethod
    def get_weights(distances, min_range):
        max_distance = max(distances[min_range])
        weights = tricubic(distances[min_range] / max_distance)
        return weights

    def standarize_x(self, value):
        return (value - self.mean_xx) / self.std_xx

    def destandarize_y(self, value):
        return value * self.std_yy + self.mean_yy

    def estimate(self, x, f):
        q = int(len(self.s_xx) * f)

        s_x = self.standarize_x(x)
        distances = np.linalg.norm(self.s_xx - s_x, axis=1)
        min_idx = np.argsort(distances)[:q]

        weights = self.get_weights(distances, min_idx)
        wm = np.diag(weights)
        
        xm = self.s_xx[min_idx]
        ym = self.s_yy[min_idx]

        poly = PolynomialFeatures(degree=self.degree)
        xm = poly.fit_transform(xm)
        xp = poly.fit_transform(s_x.reshape(1, -1))[0]

        xmt_wm = xm.T @ wm
        beta = np.linalg.pinv(xmt_wm @ xm) @ xmt_wm @ ym
        y = beta.T @ xp
        return self.destandarize_y(y)[0]
