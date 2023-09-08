from Final_project.project import goals_bar, occupy_table, line_graph

def test_goals_bar():
    assert goals_bar("Arsenal") == "The highest scorer in Arsenal was Pierre-Emerick Aubameyang with 22 goals."

def test_occupy_table():
    assert occupy_table("Arsenal") == "Arsenal's average attendance was: 29949"

def test_line_graph():
    assert line_graph("Arsenal") == "Arsenal scored 73 goals in the 2018/19 season"
