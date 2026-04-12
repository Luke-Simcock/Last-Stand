import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
storage_file = os.path.join(BASE_DIR, "TextFolders", "Storage.txt")

def get_storage_data():
    with open(storage_file, "r") as f:
        lines = f.readlines()

    name1, password1, score1 = lines[0].strip().split("|")
    name2, password2, score2 = lines[1].strip().split("|")
    name3, password3, score3 = lines[2].strip().split("|")
    name4, password4, score4 = lines[3].strip().split("|")
    name5, password5, score5 = lines[4].strip().split("|")

    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    score4 = int(score4)
    score5 = int(score5)

    print(f"Name: {name1}, Password: {password1}, Score: {score1}")
    print(f"Name: {name2}, Password: {password2}, Score: {score2}")
    print(f"Name: {name3}, Password: {password3}, Score: {score3}")
    print(f"Name: {name4}, Password: {password4}, Score: {score4}")
    print(f"Name: {name5}, Password: {password5}, Score: {score5}")

    scores = [score1, score2, score3, score4, score5]
    names = [name1, name2, name3, name4, name5]
    passwords = [password1, password2, password3, password4, password5]

    scores_sorted = sorted(scores, reverse=True)
    print (scores_sorted)
    lowest_score = scores_sorted[4]


    names_current = "bil"
    passw_current = "ung65#"
    scores_current = "5"

    account_current = f"{names_current}{passw_current}{scores_current}"
    print(account_current)

    

get_storage_data()