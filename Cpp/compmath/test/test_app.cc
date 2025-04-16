#include <utility>
#include <iostream>

#include "gnuplot-iostream.h"
#include "differentiation.hh"
#include "export_data.hh"


double funtion(double x) {
    return 1 / (1 + x*x*x)*x;
}

int main(){

    double h = 0.01;
    int NUM_POINTS = 1000;
    
    std::vector<double> x_points {};
    std::vector<double> function_values {};

    for (int i = 0; i < NUM_POINTS; i++) {
        x_points.push_back(i*h);
        function_values.push_back(funtion(i*h));
    }

    std::vector<double> derivative = compmath::differentiate(function_values, h, 4);

    compmath::export_data_to_csv("function.csv", x_points, function_values);
    compmath::export_data_to_csv("derivative.csv", x_points, derivative);

    return 0;
}