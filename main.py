from js import document

class Phrase:
    def __init__(self, name, section, desiredJob):
        self.name = name
        self.section = section
        self.desiredJob = desiredJob

    def introduce(self):
        return f"Hello! I am {self.name} from {self.section}. I want to be a {self.desiredJob} when I grow up."


people = [
    Phrase("Inigo", "Sapphire", "Lawyer"),
    Phrase("Curt", "Sapphire", "Basketball Coach"),
    Phrase("Yanna", "Sapphire", "Engineer"),
    Phrase("Luis", "Sapphire", "IT"),
    Phrase("Zyan", "Sapphire", "President")
]

def show_list():
    output = ""
    for person in people:
        output += person.introduce() + "<br>"
    
    document.getElementById("output").innerHTML = output

def add():
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    desiredJob = document.getElementById("desiredJob").value

    new_person = Phrase(name, section, desiredJob)
    people.append(new_person)

    show_list()