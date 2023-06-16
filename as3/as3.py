from flask import Flask

as3 = Flask(__name__)

@as3.route('/api/printHello',methods=['GET', 'POST'])
def print_hello():

    hello = "/home/noel/skillrank/noel_learnrepo/as3/1.py"
    with open(hello, 'r') as file:
        hello_content = file.read()
    return hello_content


@as3.route('/api/modifyRecepie', methods=['GET', 'POST'])
def modify_recipe():

    recipe = "/home/noel/skillrank/noel_learnrepo/as3/ex5.json"
    with open(recipe, 'r') as file:
        recipe_content = file.read()
    return recipe_content
if __name__ == '__main__':
    as3.run(debug=True)

