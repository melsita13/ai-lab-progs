subjects = ["maths", "phy", "che", "bio"]
days = ["Monday", "Tuesday"]
conflicts = [
    ("maths", "phy"),  # Maths and Physics cannot be on the same day
    ("che", "bio")     # Chemistry and Biology cannot be on the same day
]
def schedule_subjects(assignment):
    # Check if all subjects are assigned
    if len(assignment) == len(subjects):
        return assignment

    # Select the next unassigned subject
    for subject in subjects:
        if subject not in assignment:
            break
    
    # Try assigning each day
    for day in days:
        if is_valid_assignment(subject, day, assignment):
            assignment[subject] = day
            result = schedule_subjects(assignment)
            if result:
                return result
            assignment.pop(subject)  # backtrack if not successful
    
    return None

def is_valid_assignment(subject, day, assignment):
    # Check for conflicts with already assigned subjects
    for (subj1, subj2) in conflicts:
        if subject in (subj1, subj2):
            other_subject = subj1 if subject == subj2 else subj2
            if assignment.get(other_subject) == day:
                return False
    return True

# Run the scheduling
solution = schedule_subjects({})
print(solution)
 