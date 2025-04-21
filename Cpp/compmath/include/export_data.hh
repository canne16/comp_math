#pragma once

#include <vector>
#include <string>
#include <fstream>
#include <stdexcept>
#include <filesystem>

#include "Config.hh"

namespace compmath {

int create_directory(const std::string& dir);


/**
 * @brief Exports data to a CSV file.
 * 
 * This function writes the provided x-coordinates and corresponding function values
 * to a CSV file. The output file will include a header row and the data in two columns:
 * "x" and "value".
 * 
 * @tparam T The type of the elements in the vectors. Must support streaming to an output stream.
 * @param filename The name of the CSV file to create (relative to EXPORT_PATH).
 * @param x A vector containing the x-coordinates.
 * @param func A vector containing the corresponding function values.
 * @return int Returns 0 on success, or -1 if the file could not be opened.
 * @throws std::invalid_argument If the sizes of `x` and `func` do not match.
 * @throws std::runtime_error If the directory specified by EXPORT_PATH cannot be created.
 * 
 * @note The directory specified by EXPORT_PATH must exist or be creatable.
 *       Ensure that the type `T` supports the `<<` operator for output streams.
 */
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