# tests/test_page2.py
def test_page2_charts(page):
    page.goto("http://localhost:8501/page2")

    # Check the title
    assert page.title() == "page2"
    # Check for the presence of the header
    assert page.inner_text("h1") == "Page 2 - Data Visualization"
