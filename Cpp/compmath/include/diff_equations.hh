#pragma once

#include <vector>
#include <functional>
#include <cmath>
#include <stdexcept>

namespace compmath {

/**
 * @brief Solves an ODE system using the Euler method (1st order).
 * 
 * @tparam T Numeric type (e.g., double, float)
 * @param f The right-hand side function: f(t, state) -> std::vector<T>
 * @param f_t0 Initial state vector at t1
 * @param t1 Initial time
 * @param t2 Final time
 * @param h Step size
 * @return std::vector<std::vector<T>> Solution at each time step
 */
template <typename T, typename Func>
std::vector<std::vector<T>> solve_diff_euler(
    Func f,
    const std::vector<T>& f_t0,
    T t1,
    T t2,
    T h
) {
    size_t num_steps = static_cast<size_t>((t2 - t1) / h);
    std::vector<std::vector<T>> solution(num_steps + 1, f_t0);
    solution[0] = f_t0;
    T t = t1;
    for (size_t step = 1; step <= num_steps; ++step) {
        solution[step] = solution[step - 1] + h * f(t, solution[step - 1]);
        t += h;
    }
    return solution;
}

/**
 * @brief Solves an ODE system using the Trapezoidal method (2nd order).
 * 
 * @tparam T Numeric type
 * @param f The right-hand side function: f(t, state) -> std::vector<T>
 * @param f_t0 Initial state vector at t1
 * @param t1 Initial time
 * @param t2 Final time
 * @param h Step size
 * @return std::vector<std::vector<T>> Solution at each time step
 */
template <typename T, typename Func>
std::vector<std::vector<T>> solve_diff_trapez(
    Func f,
    const std::vector<T>& f_t0,
    T t1,
    T t2,
    T h
) {
    size_t num_steps = static_cast<size_t>((t2 - t1) / h);
    std::vector<std::vector<T>> solution(num_steps + 1, f_t0);
    solution[0] = f_t0;
    T t = t1;
    for (size_t step = 1; step <= num_steps; ++step) {
        auto predicted = solution[step - 1] + h * f(t, solution[step - 1]);
        solution[step] = solution[step - 1] + (h/2) * (f(t, solution[step - 1]) + f(t + h, predicted));
        t += h;
    }
    return solution;
}

/**
 * @brief Solves an ODE system using the 4th order Runge-Kutta method.
 * 
 * @tparam T Numeric type
 * @param f The right-hand side function: f(t, state) -> std::vector<T>
 * @param f_t0 Initial state vector at t1
 * @param t1 Initial time
 * @param t2 Final time
 * @param h Step size
 * @return std::vector<std::vector<T>> Solution at each time step
 */
template <typename T, typename Func>
std::vector<std::vector<T>> runge_kutta(
    Func f,
    const std::vector<T>& f_t0,
    T t1,
    T t2,
    T h
) {
    size_t num_steps = static_cast<size_t>((t2 - t1) / h);
    std::vector<std::vector<T>> solution(num_steps + 1, f_t0);
    solution[0] = f_t0;
    T time = t1;
    for (size_t step = 1; step <= num_steps; ++step) {
        const auto& y = solution[step - 1];
        auto k1 = f(time, y);
        std::vector<T> yk2(y.size());
        for (size_t i = 0; i < y.size(); ++i)
            yk2[i] = y[i] + h / 2 * k1[i];
        auto k2 = f(time + h / 2, yk2);
        std::vector<T> yk3(y.size());
        for (size_t i = 0; i < y.size(); ++i)
            yk3[i] = y[i] + h / 2 * k2[i];
        auto k3 = f(time + h / 2, yk3);
        std::vector<T> yk4(y.size());
        for (size_t i = 0; i < y.size(); ++i)
            yk4[i] = y[i] + h * k3[i];
        auto k4 = f(time + h, yk4);
        solution[step] = y;
        for (size_t i = 0; i < y.size(); ++i)
            solution[step][i] += (h / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]);
        time += h;
    }
    return solution;
}

} // namespace compmath