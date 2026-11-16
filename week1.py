from dataclasses import dataclass

def average(nums: list[float]) -> float:
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts



@dataclass
class Student:
    name: str
    marks: list[float]
    
    def grade(self) -> str:
        avg = average(self.marks)
        if avg >= 70:
            return "Distinction"
        elif avg >= 60:
            return "Merit"
        elif avg >= 50:
            return "Pass"
        return "Fail"


if __name__ == "__main__":
    print(average([70, 85, 62]))
    print(count_words("AI is fun and AI is the future"))

    s = Student(name="Ganesh", marks=[72, 68, 81])
    print(s.name, s.grade())
    
    s = Student(name="Abhay", marks=[50, 59, 60])
    print(s.name, s.grade())