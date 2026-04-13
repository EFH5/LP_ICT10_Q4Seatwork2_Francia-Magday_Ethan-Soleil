from js import document

# Class definition
class Classmate:
    def __init__(self, name, section, job):
        self.name = name
        self.section = section
        self.job = job

    def introduce(self):
        return f"Name: {self.name}<br>Section: {self.section}<br>Desired Job: {self.job}<br><br>"


# Initial list
classmates = [
    Classmate("Inigo", "Sapphire", "Lawyer"),
    Classmate("Curt", "Sapphire", "Basketball Coach"),
    Classmate("Yanna", "Sapphire", "Engineer"),
    Classmate("Luis", "Sapphire", "IT"),
    Classmate("Zyan", "Sapphire", "President")
]


# Show list
def show_list(event=None):
    output = ""
    for classmate in classmates:
        output += classmate.introduce()

    document.getElementById("classmate-list").innerHTML = output


# Add classmate
def add_classmate(event=None):
    username = document.getElementById("name").value.strip()
    section = document.getElementById("section").value.strip()
    desiredJob = document.getElementById("desiredJob").value.strip()

    if not username or not section or not desiredJob:
        document.getElementById("signed").innerText = "Please fill in all fields!"
        return

    if any(c.name == username for c in classmates):
        document.getElementById("signed").innerText = "You're already in the list!"
        return

    new_classmate = Classmate(username, section, desiredJob)
    classmates.append(new_classmate)

    document.getElementById("signed").innerText = f"{username} added successfully!"

    # Clear inputs
    document.getElementById("name").value = ""
    document.getElementById("section").value = ""
    document.getElementById("desiredJob").value = ""

