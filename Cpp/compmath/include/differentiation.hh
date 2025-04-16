#pragma once

#include <vector>
#include <stdexcept>
#include <cassert>
#include <cmath>

namespace compmath {

template <typename T>
std::vector<T> differentiate(
    const std::vector<T> &func, 
    const T &h, 
    int order = 2
){
    if (order != 1 && order != 2 && order != 4)
        throw std::invalid_argument("Invalid order of differentiation");
    
    std::vector<T> result = std::vector<T>(func.size());
    
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


template <typename T>
std::vector<T> twice_differenciate(
    const std::vector<T> &func, 
    const T &h, 
    int order = 2
){
    if (order != 2)
        throw std::invalid_argument("Not implemented for order != 2");
    
    std::vector<T> result = std::vector<T>(func.size());
    
    size_t len = func.size();
    
    for (size_t i = 1; i < len - 1; ++i)
        result[i] = (func[i+1] - 2*func[i] + func[i-1]) / pow(h, 2);

        // TODO: check coefficents

    result[0]     = ( 2*func[0]     - 5*func[1]     + 4*func[2]     - func[3]    ) / pow(h, 2);                 // left margin
    result[len-1] = (-2*func[len-1] + 5*func[len-2] - 4*func[len-3] + func[len-4]) / pow(h, 2);  // right margin

    return result;
}



















}