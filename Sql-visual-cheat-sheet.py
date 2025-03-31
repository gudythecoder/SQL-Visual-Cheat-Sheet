%matplotlib inline
import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Define nodes and manual positions (for flowchart layout)
positions = {
    "SQL": (0, 6),
    "SELECT": (0, 5),
    "FROM": (-3, 4),
    "WHERE": (-3, 3),
    "AND / OR / NOT": (-4, 2),
    "IN / BETWEEN / LIKE / IS NULL": (-2, 2),
    "GROUP BY": (-1, 4),
    "HAVING": (-1, 3),
    "ORDER BY": (1, 4),
    "ASC / DESC": (1, 3),
    "LIMIT": (2, 4),
    "JOINS": (3, 4),
    "INNER JOIN": (2.5, 3),
    "LEFT JOIN": (3, 3),
    "RIGHT JOIN": (3.5, 3),
    "FULL JOIN": (4, 3),
    "INSERT INTO": (-3, 1),
    "VALUES": (-3, 0),
    "UPDATE": (0, 1),
    "SET": (-0.5, 0),
    "WHERE (Update)": (0.5, 0),
    "DELETE FROM": (3, 1),
    "WHERE (Delete)": (3, 0)
}

# Define graph edges
edges = [
    ("SQL", "SELECT"),
    ("SELECT", "FROM"),
    ("FROM", "WHERE"),
    ("WHERE", "AND / OR / NOT"),
    ("WHERE", "IN / BETWEEN / LIKE / IS NULL"),
    ("SELECT", "GROUP BY"),
    ("GROUP BY", "HAVING"),
    ("SELECT", "ORDER BY"),
    ("ORDER BY", "ASC / DESC"),
    ("SELECT", "LIMIT"),
    ("SELECT", "JOINS"),
    ("JOINS", "INNER JOIN"),
    ("JOINS", "LEFT JOIN"),
    ("JOINS", "RIGHT JOIN"),
    ("JOINS", "FULL JOIN"),
    ("SQL", "INSERT INTO"),
    ("INSERT INTO", "VALUES"),
    ("SQL", "UPDATE"),
    ("UPDATE", "SET"),
    ("UPDATE", "WHERE (Update)"),
    ("SQL", "DELETE FROM"),
    ("DELETE FROM", "WHERE (Delete)")
]

G.add_edges_from(edges)

# Node color categories
color_map = {
    "SQL": "#32CD32",                # Root
    "SELECT": "#4B8BBE",             # Core command
    "FROM": "#4B8BBE",
    "WHERE": "#4B8BBE",
    "AND / OR / NOT": "#79B473",     # Conditions
    "IN / BETWEEN / LIKE / IS NULL": "#79B473",
    "GROUP BY": "#4B8BBE",
    "HAVING": "#79B473",
    "ORDER BY": "#4B8BBE",
    "ASC / DESC": "#79B473",
    "LIMIT": "#4B8BBE",
    "JOINS": "#9370DB",              # Joins group
    "INNER JOIN": "#D8BFD8",
    "LEFT JOIN": "#D8BFD8",
    "RIGHT JOIN": "#D8BFD8",
    "FULL JOIN": "#D8BFD8",
    "INSERT INTO": "#306998",        # DML
    "VALUES": "#79B473",
    "UPDATE": "#FFB000",
    "SET": "#79B473",
    "WHERE (Update)": "#79B473",
    "DELETE FROM": "#DC143C",
    "WHERE (Delete)": "#79B473"
}

# Assign colors
node_colors = [color_map.get(node, "#D3D3D3") for node in G.nodes]

# Draw the graph
plt.figure(figsize=(20, 12))
nx.draw(G, pos=positions, with_labels=True, node_color=node_colors,
        node_size=4000, font_size=10, font_weight='bold', edge_color='#999999',
        arrows=True)

# Branding + title
plt.title("Core SQL Commands Flowchart", fontsize=18, weight='bold')
plt.figtext(0.5, 0.03, "Created by Goodness Rex Nze-Igwe | github.com/gudythecoder", 
            ha="center", fontsize=10)


plt.axis('off')
plt.subplots_adjust(bottom=0.1) 
plt.show()
plt.savefig("Core_SQL_Flowchart.png", dpi=300)
