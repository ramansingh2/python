
from tabulate import _table_formats, tabulate


format_list = list(_table_formats.keys())
# current format list in tabulate version 0.8.3:
# ['simple', 'plain', 'grid', 'fancy_grid', 'github', 'pipe', 'orgtbl', 'jira', 'presto', 'psql', 'rst', 'mediawiki', 'moinmoin', 'youtrack', 'html', 'latex', 'latex_raw', 'latex_booktabs', 'tsv', 'textile']


# Each element in the table list is a row in the generated table
table = [["spam",42], ["eggs", 451], ["bacon", 0]]
headers = ["item", "qty"]

for f in format_list:
    print("\nformat: {}\n".format(f))
    print(tabulate(table, headers, tablefmt=f))