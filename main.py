from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
# Function defination
def course_sites(url):
    # Set Firefox options
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--private")

    # Path to GeckoDriver executable
    webdriver_path = '/usr/bin/geckodriver'

    # Initialize GeckoDriver service
    service = Service(executable_path=webdriver_path)

    # Initialize WebDriver
    driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        # Open urls
        driver.get(url)
        time.sleep(random.uniform(4, 7))  

        scroll_position = random.randint(200, 900)
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(random.uniform(4, 7))  

        button = driver.find_element(By.ID, "start-unit") #button by id
        actions = ActionChains(driver)
        actions.move_to_element(button).perform()  
        time.sleep(random.uniform(4, 8))  
        button.click()

        time.sleep(random.uniform(4, 7))  
        # Perform scrolling up and down multiple times
        num_scrolls = random.randint(5, 8)
        for _ in range(num_scrolls):
            # Scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(4, 6))  # Random wait 

            # Scroll back up to the top of the page
            driver.execute_script("window.scrollTo(0, 0);")
            time.sleep(random.uniform(5, 8))  # Random wait 
        another_button = driver.find_element(By.CLASS_NAME, "button button-clear text-decoration-none button-sm unit-expander") # button by class name
        actions.move_to_element(another_button).perform()  
        time.sleep(random.uniform(6, 8))  
        another_button.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(4, 7))  

    except Exception as e:
        print(f"Error processing {url}: {str(e)}")

    finally:
        # Close browser session
        driver.quit()
        driver.service.stop()


# calling the function
#adding ambassador ID at the end of the url- ?wt.mc_id=studentamb_386718
urls= ["https://learn.microsoft.com/en-us/training/paths/sql-server-2017-on-linux/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/ai-education/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/21st-century-learning-design/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/microsoft-educator-academy/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/master-microsoft-teams-any-learning-environment/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/explore-computer-vision-microsoft-azure/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/data-analytics-microsoft/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/extract-data-from-forms-document-intelligence/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/introduction-generative-ai/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-core-data-concepts/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/document-intelligence-knowledge-mining/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/create-computer-vision-solutions-azure-ai/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/az-104-administrator-prerequisites/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/prepare-data-power-bi/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-data-warehouse-analytics/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-1/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/power-plat-fundamentals/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/mie-trainer-academy-learning-path/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/describe-microsoft-365-core-services-concepts/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/describe-concepts-of-security-compliance-identity/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/get-started-with-microsoft-365-copilot/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/get-transform-data-power-bi/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/model-data-power-bi/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/microsoft-azure-architect-design-prerequisites/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/m365-security-compliance-capabilities/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/describe-capabilities-of-microsoft-identity-access/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/design-machine-learning-solution/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/get-started-c-sharp-part-3/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/manage-workspaces-datasets-power-bi/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/office-365-teacher-academy/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/get-started-office-365-windows/?wt.mc_id=studentamb_386718",
    "https://learn.microsoft.com/en-us/training/paths/beginner-python/?wt.mc_id=studentamb_386718" ]
for url in urls:
    try:
        course_sites(url)
    except Exception as e:
        print(f"Error processing {url}: {str(e)}") 
