import dashCode

def test_radioExist(dash_duo):
    app=dashCode.Dash()
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region").text == "All"
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    dash_duo.percy_snapshot("test_001_child_with_0-layout")
