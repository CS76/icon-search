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
import ssl
from os.path import basename
from bs4 import BeautifulSoup, NavigableString
from algoliasearch import algoliasearch

icons = []

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    args = parser.parse_args(arguments)
    client = algoliasearch.Client("********", "************************")
    index = client.init_index('icon-search')
    scrapeZurbCheatsheet()
    scrapeMaterialCheatsheet()
    scrapeFontAwesomeCheatsheet()
    scrapeIconicCheatsheet()
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