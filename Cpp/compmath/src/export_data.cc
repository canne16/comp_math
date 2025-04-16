#include "export_data.hh"
#include <iostream>

namespace compmath {


int create_directory(const std::string& dir) {

    if (!std::filesystem::exists(dir)) {
        // Create the directory
        if (std::filesystem::create_directory(dir)) {
            std::cout << "Directory created: " << dir << std::endl;
        } else {
            std::cerr << "Failed to create directory: " << dir << std::endl;
        }
    }

    return 0;

}

    
}