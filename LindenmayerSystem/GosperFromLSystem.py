import sys
sys.path.insert(0,'./LindenmayerSystem')
sys.path.insert(1,'.')
from LSystem import LSystem

if __name__ == '__main__':
    rules_dict={'A':'A-B--B+A++AA+B-', 'B':'+A-BB--B-A++A+B'}
    start_string='A'    
    measures_dict = {'length':4, 'angle':60}
    fn_dict = {'A':lambda turtle1: turtle1.forward(measures_dict['length']), 
            'B':lambda turtle1: turtle1.forward(measures_dict['length']), 
            '-':lambda turtle1: turtle1.right(measures_dict['angle']),
            '+':lambda turtle1: turtle1.left(measures_dict['angle']),}

    ls = LSystem(start_string=start_string, rules_dict=rules_dict, iterations=3, fn_dict=fn_dict)
    ls.display()
    ls.end_this()