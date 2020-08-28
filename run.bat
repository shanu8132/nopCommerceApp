rem pytest -v -s -m "sanity" --html=Reports\report.html src\testCases --browser chrome
pytest -v -s -m "sanity or regression" --html=Reports\report.html src\testCases --browser chrome
rem pytest -v -s -m "regression" --html=Reports\report.html src\testCases --browser chrome
rem pytest -v -s -m "sanity and regression" --html=Reports\report.html src\testCases --browser chrome