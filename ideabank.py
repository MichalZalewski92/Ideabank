
def save_idea_to_file(ideas_list):
    file = open('ideabank.txt','w')
    for i, item in enumerate(ideas_list):
        file.write(f"{i}.{item}\n")
    file.close()

def get_and_save_user_ideas():
    user_ideas = []
    while True:
        user_idea = input("Give your idea: ")
        if user_idea == "Quit":
            break
        user_ideas.append(user_idea)
    save_idea_to_file(user_ideas)
        

get_and_save_user_ideas()