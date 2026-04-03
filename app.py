from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = Dash(__name__)

# Load the data
df = pd.read_csv('formatted_data.csv')

# Ensure Date is in datetime format and sort by date
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# Create the visualization
fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales Over Time")

# Customize the chart appearance
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#cbd5e1',
    xaxis=dict(
        showgrid=False,
        title_font=dict(size=18, color='#f1f5f9'),
        tickfont=dict(size=14, color='#94a3b8')
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='rgba(255, 255, 255, 0.1)',
        title_font=dict(size=18, color='#f1f5f9'),
        tickfont=dict(size=14, color='#94a3b8')
    ),
    margin=dict(l=40, r=40, t=80, b=40),
    hovermode="x unified"
)

# Add a vertical line for the price increase on Jan 15, 2021
fig.add_shape(
    type="line",
    x0="2021-01-15", y0=0, x1="2021-01-15", y1=1,
    xref="x", yref="paper",
    line=dict(color="#f87171", width=3, dash="dash")
)

fig.add_annotation(
    x="2021-01-15", y=0.95,
    xref="x", yref="paper",
    text="Price Increase",
    showarrow=False,
    font=dict(color="#f87171", size=14),
    xanchor="left"
)

# Define the layout
app.layout = html.Div(children=[
    html.Header(id='header', children=[
        html.H1("Pink Morsel Sales Visualizer")
    ]),
    
    html.Div(id='visualization', className='card', children=[
        dcc.Graph(
            id='sales-line-chart',
            figure=fig
        )
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
