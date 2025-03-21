import requests

API_URL = "http://demo2854210.mockable.io/studentsmarks.data"

def get_student_scores(student_id):
    """Fetch student scores from the API."""
    response = requests.get(API_URL) 
    if response.status_code == 200:
        students_data = response.json()  
        return students_data.get(student_id)  
    else:
        print("Failed to fetch data")
        return None

def calculate_percentage(scores):
    """Calculate the percentage based on subject scores."""
    if not scores:
        return 0
    total_marks = sum(scores.values())
    max_marks = len(scores) * 100  
    return (total_marks / max_marks) * 100

def main():
    student_id = input("Enter student ID: ")
    scores = get_student_scores(student_id)
    
    if scores:
        percentage = calculate_percentage(scores)
        print(f"Student ID: {student_id}")
        print(f"Scores: {scores}")
        print(f"Percentage: {percentage:.2f}%")
    else:
        print("No data available for the given student ID.")

if __name__ == "__main__":
    main()