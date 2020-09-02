# PresidentialPolls
In the PresidentialTabular.py file, the first step
is to import the library get_polls and get_poll_data.
Then from prettyTable import the PrettyTable library.
List all the battleground states in an array. The
battleground states are "Wisconsin", "Florida", 
"Michigan", "Pennsylvania", "North Carolina",
"Arizona", "Texas", "Iowa", and "Georgia". Next, set
a variable x to PrettyTable(). Through a for loop that
traverses through the states of the battleground array,
set a variables to the result of the get_polls method
with candidate Biden, and set state to the particular 
state in the loop. Then traverse through the poll
in polls, where the data is equal to the result
of the poll data for the poll at the index of the url.
Then x's field_names is equal to the list at data[0]
with ["data"][0] keys. Set x's align to "l". Then,
traversing through the row in data[0]["data"], to
x, add the row values to x's rows. Finally, print x which prints results in Tabular Format.

<B>pip install realclearpolitics</B>
The program only works on Python 2.7
