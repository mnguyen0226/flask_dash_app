from dash import html, dash_table
from database import query_db
import pandas as pd


def get_dataframe():
    rows = query_db("SELECT * FROM data")
    return pd.DataFrame(rows, columns=["id", "A", "B"])


def serve_layout():
    return html.Div(
        [
            dash_table.DataTable(
                id="editable-table",
                columns=[{"name": i, "id": i} for i in ["id", "A", "B"]],
                data=get_dataframe().to_dict("records"),
                editable=True,
                row_deletable=True,
            ),
            html.Button("Add Row", id="add-row-button", n_clicks=0),
            html.Button("Save Changes", id="save-button", n_clicks=0),
        ]
    )
