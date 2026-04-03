import pytest
from app import app

@pytest.fixture
def dash_duo_server(dash_duo):
    dash_duo.start_server(app)
    return dash_duo

def test_header_present(dash_duo_server):
    dash_duo_server.wait_for_element("#header", timeout=10)

def test_visualization_present(dash_duo_server):
    dash_duo_server.wait_for_element("#sales-line-chart", timeout=10)

def test_region_picker_present(dash_duo_server):
    dash_duo_server.wait_for_element("#region-filter", timeout=10)
