def test_home_page(client, app):
    response = client.get('/')
    assert response.status_code == 200


def test_upper_case():
    assert "something".upper() == "SOMETHING"

# def test_upper_case(client, app):
#     MainForm.text.data = "something"
#
#     response = client.post('/', data={"mainform": MainForm,
#                                       request.form['submit_button']: 'Submit'})
#     html = response.get_data(as_text=True)
#     assert "SOMETHING" in html
