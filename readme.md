## A simple bot to increase website views
**Getting Started:**

`prerequisite:`

1. Install firefox.
2. Install geckodriver for Firefox. [Download here](https://github.com/mozilla/geckodriver/releases)
3. Install Git in your System.

Now, let's start using this Bot in your system as well.

**Clone the repository**

Enter the following command in your terminal:
```
git clone https://github.com/AmandracOP/automting-mlsa-viewership.git
cd automting-mlsa-viewership
```
 Firstly, Change the path according to your path of geckodriver(it should be executable):
 
> In line 15 replace the path with your path

 Now, Lets start an virtual enviornment in your system `venv`(Optional but recommended):
```
python -m venv navenv
source venv/bin/activate  # For Linux/macOS
venv\\Scripts\\activate.bat  # For Windows
```
 **Install Dependencies:**
  
  Activate your virtual environment and install the required packages listed in `requirements.txt`:

```
pip install -r requirements.txt
```

 **Run the Application:**
 Start the bot by running:

```
python main.py
```
