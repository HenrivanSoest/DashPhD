import networkx
import pandas as pd
pd.set_option('max_rows', 400)
import matplotlib.pyplot as plt

got_df = pd.read_csv('C:\Users\Henri van Soest\Documents\PhD\Writing\Year 3 Writeup\4 Framework\Framework_Timeline2.csv')

G = networkx.from_pandas_edgelist(got_df, 'Source', 'Target', 'Area', 'Year_of_proposal', 'Year_of_entry_into_force', 'Year_of_exit', 'Url')

networkx.write_graphml(G, 'GOT-network.graphml')

plt.figure(figsize=(8,8))
networkx.draw(G, with_labels=True, node_color='skyblue', width=.3, font_size=8)
plt.show()
