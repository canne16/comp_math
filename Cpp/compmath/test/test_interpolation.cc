#include <gtest/gtest.h>

#include <iostream>
#include <cmath>

#include "interpolation.hh"
#include "export_data.hh"


double function(double x) {
    return std::pow(std::sin(std::pow(x,2)),2) / x;
}

TEST(InterpolTest, Interp_Lag_Newt) {
    
    std::vector<double> x_points(10); // Точки узлов сетки
    std::vector<double> y_points(10); // Значения функции в узлах

    double step = (M_PI - 0.01) / 9;
    for (size_t i = 0; i < 10; ++i) {
        x_points[i] = 0.01 + i * step;
        y_points[i] = function(x_points[i]);
    }

    std::vector<double> x_vals(1000);
    std::vector<double> y_vals_lagr(1000);
    std::vector<double> y_vals_newt(1000);

    auto lagrange_function = compmath::interpolate_lagrange(x_points, y_points);
    auto newton_function = compmath::interpolate_newton(x_points, y_points);
    
    step = (M_PI - 0.01) / 999;
    for (size_t i = 0; i < 1000; ++i) {
        x_vals[i] = 0.01 + i * step;
        y_vals_lagr[i] = lagrange_function(x_vals[i]);
        y_vals_newt[i] = newton_function(x_vals[i]);
    }

    compmath::export_data_to_csv("initial_data.csv", x_points, y_points);
    compmath::export_data_to_csv("lagrange.csv", x_vals, y_vals_lagr);
    compmath::export_data_to_csv("newton.csv", x_vals, y_vals_newt);

    
}
