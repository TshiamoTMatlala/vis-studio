from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# Define a dictionary where keys are genres and values are search queries for each genre on YouTube.
search_queries = {
    "pop": "pop music",
    "rock": "rock music",
    "hip-hop": "hip-hop music",
    "nu-metal": "nu-metal music",
    "jazz": "jazz music",
    "classical": "classical music",
    "country": "country music",
    "rnb": "rnb music",
    # Add more genres and search queries as needed
}

def search_music_on_youtube():
    genre = input("Enter a genre (e.g., pop, rock, hip-hop): ").lower()

    # Check if the entered genre exists in the dictionary
    if genre in search_queries:
        search_query = search_queries[genre]
        # Set up Chrome WebDriver
        driver = webdriver.Chrome()

        # Open the Chrome browser and navigate to YouTube
        driver.get("https://www.youtube.com")

        # Wait for the search input field to become available
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )

        # Enter the search query and submit the form
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

        # Sleep for a few seconds to allow search results to load
        time.sleep(5)

        # Retrieve and print the search results from YouTube using XPath
        search_results = driver.find_elements(By.XPATH, "//h3[contains(@class, 'style-scope ytd-video-renderer')]/a")
        if search_results:
            random_result = random.choice(search_results)
            random_song = random_result.text
            random_result.click()  # Click on the selected video
            print(f"Here's a random {genre} song suggestion on YouTube: {random_song}")
        else:
            print(f"No search results found for '{search_query}' on YouTube")

        # Close the browser
        driver.quit()
    else:
        print(f"Sorry, we don't have search queries for the '{genre}' genre on YouTube.")

if __name__ == "__main__":
    search_music_on_youtube()
