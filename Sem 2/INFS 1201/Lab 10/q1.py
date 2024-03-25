##
# Gowshikrajan Senthilkumar - 60307390
# Week13 Lab10
# Exercise 1

def createRectangleHtml(fileName, width, height, color):
    html_f = open(fileName, 'w')

    html_f.write(f'<html>\n\t'\
                 f'<body>\n\t\t'\
                 f'<div style="width:{width}px;height:{height}px;'\
                 f'background:{color}">'\
                 f'</div>\n\t</body>'\
                 f'\n</html>')
    
    html_f.close()

