import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from scipy.stats import linregress

def analytical_solution(alpha, x, t):
    return np.sin(np.pi * x) * np.exp(-alpha * np.pi**2 * t)

def solve_transport_equation(alpha, Nx, Nt, theta):
    L = 1.0
    T = 0.5
    dx = L / Nx
    dt = T / Nt
    r = alpha * dt / dx**2

    x = np.linspace(0, L, Nx + 1)
    t = np.linspace(0, T, Nt + 1)

    u = np.zeros((Nx + 1, Nt + 1))
    u[:, 0] = np.sin(np.pi * x)

    A = np.zeros((Nx - 1, Nx - 1))
    B = np.zeros((Nx - 1, Nx - 1))

    for i in range(Nx - 1):
        A[i, i] = 1 + 2 * r * theta
        B[i, i] = 1 - 2 * r * (1 - theta)
        if i > 0:
            A[i, i - 1] = -r * theta
            B[i, i - 1] = r * (1 - theta)
        if i < Nx - 2:
            A[i, i + 1] = -r * theta
            B[i, i + 1] = r * (1 - theta)

    for n in range(Nt):
        b = B @ u[1:-1, n]
        u_inner = solve(A, b)
        u[1:-1, n + 1] = u_inner

    return u, x, t

def calculate_order_theta(alpha, thetas):
    fig, axes = plt.subplots(len(thetas), 2, figsize=(14, 5 * len(thetas)))
    if len(thetas) == 1:
        axes = np.array([axes])

    for idx, theta in enumerate(thetas):
        if theta == 0.0:
            Nx_values = [10, 20, 40, 80]
            dx_values = [1.0 / Nx for Nx in Nx_values]
            dt_values = [0.4 * dx**2 / alpha for dx in dx_values]
            Nt_values = [int(0.5 / dt) for dt in dt_values]
        if theta == 0.5:
            Nx_values = [10, 20, 40, 80]
        if theta == 0.7:
            Nx_values = [10, 20, 40, 80]
        if theta == 1.0:
            Nx_values = [10, 20, 40, 80]

        if theta == 0.5:
            Nt_values = [20, 40, 80, 160]
        if theta == 0.7:
            Nt_values = [200, 3200, 6400, 12800]
        if theta == 1.0:
            Nt_values = [200, 3200, 6400, 12800]
    
        L = 1.0
        T = 0.5
        dx_values = [L / Nx for Nx in Nx_values]
        dt_values = [T / Nt for Nt in Nt_values]
        error_norms = []

        for k in range(4):
            Nx = Nx_values[k]
            Nt = Nt_values[k]
            u_num, x, t = solve_transport_equation(alpha, Nx, Nt, theta=theta)
            u_exact = np.zeros_like(u_num)

            # for i in range(Nx + 1):
            #     for j in range(Nt + 1):
            #         u_exact[i, j] = analytical_solution(alpha, x[i], t[j])

            u_exact_T = analytical_solution(alpha, x, T)
            u_num_T = u_num[:, -1]

            error = np.abs(u_exact_T - u_num_T)
            error_norm = np.max(error)
            error_norms.append(error_norm)

            # error = np.abs(u_exact - u_num)
            # error_norm = np.linalg.norm(error, ord=1) / (Nt * Nx)
            # error_norms.append(error_norm)

        log_dx = np.log(dx_values)
        log_dt = np.log(dt_values)
        log_err = np.log(error_norms)
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from scipy.stats import linregress

def analytical_solution(alpha, x, t):
    return np.sin(np.pi * x) * np.exp(-alpha * np.pi**2 * t)

def solve_transport_equation(alpha, Nx, Nt, theta):
    L = 1.0
    T = 0.5
    dx = L / Nx
    dt = T / Nt
    r = alpha * dt / dx**2

    x = np.linspace(0, L, Nx + 1)
    t = np.linspace(0, T, Nt + 1)

    u = np.zeros((Nx + 1, Nt + 1))
    u[:, 0] = np.sin(np.pi * x)

    A = np.zeros((Nx - 1, Nx - 1))
    B = np.zeros((Nx - 1, Nx - 1))

    for i in range(Nx - 1):
        A[i, i] = 1 + 2 * r * theta
        B[i, i] = 1 - 2 * r * (1 - theta)
        if i > 0:
            A[i, i - 1] = -r * theta
            B[i, i - 1] = r * (1 - theta)
        if i < Nx - 2:
            A[i, i + 1] = -r * theta
            B[i, i + 1] = r * (1 - theta)

    for n in range(Nt):
        b = B @ u[1:-1, n]
        u_inner = solve(A, b)
        u[1:-1, n + 1] = u_inner

    return u, x, t

