class Repository:
    def __init__(self):
        self.packages = {}
    
    def add_packages(self, package):
        # package is on object
        self.packages[package.name] = package
    
    def total_size_of_packages(self):
        result = 0
        for package in self.packages.values():
            result += package.sizeGB
        return result
    
    def delete_package(self, package):
        del self.packages[package.name]
        