print("What's your idea ?: ")
#user_idea = input()

ideas_list =[]


def save_idea_to_file(ideas_list):
    file = open('ideabank.txt','w')
    for i, item in enumerate(ideas_list):
        file.write(f"{i}.{item}\n")
    file.close()

    

save_idea_to_file(("pomysł", "asdddf"))