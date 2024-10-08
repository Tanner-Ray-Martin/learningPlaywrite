# tests/test_page4.py
def test_page4_interactive_widgets(page):
    page.goto("http://localhost:8501/page4")

    # Check the title
    assert page.title() == "page4"
    # Check for the presence of the header
    assert page.inner_text("h1") == "Page 4 - Interactive Widgets"
