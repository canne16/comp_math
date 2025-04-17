#include <utility>
#include <iostream>

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

int main(){

    double h = 0.01;
    int NUM_POINTS = 1000;
    
    std::vector<double> x_points {};
    std::vector<double> function_values {};
    std::vector<double> true_derivative {};
    std::vector<double> true_second_derivative {};

    for (int i = 0; i < NUM_POINTS; i++) {
        x_points.push_back(i*h);
        function_values.push_back(funtion(i*h));
        true_derivative.push_back(derivative_function(i*h));
        true_second_derivative.push_back(second_derivative_function(i*h));
    }

    std::vector<double> derivative = compmath::differentiate(function_values, h, 4);
    std::vector<double> second_derivative = compmath::differentiate_twice(function_values, h, 2);

    compmath::export_data_to_csv("function.csv", x_points, function_values);
    compmath::export_data_to_csv("true_der.csv", x_points, true_derivative);
    compmath::export_data_to_csv("true_sec_der.csv", x_points, true_second_derivative);

    compmath::export_data_to_csv("derivative.csv", x_points, derivative);
    compmath::export_data_to_csv("sec_der.csv", x_points, second_derivative);

    return 0;
}