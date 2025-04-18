#pragma once

#include <vector>
#include <string>
#include <fstream>
#include <stdexcept>
#include <filesystem>

#include "Config.hh"

namespace compmath {

int create_directory(const std::string& dir);


template<typename T>
int export_data_to_csv(const std::string& filename, 
                       const std::vector<T>& x, 
                       const std::vector<T>& func) {
    
    if (x.size() != func.size()) {
        throw std::invalid_argument("x_coords and func_values must have the same size");
    }

    if (create_directory(EXPORT_PATH) != 0) {
        throw std::runtime_error("Failed to create directory");
    }

    std::ofstream file(EXPORT_PATH + filename);
    if (!file.is_open()) {
        return -1; // Error opening file
    }

    // Write CSV header
    file << "x, value\n";

    // Write data
    for (size_t i = 0; i < x.size(); ++i) {
        file << x[i] << "," << func[i] << "\n";
    }

    file.close();
    return 0;
}


}