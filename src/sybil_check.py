def check_val(users):
    sybil_suspects = []
    gas_df = users[["cumulativeGasUsed", "gasPrice", "value", "from"]]
    for _, user in gas_df.iterrows():
        if (
            (int(user["cumulativeGasUsed"]) * int(user["gasPrice"]))
            >= int(user["value"])
            and (user["from"] not in sybil_suspects)
            and (int(user["value"]) != 0)
        ):
            sybil_suspects.append(user["from"])
    return sybil_suspects


def get_unique_users(users):
    unique_users = []
    from_df = users[["from"]]
    for _, user in from_df.iterrows():
        if user["from"] not in unique_users:
            unique_users.append(user["from"])
    return unique_users
