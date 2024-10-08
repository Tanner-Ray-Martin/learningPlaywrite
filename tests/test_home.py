# tests/test_streamlit_app.py


def test_main_page(page):
    page.goto("http://localhost:8501")

    # Check the title
    assert page.title() == "Streamlit Feature Showcase"

    # Check for the presence of the header
    assert page.inner_text("h1") == "Navigation"

    # Interact with the button
    button = page.get_by_role("button", name="Say hello")
    button.click()
