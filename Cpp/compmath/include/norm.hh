#include <cmath>
#include <vector>
#include <stdexcept>

namespace compmath {


    
    
    double norm_inf (std::vector<double> &v1, std::vector<double> &v2) {
        if (v1.size() != v2.size())
            throw std::invalid_argument("Vectors must be of the same size");
        
        double norm = 0.0;

        for (size_t i = 0; i < v1.size(); ++i)
            norm = std::abs(v1[i] - v2[i]) <= norm ? norm : std::abs(v1[i] - v2[i]);
        
    return norm;
}








}