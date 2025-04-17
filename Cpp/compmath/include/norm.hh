#include <cmath>
#include <vector>
#include <stdexcept>

namespace compmath {
    
template <typename T>
T norm_inf (std::vector<T> &v1, std::vector<T> &v2) {
    if (v1.size() != v2.size())
        throw std::invalid_argument("Vectors must be of the same size");
    
    T norm = 0.0;

    for (size_t i = 0; i < v1.size(); ++i)
        norm = std::abs(v1[i] - v2[i]) <= norm ? norm : std::abs(v1[i] - v2[i]);
    
    return norm;
}

// TODO: check if this is the correct implementation

template <typename T>
T norm_1 (std::vector<T> &v1, std::vector<T> &v2) {
    if (v1.size() != v2.size())
        throw std::invalid_argument("Vectors must be of the same size");
    
    T norm {};

    for (size_t i = 0; i < v1.size(); ++i)
        norm += std::abs(v1[i] - v2[i]);
    
    return norm;
}




}