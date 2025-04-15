#pragma once

#include <vector>
#include <stdexcept>
#include <cassert>

template <typename T>
std::vector<T> differentiate(
    const std::vector<T> &func, 
    const T &h, 
    int order = 2
){
    if (order != 1 && order != 2)
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
        
        result[0] = (-3*func[0] + 4*func[1] - func[2]) / (2*h);                 // left margin
        result[len-1] = (3*func[len-1] - 4*func[len-2] + func[len-3]) / (2*h);  // right margin
    }

    return result;
}
