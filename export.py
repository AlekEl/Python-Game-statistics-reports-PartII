
# Export functions


def open_file(file_name):
    """Opens the file and returns content in form of a list"""
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
            content = [game for game in content if game]
            content = [game.split("\t") for game in content]
            return content
    except FileNotFoundError as err:
        raise err


def get_most_played(file_name):
    """Return and print best selling game from the file"""
    content = open_file(file_name)
    game_name = content[0][0]
    copies_sold = int(content[0][1])
    best_selling_game = [game_name, copies_sold]
    for game in range(1, len(content)):
        game_name = content[game][0]
        copies_sold = int(content[game][2])
        if best_selling_game[1] < copies_sold:
            best_selling_game[0] = game_name
            best_selling_game[1] = copies_sold
    return "Best selling game from the file is {0}.\n".format(best_selling_game[0])


def sum_sold(file_name):
    """Return and print  sum of sold copies of all the games from the file"""
    content = open_file(file_name)
    copies_sold_index = 1
    sum_of_copies_sold = 0
    for game in content:
        sum_of_copies_sold += float(game[copies_sold_index])
    return sum_of_copies_sold, "Sum of copies sold: {0}\n".format(sum_of_copies_sold)


def get_selling_avg(file_name):
    """Return and print  average number of sold copies from all the games from file"""
    content = open_file(file_name)
    avg = float(sum_sold(file_name)[0])/len(content)
    return "Average number of copies sold: {0}\n".format(avg)


def count_longest_title(file_name):
    """Return and print  number of characters in longest game title from the file"""
    content = open_file(file_name)
    title_index = 0
    longest_title = len(content[0][title_index])
    for game in range(1, len(content)):
        if longest_title < len(content[game][title_index]):
            longest_title = len(content[game][title_index])
    return "Longest title rom the file has {0} characters\n".format(longest_title)


def get_date_avg(file_name):
    """Return and print  average release date of all games from the file"""
    content = open_file(file_name)
    year_index = 2
    sum_of_release_dates = 0
    for game in content:
        sum_of_release_dates += float(game[year_index])
    avg = int(sum_of_release_dates / len(content)) + (sum_of_release_dates % len(content) > 0)
    return "Average release date is {0}.\n".format(avg)


def get_game(file_name, title):
    """Return and print  properties of a given game"""
    content = open_file(file_name)
    game_properties = []
    title_index = 0
    copies_sold_index = 1
    release_date_index = 2
    for games in range(len(content)):
        for game in range(len(content[games])):
            if title.lower() == content[games][title_index].lower():
                if game == copies_sold_index:
                    game_properties.append(float(content[games][copies_sold_index]))
                elif game == release_date_index:
                    game_properties.append(int(content[games][release_date_index]))
                else:
                    content[games][game] = content[games][game].replace("\n", "")
                    game_properties.append(content[games][game])
    return "Game properties of a given game: {0}\n".format(game_properties)


def count_grouped_by_genre(file_name):
    """Return and print dictionary with games grouped by genre"""
    content = open_file(file_name)
    genre_index = 3
    genres = {}
    for game in content:
        if game[genre_index] in genres:
            genres[game[genre_index]] += 1
        else:
            genres[game[genre_index]] = 1
    return "Games grouped by genre: {0}".format(genres)


def get_date_ordered(file_name):
    """Return and print list with games sorted by realase year"""
    content = open_file(file_name)
    title_index = 0
    tuple_title_index = 1
    year_index = 2
    games_dict = {}
    arr = []
    for game in content:
        if int(game[year_index]) in games_dict:
            games_dict[int(game[year_index])].append(game[title_index])
        else:
            games_dict[int(game[year_index])] = [game[title_index]]
    sorted_list = [(k, games_dict[k]) for k in sorted(games_dict)]
    sorted_list.reverse()
    counter = 0
    for game in sorted_list:
        arr.append(game[tuple_title_index])
        arr[counter].sort()
        counter += 1
    arr = [item for sublist in arr for item in sublist]
    return "Games sorted by release year: {0}".format(arr)


def export_answers(file_name):
    title = input("Title of the game: ")
    functions = [get_most_played(file_name),
                 sum_sold(file_name)[1],
                 get_selling_avg(file_name),
                 count_longest_title(file_name),
                 get_date_avg(file_name),
                 get_game(file_name, title),
                 count_grouped_by_genre(file_name),
                 get_date_ordered(file_name)]
    answers = ""
    for answer in functions:
        answers += answer
    with open("answers_part2.txt", "w") as f:
        f.write(answers)


export_answers("game_stat.txt")