def calculate_order_theta(alpha, thetas):
    fig, axes = plt.subplots(len(thetas), 2, figsize=(14, 5 * len(thetas)))
    if len(thetas) == 1:
        axes = np.array([axes])

    for idx, theta in enumerate(thetas):
        if theta == 0.0:
            Nx_values = [10, 20, 40, 80]
            dx_values = [1.0 / Nx for Nx in Nx_values]
            dt_values = [0.4 * dx**2 / alpha for dx in dx_values]
            Nt_values = [int(0.5 / dt) for dt in dt_values]
        if theta == 0.5:
            Nx_values = [10, 20, 40, 80]
        if theta == 0.7:
            Nx_values = [10, 20, 40, 80]
        if theta == 1.0:
            Nx_values = [10, 20, 40, 80]

        if theta == 0.5:
            Nt_values = [20, 40, 80, 160]
        if theta == 0.7:
            Nt_values = [200, 3200, 6400, 12800]
        if theta == 1.0:
            Nt_values = [200, 3200, 6400, 12800]
    
        L = 1.0
        T = 0.5
        dx_values = [L / Nx for Nx in Nx_values]
        dt_values = [T / Nt for Nt in Nt_values]
        error_norms = []

        for k in range(4):
            Nx = Nx_values[k]
            Nt = Nt_values[k]
            u_num, x, t = solve_transport_equation(alpha, Nx, Nt, theta=theta)
            u_exact = np.zeros_like(u_num)

            # for i in range(Nx + 1):
            #     for j in range(Nt + 1):
            #         u_exact[i, j] = analytical_solution(alpha, x[i], t[j])

            u_exact_T = analytical_solution(alpha, x, T)
            u_num_T = u_num[:, -1]

            error = np.abs(u_exact_T - u_num_T)
            error_norm = np.max(error)
            error_norms.append(error_norm)

            # error = np.abs(u_exact - u_num)
            # error_norm = np.linalg.norm(error, ord=1) / (Nt * Nx)
            # error_norms.append(error_norm)

        log_dx = np.log(dx_values)
        log_dt = np.log(dt_values)
        log_err = np.log(error_norms)

        coeffsx = linregress(log_dx, log_err)
        coeffst = linregress(log_dt, log_err)
        # order_x = coeffsx[0] / 2
        # if (theta != 0.5):
        #     order_t = coeffst[0] / 2
        # else:
        #     order_t = coeffst[0]

        order_x = coeffsx[0]
        order_t = coeffst[0]

        axes[idx, 0].plot(log_dx, log_err, 'o-', label='Ошибка по dx')
        axes[idx, 0].plot(log_dx, coeffsx[0]*log_dx + coeffsx[1], '--', label=f'Наклон: {order_x:.2f}')
        axes[idx, 0].set_title(f'θ = {theta} — Порядок по x: {order_x:.2f}')
        axes[idx, 0].set_xlabel('log(dx)')
        axes[idx, 0].set_ylabel('log(ошибка)')
        axes[idx, 0].legend()
        axes[idx, 0].grid()

        axes[idx, 1].plot(log_dt, log_err, 'o-', label='Ошибка по dt')
        axes[idx, 1].plot(log_dt, coeffst[0]*log_dt + coeffst[1], '--', label=f'Наклон: {order_t:.2f}')
        axes[idx, 1].set_title(f'θ = {theta} — Порядок по t: {order_t:.2f}')
        axes[idx, 1].set_xlabel('log(dt)')
        axes[idx, 1].set_ylabel('log(ошибка)')
        axes[idx, 1].legend()
        axes[idx, 1].grid()

        print(f"θ = {theta}: порядок по x = {order_x:.2f}, порядок по t = {order_t:.2f}")

    plt.tight_layout()
    plt.savefig('Lab2_order.png')

calculate_order_theta(alpha=1.0, thetas=[0.0, 0.5, 1.0])

