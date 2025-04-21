#pragma once

#include <vector>
#include <stdexcept>
#include <cassert>
#include <cmath>
#include <functional>

/**
 * @file interpolation.hh
 * @brief Interpolation methods for numerical analysis.
 *
 * Provides functions to construct interpolating polynomials using Lagrange and Newton methods.
 */

namespace compmath {

/**
 * @brief Constructs a Lagrange interpolating polynomial.
 *
 * Given nodes (x_nodes) and their corresponding values (y_values), this function returns
 * a callable object representing the Lagrange interpolation polynomial.
 *
 * @tparam T Numeric type (e.g., double, float)
 * @param x_nodes Vector of x-coordinates of interpolation nodes
 * @param y_values Vector of y-coordinates (function values at nodes)
 * @return std::function<T(T)> Callable polynomial function
 * @throws std::invalid_argument if x_nodes and y_values have different sizes
 */
template <typename T>
std::function<T(T)> interpolate_lagrange(
    const std::vector<T>& x_nodes,
    const std::vector<T>& y_values
) {
    if (x_nodes.size() != y_values.size())
        throw std::invalid_argument("x_nodes and y_values must have the same size");

    size_t n = x_nodes.size();

    return [x_nodes, y_values, n](T x) -> T {
        T result = 0;
        for (size_t i = 0; i < n; ++i) {
            T term = y_values[i];
            for (size_t j = 0; j < n; ++j) {
                if (i != j) {
                    term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j]);
                }
            }
            result += term;
        }
        return result;
    };
}

/**
 * @brief Constructs a Newton interpolating polynomial.
 *
 * Given nodes (x_nodes) and their corresponding values (y_values), this function returns
 * a callable object representing the Newton interpolation polynomial.
 *
 * @tparam T Numeric type (e.g., double, float)
 * @param x_nodes Vector of x-coordinates of interpolation nodes
 * @param y_values Vector of y-coordinates (function values at nodes)
 * @return std::function<T(T)> Callable polynomial function
 * @throws std::invalid_argument if x_nodes and y_values have different sizes
 */
template <typename T>
std::function<T(T)> interpolate_newton(
    const std::vector<T>& x_nodes,
    const std::vector<T>& y_values
) {
    if (x_nodes.size() != y_values.size())
        throw std::invalid_argument("x_nodes and y_values must have the same size");

    size_t n = x_nodes.size();
    std::vector<T> coef = y_values;

    // Compute divided differences in-place
    for (size_t j = 1; j < n; ++j) {
        for (size_t i = n - 1; i >= j; --i) {
            coef[i] = (coef[i] - coef[i - 1]) / (x_nodes[i] - x_nodes[i - j]);
        }
    }

    return [x_nodes, coef, n](T x) -> T {
        T result = coef[n - 1];
        for (size_t i = n - 1; i-- > 0;) {
            result = result * (x - x_nodes[i]) + coef[i];
        }
        return result;
    };
}

}