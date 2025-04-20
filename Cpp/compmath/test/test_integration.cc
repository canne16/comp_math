#include <gtest/gtest.h>

#include <iostream>
#include <cmath>

#include "integration.hh"
#include "export_data.hh"


double function(double x) {
    return x / (1 + pow(x, 3));
}


TEST(IntegrTest, Int_Check_Order) {
    
    std::vector<double> errors_trapez     {};
    std::vector<double> errors_rect     {};
    std::vector<double> errors_simpson     {};

    size_t MAX_N_POINTS = pow(2,20);
    double x_start = 1;
    double x_end   = 10;
    double true_integral = 0.735673833988999;

    std::vector<double> results_trapez {};
    std::vector<double> results_rect {};
    std::vector<double> results_simpson {};
    
    std::vector<double> h_vals {};

    for (size_t i = 2; i < MAX_N_POINTS; i*=2){
        
        h_vals.push_back(i);
        errors_trapez.push_back(
            std::abs(compmath::integrate_trapez(function, x_start, x_end, i)-true_integral)
        );
        errors_rect.push_back(
            std::abs(compmath::integrate_rect(function, x_start, x_end, i, "left")-true_integral)
        );
        errors_simpson.push_back(
            std::abs(compmath::integrate_simpson(function, x_start, x_end, i)-true_integral)
        );

    }
        
    compmath::export_data_to_csv("errors_trapez.csv", h_vals, errors_trapez);
    compmath::export_data_to_csv("errors_rect.csv", h_vals, errors_rect);
    compmath::export_data_to_csv("errors_simpson.csv", h_vals, errors_simpson);
    
}
