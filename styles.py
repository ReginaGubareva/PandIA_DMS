colors = {
    "h1": "#98703A",
    "h2": "#D893C2"
}

table_colors = [
    {
        'background': '#B9E0FF',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#8D9EFF',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#8D72E1',
        'text': 'rgb(30, 30, 30)'
    },
    {
        'background': '#6C4AB6',
        'text': 'rgb(30, 30, 30)'
    },
]

table = {
    'maxHeight': '50ex',
    'overflowY': 'scroll',
    'width': '45%',
    'minWidth': '45%',
}

cell = {
    'fontFamily': 'Open Sans',
    'textAlign': 'center',
    'height': '30px',
    'width': '20px',
    'padding': '2px 12px',
    'whiteSpace': 'inherit',
    'overflow': 'hidden',
    'textOverflow': 'ellipsis',
}

header = {
    'fontWeight': 'bold',
    'backgroundColor': 'white'
}

stripped_rows = {
    'if': {'row_index': 'odd'},
    'backgroundColor': 'rgb(248, 248, 248)'
}

table_row_highlight = {
    'if': {'row_index': 4},
    "backgroundColor": "#3D9970",
    'color': 'white'
}

h1 = {
    "fontSize": "32px",
    "color": colors['h1'],
    'text_align': ''
}

h2 = {
    "color": colors['h2'],
    'text_align': 'center'
}

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "30%",
    "padding": "4rem 2rem",
    "background-color": "#B4CDE6",
    "font-size": "20px",
    "text-color": "white",
    "text-align": "right",
}

CONTENT_STYLE_HOME = {
    "margin-left": "13rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

NAVLINK_STYLE = {
    "color": "white",
    "font-size": "20px",
    "text-decoration": "none",
    "display": "flex",
    "justify-content": "flex-start",
    "align-items": "stretch",
    "flex-direction": "row",
    'if acitve': {"color": "green"}
}
