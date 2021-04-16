from conans import ConanFile


class UndistortConan(ConanFile):
    generators = ["cmake", "virtualrunenv"]
    requires = (
        "kinect-azure-sensor-sdk/1.4.1@camposs/stable",
    )

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def imports(self):
        self.copy(src="bin", pattern="*.dll", dst="./bin")     # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="", pattern="**.dll", dst="./bin", keep_path=False)     # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="lib", pattern="*.dylib*", dst="./lib")  # Copies all dylib files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.so*", dst="./lib")     # Copies all so files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.lib", dst="./lib")     # Copies all lib files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.a", dst="./lib")       # Copies all static libraries from packages lib folder to my "lib" folder
        self.copy(src="bin", pattern="*", dst="./bin")         # Copies all applications


