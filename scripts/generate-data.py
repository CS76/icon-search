#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Venkata chandrasekhar Nainala 
# Version: 0.1.0
# Email: mailcs76@gmail.com 

""" Scrape 
"""

import os
import sys
import json
import urllib2
import argparse
import time
import requests
import csv
import json
import ssl
from os.path import basename
from bs4 import BeautifulSoup, NavigableString
from algoliasearch import algoliasearch

icons = []

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    args = parser.parse_args(arguments)
    client = algoliasearch.Client("OMA2ZHV973", "f16887717d3551149308c550f5caa179")
    index = client.init_index('dev-icon-search')
    # scrapeZurbCheatsheet()
    # scrapeMaterialCheatsheet()
    # scrapeFontAwesomeCheatsheet()
    # scrapeIconicCheatsheet()
    scrapeFontAwesome5Cheatsheet()
    global icons
    writeDataToFile("data.json",icons)
    index.add_objects(icons)

def scrapeMaterialCheatsheet():
	printText("Fetching Material Data")
	materialURL = "https://material.io/icons/data/";
	materialRequest = requests.get(materialURL+"grid.json")
	global icons
	for icon in materialRequest.json()['icons']:
		iconJSON = requests.get(materialURL+icon['id']+".json").json()
		icon = {}
		icon["source"] = "material"
		icon["category"] = iconJSON['group_id']
		icon["source"] = "material"
		icon["name"] = iconJSON['name']
		icon["unicode"] = '&#x' + iconJSON['codepoint'] + ";"
		icon["assets"] = iconJSON['assets']
		icon['search'] = iconJSON['keywords']
		icon['version'] = "v3.0.1"
		icon['class'] = iconJSON['ligature']
		icon['search'].append(iconJSON['name'].strip())
		icon["objectID"] = "mi-" + iconJSON['ligature']
		print icon["objectID"]
		icons.append(icon)
	printText(str(len(icons)))

def scrapeIconicCheatsheet():
	printText("Fetching Iconic Data")
	iconicURL = "https://useiconic.com/open";
	cheatSheetHTML = requests.get(iconicURL).text;
	cheatSheetSoup = BeautifulSoup(cheatSheetHTML, "html.parser")
	iconsDiv = cheatSheetSoup.findAll("div", { "class" : "icon-item" })
	global icons
	for iconDiv in iconsDiv:
		icon = {}
		icon["source"] = "iconic"
		icon["name"] = iconDiv.find("p").text
		icon["search"] = [iconDiv.find("p").text.strip()]
		icon["assets"] = {} 
		iconImg = iconDiv.findAll("div", {'class':"icon-code-img"})
		icon["assets"]['img'] = iconImg[0].find("input")['value'].replace("\"","'")
		icon["assets"]['svg'] = iconImg[1].find("input")['value'].replace("\"","'")
		icon["assets"]['font'] = iconDiv.find("div", {'class':"icon-code-font"}).find("input")['value'].replace("\"","'")
		icon["assets"]['bootstrap'] = iconDiv.find("div", {'class':"icon-code-bootstrap"}).find("input")['value'].replace("\"","'")
		icon["assets"]['foundation'] = iconDiv.find("div", {'class':"icon-code-foundation"}).find("input")['value'].replace("\"","'")
		icon["version"] = '1.1.0'
		icon["category"] = '-'
		icon["objectID"] = "oi-" + icon["name"]
		print icon["objectID"]
		icons.append(icon)
	printText(str(len(icons)))

def scrapeZurbCheatsheet():
	printText("Fetching Foundation Data")
	# zurbURL = "https://zurb.com/playground/foundation-icon-fonts-3";
	cheatSheetHTML = open("zurb.html","r")
	cheatSheetSoup = BeautifulSoup(cheatSheetHTML, "html.parser")
	categories = cheatSheetSoup.findAll("h2", { "class" : "with-download-link" })
	global icons
	for category in categories:
		categoryName = category.text
		fontsUL = category.findNext('ul')
		for fontLI in fontsUL.findAll("li",recursive=False):
			icon = {}
			icon["search"] = [fontLI.find("p").text.strip()]
			icon["source"] = "foundation"
			icon["name"] = fontLI.find("p").text
			icon["class"] = fontLI.find("i")['class'][0]
			icon["version"] = 3
			icon["category"] = categoryName
			icon["objectID"] = "z-" + icon["class"]
			print icon["objectID"]
			icons.append(icon)
	printText(str(len(icons)))

