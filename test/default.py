import os
from selenium.common.exceptions import TimeoutException

from . import Driver
from . import Config
from . import Log

from ..elements.button import Button
from ..elements.checkbox import CheckBox
from ..elements.label import Label
from ..elements.radiobutton import RadioButton
from ..elements.selectfield import SelectField
from ..elements.textfield import TextField


def test_on_local_default_webpage(browserName, webdriverPath):
    Config.set(browser=browserName)
    Config.set(webdriver=webdriverPath)
    
    driver = Driver()

    # Load default testform
    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path)
    testpage = os.path.join(dir_path, 'testforms', 'default.html')
    driver.get(testpage)

    form = {
        'firstname_label': Label(name='firstname_label'),
        'firstname': TextField(name='firstname'),

        'lastname_label': Label(name='lastname_label'),
        'lastname': TextField(name='lastname'),

        'pref-numbers_label': Label(name='pref-numbers_label'),
        'pref-numbers': SelectField(name='pref-numbers'),

        'this_label': Label(name='this_label'),
        'this': RadioButton(name='this'),
        'that_label': Label(name='that_label'),
        'that': RadioButton(name='that'),

        'science_label': Label(name='science_label'),
        'science': CheckBox(name='science'),
        'technology_label': Label(name='technology_label'),
        'technology': CheckBox(name='technology'),
        'engineering_label': Label(name='engineering_label'),
        'engineering': CheckBox(name='engineering'),
        'mathematics_label': Label(name='mathematics_label'),
        'mathematics': CheckBox(name='mathematics'),

        'click-me': Button(name='click-me'),
        #'do-not-click-me': Button(name='do-not-click-me'),

        # Page element which shows validation state for required interactions
        'validated': Label(id='validated')
    }

    # Click all required form elements
    for key in form:
        form[key].click()

    # Enter generic text into 'firstname' and 'lastname' textfields
    form['firstname'].text = 'Ada'
    form['lastname'].text = 'Lovelace'

    # Select 'Prime' for 'pref-numbers'
    form['pref-numbers'].select(text='Prime')

    # Check for pass in valid element (this may need to be changed)
    validated = form['validated']
    try:
        validated.waitForValue('TRUE')

    except TimeoutException:
        raise Error('>>>>>>> FAIL')
    if 'TRUE' in validated.text:
        print('>>>>>>> PASS')
    assert('TRUE' in validated.text)
