#pragma once

#include <vector>
#include <stdexcept>
#include <cassert>
#include <cmath>

namespace compmath {


/**
 * @brief Numerically compute the first derivative of a sampled function using finite differences.
 * 
 * @tparam T Numeric type (e.g., double, float)
 * @param func Vector of sampled function values
 * @param result Vector to store the computed derivative (must be same size as func)
 * @param h Step size between samples
 * @param order Order of the finite difference scheme: 1 (forward), 2 (central), or 4 (fourth-order central). Default: 2
 * @return Reference to result vector containing the derivative
 * @throws std::invalid_argument if order is not 1, 2, or 4, or if func and result sizes do not match
 */
template <typename T>
std::vector<T>& differentiate(
    const std::vector<T> &func,
    std::vector<T>& result,
    const T &h, 
    int order = 2
){
    if (order != 1 && order != 2 && order != 4)
        throw std::invalid_argument("Invalid order of differentiation");
    
    if (func.size() != result.size())
        throw std::invalid_argument("Derivative must be the same shape as function");
        
    size_t len = func.size();
    
    if (order == 1) {
        
        for (size_t i = 0; i < len - 1; ++i)
            result[i] = (func[i + 1] - func[i]) / h;
        
        result[len-1] = (func[len-1] - func[len-2]) / h;                        // left margin

    } else if (order == 2) {
        
        for (size_t i = 1; i < len - 1; ++i)
            result[i] = (func[i + 1] - func[i-1]) / (2*h);
        
        result[0]     = (-3*func[0]     + 4*func[1]     - func[2]    ) / (2*h);                 // left margin
        result[len-1] = ( 3*func[len-1] - 4*func[len-2] + func[len-3]) / (2*h);  // right margin
    
    } else if (order == 4) {
        
        for (size_t i = 2; i < len - 2; ++i)
            result[i] = (func[i-2] - 8*func[i-1] + 8*func[i+1] - func[i+2]) / (12*h);
        
        result[0] = (-25*func[0] + 48*func[1] - 36*func[2] + 16*func[3] - 3*func[4]) / (12*h);                 // left margin
        result[1] = ( -3*func[0] - 10*func[1] + 18*func[2] -  6*func[3] +   func[4]) / (12*h);                 // left margin
        
        result[len-1] = (25*func[len-1] - 48*func[len-2] + 36*func[len-3] - 16*func[len-4] + 3*func[len-5]) / (12*h);  // right margin
        result[len-2] = ( 3*func[len-1] + 10*func[len-2] - 18*func[len-3] +  6*func[len-4] -   func[len-5]) / (12*h);  // right margin
    
    }

    return result;
}


/**
 * @brief Numerically compute the second derivative of a sampled function using finite differences (second order).
 * 
 * @tparam T Numeric type (e.g., double, float)
 * @param func Vector of sampled function values
 * @param result Vector to store the computed second derivative (must be same size as func)
 * @param h Step size between samples
 * @param order Order of the finite difference scheme (only 2 is implemented). Default: 2
 * @return Reference to result vector containing the second derivative
 * @throws std::invalid_argument if order != 2 or if func and result sizes do not match
 */
template <typename T>
std::vector<T>& differentiate_twice(
    const std::vector<T> &func, 
    std::vector<T>& result,
    const T &h, 
    int order = 2
){
    if (order != 2)
        throw std::invalid_argument("Not implemented for order != 2");
        
    if (func.size() != result.size())
        throw std::invalid_argument("Derivative must be the same shape as function");
        
    size_t len = func.size();
    
    for (size_t i = 1; i < len - 1; ++i)
        result[i] = (func[i+1] - 2*func[i] + func[i-1]) / pow(h, 2);

    result[0]     = (2*func[0]     - 5*func[1]     + 4*func[2]     - func[3]    ) / pow(h, 2);  // left margin
    result[len-1] = (2*func[len-1] - 5*func[len-2] + 4*func[len-3] - func[len-4]) / pow(h, 2);  // right margin

    return result;
}

}