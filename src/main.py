from get_data import get_data, get_users_nieghbors


def main():
    users = get_data()
    print(users.head())


if __name__ == "__main__":
    main()
