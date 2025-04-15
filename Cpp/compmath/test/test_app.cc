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

    Gnuplot gp;
    std::vector<std::pair<double, double>> func_points;
    std::vector<std::pair<double, double>> der_points;
    
    std::vector<double> x_points {};
    std::vector<double> function_values {};

    for (int i = 0; i < NUM_POINTS; i++) {
        x_points.push_back(i*h);
        function_values.push_back(funtion(i*h));
        func_points.emplace_back(i*h, funtion(i*h)); 
    }

    std::vector<double> derivative = differentiate(function_values, h, 2);

    for (int i = 0; i < derivative.size(); i++) {
        der_points.emplace_back(i*h, derivative[i]); 
    }

    gp << "set title 'DerivTest'\n";
    gp << "set xzeroaxis\n";
    gp << "set yzeroaxis\n";
    gp << "plot '-' with lines title '1/(1+x)', '-' with lines title '-1/(1+x)^2'\n";
    gp.send1d(func_points);
    gp.send1d(der_points);

    export_data_to_csv("function.csv", x_points, function_values);
    export_data_to_csv("derivative.csv", x_points, derivative);

    return 0;
}