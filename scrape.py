import requests, bs4
import numpy as np

# difficulty: 1=easy, 2=medium, 3=hard, 4=evil
def getboard(difficulty):
    # gets the website
    res = requests.get('http://nine.websudoku.com/?level=' + str(difficulty))
    res.raise_for_status()
    # saves the HTML elements of the board values
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    grid = soup.select('#puzzle_grid td input')

    # extracts the values
    values = [int(x.attrs.get('value', 0)) for x in grid]

    # return the array in grid format
    return np.array_split(values, 9)