def plot_solutions_for_thetas(alpha, thetas, Nx=50, Nt=1000):
    x = np.linspace(0, 1, Nx + 1)
    t_indices = [0, Nt // 4, Nt // 2, Nt]
    t_values = [0.5 * i / Nt for i in t_indices]

    fig, axes = plt.subplots(len(thetas), 1, figsize=(10, 4 * len(thetas)))

    if len(thetas) == 1:
        axes = [axes]

    for idx, theta in enumerate(thetas):
        u_num, x, t = solve_transport_equation(alpha, Nx, Nt, theta=theta)
        for ti, t_idx in enumerate(t_indices):
            u_exact = analytical_solution(alpha, x, t[t_idx])
            axes[idx].plot(x, u_num[:, t_idx], label=f'Числ. t={t[t_idx]:.2f}', linestyle='-')
            axes[idx].plot(x, u_exact, label=f'Аналит. t={t[t_idx]:.2f}', linestyle='--')

        axes[idx].set_title(f'θ = {theta}: решение в разные моменты времени')
        axes[idx].set_xlabel('x')
        axes[idx].set_ylabel('u(x, t)')
        axes[idx].legend()
        axes[idx].grid()

    plt.tight_layout()
    plt.savefig('Lab2_solution.png')

plot_solutions_for_thetas(alpha=1.0, thetas=[0.0, 0.5, 1.0], Nx=50, Nt=10000)
        coeffsx = linregress(log_dx, log_err)
        coeffst = linregress(log_dt, log_err)
        # order_x = coeffsx[0] / 2
        # if (theta != 0.5):
        #     order_t = coeffst[0] / 2
        # else:
        #     order_t = coeffst[0]

        order_x = coeffsx[0]
        order_t = coeffst[0]

        axes[idx, 0].plot(log_dx, log_err, 'o-', label='Ошибка по dx')
        axes[idx, 0].plot(log_dx, coeffsx[0]*log_dx + coeffsx[1], '--', label=f'Наклон: {order_x:.2f}')
        axes[idx, 0].set_title(f'θ = {theta} — Порядок по x: {order_x:.2f}')
        axes[idx, 0].set_xlabel('log(dx)')
        axes[idx, 0].set_ylabel('log(ошибка)')
        axes[idx, 0].legend()
        axes[idx, 0].grid()

        axes[idx, 1].plot(log_dt, log_err, 'o-', label='Ошибка по dt')
        axes[idx, 1].plot(log_dt, coeffst[0]*log_dt + coeffst[1], '--', label=f'Наклон: {order_t:.2f}')
        axes[idx, 1].set_title(f'θ = {theta} — Порядок по t: {order_t:.2f}')
        axes[idx, 1].set_xlabel('log(dt)')
        axes[idx, 1].set_ylabel('log(ошибка)')
        axes[idx, 1].legend()
        axes[idx, 1].grid()

        print(f"θ = {theta}: порядок по x = {order_x:.2f}, порядок по t = {order_t:.2f}")

    plt.tight_layout()
    plt.savefig('Lab2_order.png')

calculate_order_theta(alpha=1.0, thetas=[0.0, 0.5, 1.0])

def plot_solutions_for_thetas(alpha, thetas, Nx=50, Nt=1000):
    x = np.linspace(0, 1, Nx + 1)
    t_indices = [0, Nt // 4, Nt // 2, Nt]
    t_values = [0.5 * i / Nt for i in t_indices]

    fig, axes = plt.subplots(len(thetas), 1, figsize=(10, 4 * len(thetas)))

    if len(thetas) == 1:
        axes = [axes]

    for idx, theta in enumerate(thetas):
        u_num, x, t = solve_transport_equation(alpha, Nx, Nt, theta=theta)
        for ti, t_idx in enumerate(t_indices):
            u_exact = analytical_solution(alpha, x, t[t_idx])
            axes[idx].plot(x, u_num[:, t_idx], label=f'Числ. t={t[t_idx]:.2f}', linestyle='-')
            axes[idx].plot(x, u_exact, label=f'Аналит. t={t[t_idx]:.2f}', linestyle='--')

        axes[idx].set_title(f'θ = {theta}: решение в разные моменты времени')
        axes[idx].set_xlabel('x')
        axes[idx].set_ylabel('u(x, t)')
        axes[idx].legend()
        axes[idx].grid()

    plt.tight_layout()
    plt.savefig('Lab2_solution.png')

plot_solutions_for_thetas(alpha=1.0, thetas=[0.0, 0.5, 1.0], Nx=50, Nt=10000)