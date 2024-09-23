import numpy as np
import matplotlib.pyplot as plt
import Color_convertation as conv

R = 1
lambda_mono = 380 * 1e-9
lambda0 = 565 * 1e-9
delta_lambda = 200 * 1e-9
n2 = 1
n1 = 1.5

if lambda_mono < 380 * 1e-9 or lambda0 < 380 * 1e-9:
    print("Введите длины волн в видимом диапозоне от 380 до 780")
    exit(1)
elif lambda_mono > 780 * 1e-9 or lambda0 > 780 * 1e-9:
    print("Введите длины волн в видимом диапозоне от 380 до 780")
    exit(1)

r_m = np.sqrt(10 * lambda_mono * R / n2)
r_array_1 = np.linspace(0, r_m, 1000)
r_d = np.sqrt((R * lambda0 * (2 * lambda0 - delta_lambda)) / (2 * delta_lambda))
r_array_2 = np.linspace(0, r_d, 1000)

def intens_mono(lambda_, r):
    return np.cos((np.pi * n2 * r ** 2) / (R * lambda_) + np.pi / 2) ** 2

I_mono_arr = np.array([intens_mono(lambda_=lambda_mono, r=r) for r in r_array_1])

def mono_rings(obj, title):
    rgb = conv.color_convertation(lambda_mono)
    for I, r in zip(I_mono_arr, r_array_1):
        circle = plt.Circle((0, 0), r, edgecolor=rgb, alpha=I, fill=False, lw=0.5)
        obj.add_patch(circle)

    obj.set_title(title)
    obj.set_xlim(-r_m, r_m)
    obj.set_ylim(-r_m, r_m)
    obj.set_facecolor('black')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)


def mono_density(obj, title):
    rgb = conv.color_convertation(lambda_mono)
    obj.plot(r_array_1, I_mono_arr, color=rgb)
    obj.set_title(title)
    obj.set_xlabel('r')
    obj.set_ylabel('I')
    obj.grid(True)

def intens_quasimono(lambda_c, delta_lambda_, r):
    R_cf = ((n2 - n1) / (n2 + n1)) ** 2
    T_cf = 4 * n1 * n2 / ((n2 + n1) ** 2)
    return R_cf * (T_cf ** 2 + 1 + 2 * T_cf * np.sinc((np.pi * delta_lambda_ * r ** 2) / (lambda_c ** 2 * R) + np.pi / 2) * np.cos(2 * np.pi * r ** 2 / (lambda_c * R) + np.pi / 2))

I_q_arr = np.array([intens_quasimono(lambda0, delta_lambda, r=r) for r in r_array_2])

def quasi_rings(obj, title):
    wave = np.linspace(lambda0 - delta_lambda / 2, lambda0 + delta_lambda / 2, num=len(r_array_2))
    for I, r, wl in zip(I_q_arr, r_array_2, wave):
        rgb = conv.color_convertation(wl)
        circle = plt.Circle((0, 0), r, edgecolor=rgb, alpha=I, fill=False, lw=0.5)
        obj.add_patch(circle)
    obj.set_title(title)
    obj.set_xlim(-r_d, r_d)
    obj.set_ylim(-r_d, r_d)
    obj.set_facecolor('black')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(False)

def quasi_density(obj, title):
    rgb = conv.color_convertation(lambda0)
    obj.plot(r_array_2, I_q_arr, color=rgb)
    obj.set_title(title)
    obj.set_xlabel('r')
    obj.set_ylabel('I')
    obj.grid(True)


fig, obj = plt.subplots(1, 2, figsize=(14, 8))
mono_rings(obj[0], 'Кольца Ньютона в монохроматическом свете')
quasi_rings(obj[1], 'Кольца Ньютона в квазимонохроматическом свете')
plt.tight_layout()
plt.show()


fig, obj = plt.subplots(1, 2, figsize=(14, 8))
mono_density(obj[0], 'Интенсивность в монохроматическом свете')
quasi_density(obj[1], 'Интенсивность в квазимонохроматическом свете')
plt.tight_layout()
plt.show()