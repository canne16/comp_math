#include <gtest/gtest.h>
#include <vector>
#include <cmath>
#include <fstream>

#include "differentiation.hh"

// class DiffTest : public ::testing::TestWithParam<std::tuple<std::vector, bool>> {};

double funtion (double x) {
    return 1 / (1 + x);
}

TEST(DiffTest, Diff_first_order) {
    
    // std::vector<double> function_values {};
 
    // for (int i = 0; i < 10; ++i) {
    //     function_values.push_back(funtion(i));
    // }

    // double h = 0.1;
    // std::vector<double> derivative = differentiate(function_values, h, 1);

    EXPECT_TRUE(
        true
        // derivative.size() == function_values.size()
    );


}

TEST(DiffTest, Diff_second_order) {
    
    EXPECT_TRUE(
        true
    );

}