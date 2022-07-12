import matplotlib.pyplot as plt


def pie_plot(unique_users, sybil_suspects):
    unique_authentic_users = unique_users - sybil_suspects
    labels = "Sybil Suspects", "Authentic Users"
    sizes = [sybil_suspects, unique_authentic_users]
    explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes,
        explode=explode,
        labels=labels,
        autopct="%1.1f%%",
        shadow=False,
        startangle=90,
        colors=["#369EFF", "#10B3A3"],
    )
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
