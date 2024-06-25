from dash import Dash, html, dash_table, Input, Output, State
from server import server
import layout
from database import insert_or_update_db
import dash

app = Dash(__name__, server=server)
app.layout = layout.serve_layout


@app.callback(
    Output("editable-table", "data"),
    [Input("add-row-button", "n_clicks"), Input("save-button", "n_clicks")],
    [State("editable-table", "data"), State("editable-table", "data_previous")],
)
def update_table(add_clicks, save_clicks, rows, prev_rows):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = "No clicks yet"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "add-row-button":
        rows.append({"id": len(rows) + 1, "A": "", "B": ""})
    elif button_id == "save-button" and rows != prev_rows:
        insert_or_update_db(rows)

    return rows


if __name__ == "__main__":
    app.run_server(debug=True)
