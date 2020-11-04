import inspect
import os
import re
import pytest
import math
import numpy as np
from scipy.special import softmax
import calculator as calc
import calculator.derivatives as drt



path = './calculator'
files = os.listdir(path)
file_names = []
for f in files:
    try:
        file_names.append(os.path.join(path, os.listdir(f)))
    except:
        pass

README_CONTENT_CHECK_FOR = ["sin"
,"d_sin"
,"cos"
,"d_cos"
,"tan"
,"d_tan"
,"tanh"
,"d_tanh"
,"log"
,"d_log"
,"exp"
,"d_exp"
,"softmax"
,"d_softmax"
,"relu"
,"d_relu"
,"sigmoid"
,"d_sigmoid"]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 6

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    for each_module in file_names:
        lines = inspect.getsource(each_module)
        spaces = re.findall('\n +.', lines)
        for space in spaces:
            assert len(space) % 4 == 2, f"Your script {each_module} contains misplaced indentations"
            assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    for each_module in file_names:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    for item in file_names:
        functions = inspect.getmembers(item, inspect.isfunction)
        for function in functions:
            if function[1].__name__ not in ['namedtuple', 'wraps']:
                assert function[1].__annotations__


def test_docstrings():
    '''
    Test caset to check docstrings in the function defn
    '''
    for folder in file_names:
        files = folder
        for file in files:
            funcs = inspect.getmembers(file, inspect.isfunction)
            for func in funcs:
                if func[1].__doc__ == None:
                    continue
                print(func[1].__doc__)
                assert func[1].__doc__

def test_sin():
    assert calc.sin(45,'degree') == math.sin(45)

def test_cos():
    assert calc.cos(45,'degree') == math.cos(45)

def test_tan():
    assert calc.tan(45,'degree') == math.tan(45)

def test_tanh():
    assert calc.tanh(45,'degree') == math.tanh(45)

def test_log():
    assert calc.log(45) == math.log(45)

def test_exp():
    assert calc.exp(45) == math.exp(45)

def test_softmax():
    # assert (calc.softmax([4,5,6,7]) == softmax([4,5,6,7])).any()
    assert np.allclose(calc.softmax([4,5,6,7]),softmax([4,5,6,7]))

def test_relu():
    assert calc.relu(5) == np.maximum(0,5)

def test_sigmoid():
    assert calc.sigmoid(7) == (1/(1 + np.exp(-7)))

def test_d_sin():
    assert drt.d_sin(45,'degree') == math.cos(45)

def test_d_cos():
    assert drt.d_cos(45,'degree') == -math.sin(45)

def test_d_tan():
    assert drt.d_tan(45,'degree') == 1/(math.cos(45))**2

def test_d_tanh():
    assert drt.d_tanh(45,'degree') == 1-(math.tanh(45))**2

def test_d_log():
    assert drt.d_log(45) == 1/45

def test_d_exp():
    assert drt.d_exp(45) == np.exp(45)

def test_d_softmax():
    val = 1-(math.atan(4)*math.atan(4))
    assert drt.d_softmax(4) == val

def test_d_relu():
    val = 1 if 5>0 else 0
    assert drt.d_relu(5) == val

def test_d_sigmoid():
    val = (1 / (1 + math.exp(-7))) * (1-(1 / (1 + math.exp(-7))))
    assert drt.d_sigmoid(7) == val