def scrapeFontAwesome5Cheatsheet():
	printText("Fetching FontAwesome 5 Data")
	cheatSheetHTML = open("FontAwesome5.htm","r")
	cheatSheetSoup = BeautifulSoup(cheatSheetHTML, "html.parser")
	wrapperDiv = cheatSheetSoup.find("section", { "id" : "results-icons" })
	fonts = wrapperDiv.findAll("li", { "class" : "dib" })
	global icons
	i = 0 
	for font in fonts:
		icon = {}
		faIconAnchor = font.findAll("a", {"class", "hover-bg-blue4"})[0]
		faPrefix = faIconAnchor.findAll("svg")[0]["data-prefix"]
		faIconURL =faIconAnchor['href']
		faIcon = faIconURL.replace("https://fontawesome.com/icons/","").split("?")[0]
		fontawesomeIconHTML = requests.get(faIconURL).text
		fontawesomeIconSoup = BeautifulSoup(fontawesomeIconHTML, "html.parser")
		icon["source"] = "fontawesome5"
		icon["name"] = faIcon
		topDiv = fontawesomeIconSoup.findAll("div", { "class", "relative" })[0]
		iconJSON = json.loads(topDiv.findAll("script")[0].text.strip().replace("window.__inline_data__ = ", ""))
		for iconData in iconJSON:
			if "relationships" in iconData["data"]:
				icon["categories"] = []
				if "categories" in iconData["data"]["relationships"]:
					for iconCat in iconData["data"]["relationships"]["categories"]["data"]:
						icon["categories"].append(iconCat["id"])
				icon["search"] = iconData["data"]["attributes"]["search"]["terms"]
				icon["class"] = "fa-" + iconData["data"]["attributes"]['id']
				icon["unicode"] = iconData["data"]["attributes"]['unicode']
				icon["prefix"] = faPrefix
				icon["version"] = "5.0.0"
		if len(icon["search"]) == 0:
			icon["search"].append(icon["name"])
		if len(icon["categories"]) == 0:
			icon["categories"].append("-")
 		icon["objectID"] = "fa5-"+faPrefix+"-"+faIcon
		icons.append(icon)
		i = i + 1
		print i
	printText(str(len(icons)))


def scrapeFontAwesomeCheatsheet():
	# client = algoliasearch.Client("**********", "************************")
	# index = client.init_index('font_awesome')
	fontawesomeURL = "http://fontawesome.io/icons/";
	printText("Fetching FontAwesome Data")
	cheatSheetHTML = requests.get(fontawesomeURL).text
	cheatSheetSoup = BeautifulSoup(cheatSheetHTML, "html.parser")
	wrapperDiv = cheatSheetSoup.find("div", { "id" : "icons" })
	fonts = wrapperDiv.findAll("div", { "class" : "fa-hover" })
	global icons
	for font in fonts:
		icon = {}
		faIcon = font.findAll("a")[0]['href'].replace("../icon/","")
		aliases = font.findAll("span", { "class" : "text-muted" })
		icon["search"] = []
		if len(aliases) > 0:
			for alias in aliases:
				if len(alias.findAll("em")) > 0:
					icon["search"].append((alias.findAll("em")[0]).text.strip())
		icon["search"].append(faIcon.strip()) 
		try:
			fontawesomeIconURL = "http://fontawesome.io/icon/" + faIcon
			fontawesomeIconHTML = requests.get(fontawesomeIconURL).text
			fontawesomeIconSoup = BeautifulSoup(fontawesomeIconHTML, "html.parser")
			icon["source"] = "fontawesome"
			icon["name"] = faIcon
			h1Div = fontawesomeIconSoup.findAll("h1", { "class" : "info-class" })[0]
			icon["class"] = ''.join([element for element in h1Div if isinstance(element, NavigableString)]).replace("\n","").strip()
			icon["unicode"] = '&#x' + (h1Div.findAll("span", { "class" : "upper" })[0]).text + ";"
			smallDiv = h1Div.findAll("small")[0]
			smallDivContent = ''.join([element for element in smallDiv if isinstance(element, NavigableString)]).replace("\n","").strip().split(u'·')
			icon["version"] = (smallDivContent[2].split(":")[1]).strip()
			icon["category"] = (smallDivContent[3].split(":")[1]).strip()
			icon["objectID"] = "fa-" + faIcon
			print icon["objectID"]
			icons.append(icon)
		except:
			pass
	printText(str(len(icons)))

def printText(text):
	print text

def writeDataToFile(filename, data):
    with open(filename, "w") as fp:
        json.dump(data, fp)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))