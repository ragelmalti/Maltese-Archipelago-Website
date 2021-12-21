#ザクロン
import os
import sys
beforel = []
afterl = []
doc  = input("File name: ")
with open('c:/Users/Zachary/Desktop/'+doc+'.html', 'r', encoding='utf8') as file:
    for line in file:
        if line.find("<title>") > -1 or line.find("<!DOCTYPE html>") > -1 or line.find("<html>") > -1 or line.find("<head>") > -1:
            beforel.append(line)
        else:
            afterl.append(line)
with open("c:/Users/Zachary/Desktop/"+doc+".html", "w", encoding='utf8') as file:
    for line in beforel:
        file.write(line)
    file.write('\t\t<meta charset="utf-8"/>\n\t\t<meta name="keywords" content="Malta, history, culture, language, religion"/>\n\t\t<meta name="description" content="Website containing original articles, and other web resources, on the Maltese Archipelago."/>\n\t\t<meta name="robots" content="index,follow" />\n\t\t<!--Open Graph Meta tags -->\n\t\t<meta name="og:title" content="Maltese Archipelago Information"/>\n\t\t<meta name="og:description" content="Website containing original articles, and other web resources, on the Maltese Archipelago."/>\n\t\t<meta name="og:image" content="/open-graph.png"/>\n\t\t<meta name="og:type" content="website"/>\n\t\t<meta name="og:url" content="https://maltese-archipelago-info.neocities.org/"/>\n\t\t<!--Link tags -->\n\t\t<link rel="shortcut icon" type="image/jpg" href="images/tab.ico"/>\n\t\t<link rel="stylesheet" type="text/css" href="style.css"/>')
    for line in afterl:
        file.write(line)
