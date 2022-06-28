from get_data import get_data
from sybil_check import check_val
from pprint import pprint


def main():
    users = get_data()
    print(len(users))
    sybil_suspects = check_val(users)
    pprint(len(sybil_suspects))


if __name__ == "__main__":
    main()
