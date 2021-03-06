import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from components import news_feed, twitter_feed
from components import confirmed_cases_chart, infection_trajectory_chart
from components import confirmed_scatter_mapbox, drive_thru_scatter_mapbox
from components import daily_stats_mobile
from components import scatter_mapbox
from components import news_feed, twitter_feed
from pages import mobile_navbar, mobile_footer


build_mobile_layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dbc.Navbar(id="navbar-content", color="#010915", dark=True, className="fixed-navbar",),
        dbc.Container(id="page-content", className="mt-4", fluid=True),
        dbc.Container(id="footer-content", className="footer-content", fluid=True)
    ]
)