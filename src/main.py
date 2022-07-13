from get_data import get_data
from sybil_check import check_val, get_unique_users
from graph_users import pie_plot
from pprint import pprint


def main():
    # Get the user Data
    users = get_data()
    # Get the Sybil Suspects
    sybil_suspects = check_val(users)
    # Get the unique users
    unique_users = get_unique_users(users)
    print("Total Unique users is {}".format(len(unique_users)))
    print(
        "Unique Users not sybiling is {}".format(
            len(unique_users) - len(sybil_suspects)
        )
    )
    # Graph the ration of unique users and sybil suspects
    pie_plot(len(unique_users), len(sybil_suspects))


if __name__ == "__main__":
    main()
