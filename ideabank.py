import sys

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
        

#get_and_save_user_ideas()

def list_data_from_file():
    file = open('ideabank.txt','r')
    ideas = file.readlines()
    for idea in ideas:
        print(idea)

def delete_idea(index):
    file = open('ideabank.txt','r')
    ideas = file.readlines()
    try:
        del ideas[index]
        print(ideas)
        save_idea_to_file(ideas)
    except:
        print("There is no that index in ideas")



# list_data_from_file()

def main():
    if len(sys.argv) == 1:
        get_and_save_user_ideas()
    elif sys.argv[1] == "--list":
        list_data_from_file()
    elif sys.argv[1] == "--delete":
        try:
            line_to_delete = sys.argv[2]
            delete_idea(int(line_to_delete))
        except IndexError:
            print("Podaj idee do usunięcia")

        

        #delete_data_from_file()
    print(sys.argv)

main()