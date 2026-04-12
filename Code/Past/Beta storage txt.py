import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
storage_file = os.path.join(BASE_DIR, "TextFolders", "Storage.txt")

def get_storage_data():
    with open(storage_file, "r") as f:
        lines = f.readlines()

    scores = [int(line[9:12]) for line in lines[:5]]

    scores1 = scores[0] if len(scores) > 0 else None
    scores2 = scores[1] if len(scores) > 1 else None
    scores3 = scores[2] if len(scores) > 2 else None
    scores4 = scores[3] if len(scores) > 3 else None
    scores5 = scores[4] if len(scores) > 4 else None


    passws = [str(line[3:9]) for line in lines[:5]]

    passw1 = passws[0] if len(passws) > 0 else None
    passw2 = passws[1] if len(passws) > 1 else None
    passw3 = passws[2] if len(passws) > 2 else None
    passw4 = passws[3] if len(passws) > 3 else None
    passw5 = passws[4] if len(passws) > 4 else None


    names = [str(line[0:3]) for line in lines[:5]]

    name1 = names[0] if len(names) > 0 else None
    name2 = names[1] if len(names) > 1 else None
    name3 = names[2] if len(names) > 2 else None
    name4 = names[3] if len(names) > 3 else None
    name5 = names[4] if len(names) > 4 else None

    """
    print("=============================================")
    print(scores1, scores2, scores3, scores4, scores5)
    print(name1, name2, name3, name4, name5)
    print(passw1, passw2, passw3, passw4, passw5)
    print("=============================================")
    """

    names_and_scores_sorted = sorted(list(zip(names, scores)), key=lambda x: x[1], reverse=True)
    names_and_scores_sorted_fixed = [f"{name}{score}" for name, score in names_and_scores_sorted]
    names_and_scores_sorted_fixed = ("[" + ", ".join(f"{name}{score}" for name, score in names_and_scores_sorted) + "]")

    print(names_and_scores_sorted_fixed)

    scores_sorted = sorted(scores, reverse=True)
    print(scores_sorted)
    lowest_score = scores_sorted[4]
    fourth_score = scores_sorted[3]
    third_score = scores_sorted[2]
    second_score = scores_sorted[1]
    highest_score = scores_sorted[0]
    lowest_score_index = scores.index(lowest_score)
    print(lowest_score)
    print(lowest_score_index)

    names_current = "bil"
    passw_current = "ung65#"
    scores_current = "5"

    scores_current = str(scores_current.zfill(3))
    account_current = f"{names_current}{passw_current}{scores_current}"
    print(account_current)

    if int(scores_current) > lowest_score:
        lines[lowest_score_index] = account_current + "\n"
        with open(storage_file, "w") as f:
            f.writelines(lines)

get_storage_data()