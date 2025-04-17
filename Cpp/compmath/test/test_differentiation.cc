#include <gtest/gtest.h>

#include <iostream>
#include <cmath>

#include "norm.hh"
#include "differentiation.hh"
#include "export_data.hh"


double funtion(double x) {
    return x / (1 + pow(x, 3));
}

double derivative_function(double x) {
    return (1-2*pow(x, 3)) / pow((1 + pow(x, 3)), 2);
}

double second_derivative_function(double x) {
    return (6*pow(x,2)*(pow(x,3)-2)) / pow((1 + pow(x, 3)), 3);
}

TEST(DiffTest, Diff_check_order) {
    
    std::vector<double> errors_der_1_ord     {};
    std::vector<double> errors_der_2_ord     {};
    std::vector<double> errors_der_4_ord     {};
    std::vector<double> errors_sec_der_2_ord {};

    std::vector<double> x_points               {};
    std::vector<double> function_values        {};
    std::vector<double> true_derivative        {};
    std::vector<double> true_second_derivative {};

    std::vector<double> derivative_1_ord        {};
    std::vector<double> derivative_2_ord        {};
    std::vector<double> derivative_4_ord        {};
    std::vector<double> second_derivative_2_ord {};

    std::vector<double> h_vals {};
    double x_start = 1;
    double x_end   = 10;
    
    for (size_t i = 1; i < 22; i++){
        h_vals.push_back(pow(0.5, i));
    }

    for (size_t i = 0; i < h_vals.size(); i++) {
        double h = h_vals[i];

        for (double x = x_start; x < x_end+h; x += h){
            x_points.push_back(x);
            function_values.push_back(funtion(x));
            true_derivative.push_back(derivative_function(x));
            true_second_derivative.push_back(second_derivative_function(x));
        }

        derivative_1_ord.resize(function_values.size());
        derivative_2_ord.resize(function_values.size());
        derivative_4_ord.resize(function_values.size());
        second_derivative_2_ord.resize(function_values.size());

        derivative_1_ord = compmath::differentiate(function_values, derivative_1_ord, h, 1);
        derivative_2_ord = compmath::differentiate(function_values, derivative_2_ord, h, 2);
        derivative_4_ord = compmath::differentiate(function_values, derivative_4_ord, h, 4);
        second_derivative_2_ord = compmath::differentiate_twice(function_values, second_derivative_2_ord, h, 2);

        errors_der_1_ord.push_back(compmath::norm_inf(derivative_1_ord, true_derivative));
        errors_der_2_ord.push_back(compmath::norm_inf(derivative_2_ord, true_derivative));
        errors_der_4_ord.push_back(compmath::norm_inf(derivative_4_ord, true_derivative));
        errors_sec_der_2_ord.push_back(compmath::norm_inf(second_derivative_2_ord, true_second_derivative));

        x_points.clear();
        function_values.clear();
        true_derivative.clear();
        true_second_derivative.clear();
        derivative_1_ord.clear();
        derivative_2_ord.clear();
        derivative_4_ord.clear();
        second_derivative_2_ord.clear();

    }

    compmath::export_data_to_csv("errors_der_1_ord.csv", h_vals, errors_der_1_ord);
    compmath::export_data_to_csv("errors_der_2_ord.csv", h_vals, errors_der_2_ord);
    compmath::export_data_to_csv("errors_der_4_ord.csv", h_vals, errors_der_4_ord);
    compmath::export_data_to_csv("errors_sec_der_2_ord.csv", h_vals, errors_sec_der_2_ord);

}
