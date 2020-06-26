'''
Author: Manohar Chitoda

This program is for automation of common uses on LinkedIn

'''

from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os,random,time,sys

# Handels invalid input
def invalid():
	messagebox.showinfo("Error","Invalid Option")
	ask()

# Asks for choices
def ask():
	choice = simpledialog.askinteger("Choice","Choose the following options!\n1: Post something\n2: Find Someone\n")
	switch_replacement(choice)
	
# Direct the choices
def switch_replacement(choice):
	switcher = {
		1: post,
		2: findProfile
	}
	fun = switcher.get(choice,lambda: invalid())
	fun()

# Choice of posting something
def post():
	post_stmt = simpledialog.askstring("Post", "What do you want your post to say?")
	print(post_stmt)

# Choice of finding a profile
def findProfile():
	find_this = simpledialog.askstring("Post", "Who are you looking for?\n\nEnter the name in lowercase & without any space!")
	browser.get("https://www.linkedin.com/in/" + find_this + "/")

# Main program
if __name__ == "__main__":
	browser = webdriver.Chrome("driver/chromedriver")
	#Open the linkedin login page
	browser.get('https://www.linkedin.com/login')

	#Opening the config file that has my credentials 
	file = open('config.txt')
	lines = file.readlines()
	username = lines[0]
	password = lines[1]

	#insert username in the email field
	elementID = browser.find_element_by_id('username')
	elementID.send_keys(username)

	# insert password in the password field
	elementID = browser.find_element_by_id('password')
	elementID.send_keys(password)

	# submit and login
	elementID.submit()
	app_window = tk.Tk()
	ask()