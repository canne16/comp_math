#pragma once

#include <vector>
#include <stdexcept>
#include <cassert>
#include <cmath>
#include <functional>

namespace compmath {

/**
 * @brief Numerically integrate a function using the trapezoidal rule.
 * 
 * @note Order: 2
 * 
 * @tparam T Numeric type (e.g., double, float)
 * @tparam Func Callable type: T func(T)
 * @param func Function to integrate (can be a function pointer, lambda, or functor)
 * @param a Lower bound of integration
 * @param b Upper bound of integration
 * @param n Number of intervals (default: 1000)
 * @return Approximate value of the definite integral of func from a to b
 */
template <typename T, typename Func>
T integrate_trapez(
    Func func,                
    T a,                      
    T b,                      
    size_t n = 1000              
) {
    if (n == 0) throw std::invalid_argument("Number of intervals must be positive");
    T h = (b - a) / n;
    T result = 0;

    for (size_t i = 1; i < n; ++i) {
        T x = a + i * h;
        result += func(x);
    }

    result = (func(a) + 2 * result + func(b)) * h / 2;
    return result;
}
    

/**
 * @brief Numerically integrate a function using the rectangle (left, right, or midpoint) rule.
 * 
 * @note Order: 1 (left, right) / 2 (modpoint)
 * 
 * @tparam T Numeric type (e.g., double, float)
 * @tparam Func Callable type: T func(T)
 * @param func Function to integrate
 * @param a Lower bound of integration
 * @param b Upper bound of integration
 * @param n Number of intervals (default: 1000)
 * @param method Rectangle method: "left", "right", or "midpoint" (default: "left")
 * @return Approximate value of the definite integral of func from a to b
 * @throws std::invalid_argument if n == 0 or method is unknown
 */
template <typename T, typename Func>
T integrate_rect(
    Func func,
    T a,
    T b,
    size_t n = 1000,
    const std::string& method = "left"
) {
    if (n == 0) 
        throw std::invalid_argument("Number of intervals must be positive");

    T h = (b - a) / n;
    T result = 0;

    if (method == "left") {
        for (size_t i = 0; i < n; ++i) {
            T x = a + i * h;
            result += func(x);
        }
    } else if (method == "right") {
        for (size_t i = 1; i <= n; ++i) {
            T x = a + i * h;
            result += func(x);
        }
    } else if (method == "midpoint") {
        for (size_t i = 0; i < n; ++i) {
            T x = a + i * h + h / 2;
            result += func(x);
        }
    } else
        throw std::invalid_argument("Unknown rectangle method: " + method);

    return result * h;
}


/**
 * @brief Numerically integrate a function using Simpson's rule.
 * 
 * @note Order: 4
 * 
 * @tparam T Numeric type (e.g., double, float)
 * @tparam Func Callable type: T func(T)
 * @param func Function to integrate
 * @param a Lower bound of integration
 * @param b Upper bound of integration
 * @param n Number of intervals (must be even, default: 1000)
 * @return Approximate value of the definite integral of func from a to b
 * @throws std::invalid_argument if n == 0 or n is not even
 */
template <typename T, typename Func>
T integrate_simpson(
    Func func,
    T a,
    T b,
    size_t n = 1000
) {

    if (n == 0 || n % 2 != 0)
        throw std::invalid_argument("Number of intervals must be positive and even for Simpson's rule");

    T h = (b - a) / n;
    T result = func(a) + func(b);

    for (size_t i = 1; i < n; ++i) {
        T x = a + i * h;
        if (i % 2 == 0)
            result += 2 * func(x);
        else
            result += 4 * func(x);
    }

    return result * h / 3;
}


/**
 * @brief Estimate the integral and its error using Runge's rule.
 *
 * This function computes the integral of a function using a specified integration method
 * with two different numbers of intervals (n1 and n2), and estimates the error using Runge's rule.
 *
 * @tparam T Numeric type (e.g., double, float)
 * @tparam Func Callable type: T func(T)
 * @tparam Integrator Callable type for integration method: T integrator(Func, T, T, size_t)
 * @param integrator Integration method (e.g., integrate_simpson, integrate_trapez, integrate_rect)
 * @param func Function to integrate
 * @param a Lower bound of integration (specify type! ex: 3.0, not 3)
 * @param b Upper bound of integration (specify type! ex: 3.0, not 3)
 * @param n Number of intervals for the first estimate (result estimate will use 2*n)
 * @param order The order of the integration method (e.g., 2 for trapezoidal, 4 for Simpson)
 * @return std::pair<T, T> where first is the refined integral estimate (using n2), and second is the estimated error
 *
 * @note Example usage:
 * @code
 * auto [I2n, error] = compmath::runge_rule(
 *     compmath::integrate_simpson<double, decltype(f)>, f, 0.0, M_PI, 10, 4
 * );
 * @endcode
 */
template <typename T, typename Func, typename Integrator>
std::pair<T, T> runge_rule(
    Integrator integrator,
    Func func,
    T a,
    T b,
    size_t n,
    int order
) {
    T In  = integrator(func, a, b, n);
    T I2n = integrator(func, a, b, 2*n);
    T R = std::abs(I2n - In) / (std::pow(2, order) - 1);
    return {I2n, R};
}



}