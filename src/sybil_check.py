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
