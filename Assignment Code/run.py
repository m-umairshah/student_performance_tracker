class Student:

    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add_score(self, subject, obtained_marks, total_marks):

        self.scores[subject] = {"obtained": obtained_marks, "total": total_marks}

    def calculate_average(self):

        if not self.scores:
            return 0
        total_obtained = sum(data["obtained"] for data in self.scores.values())
        total_marks = sum(data["total"] for data in self.scores.values())
        return (total_obtained / total_marks) * 100

    def is_passing(self, passing_percentage=40):

        return all((data["obtained"] / data["total"]) * 100 >= passing_percentage for data in self.scores.values())


class PerformanceTracker:

    def __init__(self):
        self.students = {}  # Dictionary to hold Student objects with names as keys
        self.subjects = set()  # Set to dynamically store all subjects

    def add_student(self, name):

        if name not in self.students:
            self.students[name] = Student(name)
        return self.students[name]

    def add_subject(self, subject):

        self.subjects.add(subject)

    def calculate_class_average(self):

        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):

        if not self.students:
            print("No student data available.")
            return
        print("\n--- Individual Student Performance ---")
        for name, student in self.students.items():
            average = student.calculate_average()
            status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {name}, Average Percentage: {average:.2f}%, Status: {status}")
            print("Subjects and Scores:")
            for subject, data in student.scores.items():
                print(f"  {subject}: {data['obtained']} / {data['total']}")
            print()


def get_subject_and_scores():

    scores = {}
    while True:
        subject = input("Enter subject name (or 'done' to stop): ").strip()
        if subject.lower() == 'done':
            break
        if not subject:
            print("Subject name cannot be empty. Try again.")
            continue

        while True:
            try:
                total_marks = int(input(f"Enter total marks for {subject}: "))
                if total_marks > 0:
                    break
                else:
                    print("Total marks must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                obtained_marks = int(input(f"Enter obtained marks for {subject}: "))
                if 0 <= obtained_marks <= total_marks:
                    scores[subject] = {"obtained": obtained_marks, "total": total_marks}
                    break
                else:
                    print(f"Obtained marks must be between 0 and {total_marks}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return scores


def main():

    print("Welcome to the Enhanced Student Performance Tracker!")
    tracker = PerformanceTracker()

    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if not name:
            print("Student name cannot be empty. Try again.")
            continue

        print(f"Enter subjects, total marks, and obtained marks for {name}:")
        scores = get_subject_and_scores()
        if not scores:
            print("No subjects entered. Skipping this student.")
            continue

        student = tracker.add_student(name)
        for subject, data in scores.items():
            tracker.add_subject(subject)
            student.add_score(subject, data["obtained"], data["total"])

    tracker.display_student_performance()
    class_average = tracker.calculate_class_average()
    print(f"\nClass Average Percentage: {class_average:.2f}%")

if __name__ == "__main__":
    main()
