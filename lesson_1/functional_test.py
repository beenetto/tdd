from selenium import webdriver

browser = webdriver.Firefox()

# USER visits homepage
browser.get('http://localhost:8000')

# User sees "Django" in the page title
assert 'Django' in browser.title

# User invited to enter a to-do list item straight away

# User types "My to do" into the textbox

# When user hits ENTER, the page updates
# "1: My to-do" as an item in the to-do list

# There is still a textbox inviting the user to add an other item.
# User enters "My second to do"

# Page updates again and shows both items

# User notices that there is a unique url generated

# User visits that URL and sees that the enered itms are still in the list

# User finishes

browser.quit()
