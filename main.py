from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

# Function to perform actions on a website
def course_sites(url):
    # Set Firefox options
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--private")

    # Path to GeckoDriver executable
    webdriver_path = '/usr/bin/geckodriver'

    # Initialize the GeckoDriver service
    service = Service(executable_path=webdriver_path)

    # Initialize the WebDriver
    driver = webdriver.Firefox(service=service, options=firefox_options)

    try:
        # Open the URL from the function defined3   
        driver.get(url)
        time.sleep(2)  # Wait for 
        
        # Scroll down the page
        driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)  # Wait for 
        
        # Click on a button
        button = driver.find_element(By.ID, "start-unit")
        button.click()
        time.sleep(3)  # Wait for 
        
        # Go back to the site
        driver.get(url)
        time.sleep(2)  # Wait for 
        
        # Click some more buttons
        another_button = driver.find_element(By.CLASS_NAME, "button button-clear text-decoration-none button-sm unit-expander")
        another_button.click()
        time.sleep(2)  # Wait for 
        
        # Example of scrolling again
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Wait for 
        
    finally:
        # Close browser
        driver.quit()
        driver.service.stop()
# calling the function
#add ambassador ID at the end of the url- ?wt.mc_id=studentamb_386718
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