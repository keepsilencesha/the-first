import os,sys
from  core  import  src
BEAS=os.path.dirname(__file__)
sys.path.append(BEAS)
if __name__ == '__main__':
    src.run()