# tests/test_page1.py
def test_page1_widgets(page):
    page.goto("http://localhost:8501/page1")

    # Check the title
    assert page.title() == "page1"
    # Check for the presence of the header
    assert page.inner_text("h1") == "Page 1 - Widgets Galore"
