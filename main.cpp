#include <iostream>
#include <string>

int main() {
    // Replace with your actual server URL
    const std::string SERVER_URL = "http://your-computer-ip:5466/checkin";

    std::string command = "curl qrenco.de/" + SERVER_URL;
    system(command.c_str());

    std::cout << "\nQR Code generated for URL: " << SERVER_URL << std::endl;
    std::cout << "Display this QR code for employees to scan." << std::endl;

    return 0;
}