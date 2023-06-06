

class Set:
    def __init__(self):
        self.items = []
    
    def add(self, new_element):
        if new_element not in self.items:
            self.items.append(new_element)
    
    def remove(self, element):
        if element in self.items:
            self.items.remove(element)
    
    def contains(self, element):
        return element in self.items
    
    def size(self):
        return len(self.items)
    
    def iterator(self):
        return iter(self.items)
    
    def intersection(self, other_set):
        result = Set()
        for item in self.items:
            if item in other_set.items:
                result.add(item)
        return result
    
    def union(self, other_set):
        result = Set()
        for item in self.items:
            result.add(item)
        for item in other_set.items:
            result.add(item)
        return result
    
    def difference(self, other_set):
        result = Set()
        for item in self.items:
            if item not in other_set.items:
                result.add(item)
        return result
    
    def is_subset(self, other_set):
        for item in self.items:
            if item not in other_set.items:
                return False
        return True


def main():
    s1 = Set()

    # Ask the user to input the elements of the first set
    input_str = input("Enter the elements of the first set, separated by commas: ")
    elements = input_str.split(",")
    for element in elements:
        s1.add(int(element))

    while True:
        print("\n---- Set Operations Menu ----")
        print("1. Add element to the set")
        print("2. Remove element from the set")
        print("3. Check if an element is in the set")
        print("4. Print the size of the set")
        print("5. Compute the intersection with another set")
        print("6. Compute the union with another set")
        print("7. Compute the difference with another set")
        print("8. Check if the set is a subset of another set")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Add element to the set
            element = int(input("Enter the element to add: "))
            s1.add(element)
            print("Element added to the set")

        elif choice == 2:
            # Remove element from the set
            element = int(input("Enter the element to remove: "))
            s1.remove(element)
            print("Element removed from the set")

        elif choice == 3:
            # Check if an element is in the set
            element = int(input("Enter the element to check: "))
            if s1.contains(element):
                print("Element is in the set")
            else:
                print("Element is not in the set")

        elif choice == 4:
            # Print the size of the set
            print("Size of set:", s1.size())

        elif choice == 5:
            # Compute the intersection with another set
            s2 = Set()
            input_str = input("Enter the elements of the second set, separated by commas: ")
            elements = input_str.split(",")
            for element in elements:
                s2.add(int(element))
            s3 = s1.intersection(s2)
            print("Intersection of the two sets:", [item for item in s3.iterator()])

        elif choice == 6:
            # Compute the union with another set
            s2 = Set()
            input_str = input("Enter the elements of the second set, separated by commas: ")
            elements = input_str.split(",")
            for element in elements:
                s2.add(int(element))
            s4 = s1.union(s2)
            print("Union of the two sets:", [item for item in s4.iterator()])

        elif choice == 7:
            # Compute the difference with another set
            s2 = Set()
            input_str = input("Enter the elements of the second set, separated by commas: ")
            elements = input_str.split(",")
            for element in elements:
                s2.add(int(element))
            s5 = s1.difference(s2)
            print("Difference of the two sets:", [item for item in s5.iterator()])

        elif choice == 8:
            # Check if the set is a subset of another set
            s2 = Set()
            input_str = input("Enter the elements of the other set, separated by commas: ")
            elements = input_str.split(",")
            for element in elements:
                s2.add(int(element))
            if s1.is_subset(s2):
                print("The set is a subset of the other set")
            else:
                print("The set is not a subset of the other set")


        elif choice == 9:
            print("Exiting program...")
            quit()
main()
