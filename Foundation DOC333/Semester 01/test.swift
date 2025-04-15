import Foundation

// A simple class representing a person
class Person {
    var firstName: String
    var lastName: String
    var age: Int
    
    init(firstName: String, lastName: String, age: Int) {
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    }
    
    func fullName() -> String {
        return "\(firstName) \(lastName)"
    }
    
    func celebrateBirthday() {
        age += 1
        print("Happy \(age)th birthday, \(firstName)!")
    }
}

// A struct representing a point in 2D space
struct Point {
    var x: Double
    var y: Double
    
    func distance(to point: Point) -> Double {
        let dx = x - point.x
        let dy = y - point.y
        return sqrt(dx * dx + dy * dy)
    }
}

// A function to demonstrate usage of the Person class and Point struct
func main() {
    let person = Person(firstName: "John", lastName: "Doe", age: 30)
    print("Person's full name: \(person.fullName())")
    person.celebrateBirthday()
    
    let point1 = Point(x: 0.0, y: 0.0)
    let point2 = Point(x: 3.0, y: 4.0)
    print("Distance between points: \(point1.distance(to: point2))")
    
    // Additional functionality to reach around 100 lines
    let people = [
        Person(firstName: "Alice", lastName: "Smith", age: 25),
        Person(firstName: "Bob", lastName: "Johnson", age: 40),
        Person(firstName: "Charlie", lastName: "Brown", age: 35)
    ]
    
    for person in people {
        print("\(person.fullName()) is \(person.age) years old.")
    }
    
    let points = [
        Point(x: 1.0, y: 1.0),
        Point(x: 2.0, y: 2.0),
        Point(x: 3.0, y: 3.0)
    ]
    
    for i in 0..<points.count {
        for j in i+1..<points.count {
            print("Distance between point \(i+1) and point \(j+1): \(points[i].distance(to: points[j]))")
        }
    }
    
    // More functionality to reach around 100 lines
    let morePeople = [
        Person(firstName: "David", lastName: "Wilson", age: 28),
        Person(firstName: "Eva", lastName: "Taylor", age: 22),
        Person(firstName: "Frank", lastName: "Anderson", age: 33)
    ]
    
    for person in morePeople {
        print("\(person.fullName()) is \(person.age) years old.")
        person.celebrateBirthday()
    }
    
    let morePoints = [
        Point(x: 4.0, y: 4.0),
        Point(x: 5.0, y: 5.0),
        Point(x: 6.0, y: 6.0)
    ]
    
    for i in 0..<morePoints.count {
        for j in i+1..<morePoints.count {
            print("Distance between point \(i+1) and point \(j+1): \(morePoints[i].distance(to: morePoints[j]))")
        }
    }
}

main()