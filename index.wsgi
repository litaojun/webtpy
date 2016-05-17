import sys  
import os.path  

sys.path.append(os.path.join(os.path.dirname(__file__), 'test'))  
    
import sae  
from test import myweb  
    
application = sae.create_wsgi_app(myweb.testweb)