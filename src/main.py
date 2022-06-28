from get_data import get_data
from sybil_check import check_val, get_unique_users
from pprint import pprint


def main():
    users = get_data()
    sybil_suspects = check_val(users)
    unique_users = get_unique_users(users)
    print(
        "Unique Users not sybiling is {}".format(
            len(unique_users) - len(sybil_suspects)
        )
    )


if __name__ == "__main__":
    main()
