from rcp import get_polls, get_poll_data
from prettytable import PrettyTable


battleground_states = [
    "Wisconsin",
    "Florida",
    "Michigan",
    "Pennsylvania",
    "North Carolina",
    "Arizona",
    "Texas",
    "Iowa",
    "Georgia",
]
x = PrettyTable()

for state in battleground_states:
    polls = get_polls(candidate="Biden",state=state)
    for poll in polls:
            data = get_poll_data(poll['url'])
            x.field_names = list(data[0]["data"][0].keys())
            x.align = "l"

            for row in data[0]["data"]:
                x.add_row(row.values())

            print(x)