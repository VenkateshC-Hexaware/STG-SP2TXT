import sys
import logging
logging.basicConfig(stream=sys.stderr)

# Path of the Flask APP must be set to access files
sys.path.insert(0,"D:/ISGSPP/")

# Below code is required if you use virtualenv to run your app
# Get the activate_this.py in your <virtual_env>/Scripts and add here
# activate_this = 'D:/non-anaconda-env/Scripts/activate_this.py'
# with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this)) 

from app import app as application