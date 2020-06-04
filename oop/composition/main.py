import repository
import package


repository = repository.Repository()

package_a = package.Packages("a", 10)
package_b = package.Packages("b", 11)
package_c = package.Packages("c", 12)


# Adding packages to repository 

repository.add_packages(package_a)
repository.add_packages(package_b)
repository.add_packages(package_c)


print(repository.total_size_of_packages())

# delete package_a
repository.delete_package(package_a)

print(repository.total_size_of_packages())


package_d = package.Packages("d", 200)

repository.add_packages(package_d)

print(repository.total_size_of_packages())