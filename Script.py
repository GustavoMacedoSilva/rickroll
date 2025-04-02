from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)  # Allow the browser to run in the background
options.add_argument("--start-maximized")  # Start maximized

driver = webdriver.Edge(options=options)
driver.get("https://shattereddisk.github.io/rickroll/rickroll.mp4")