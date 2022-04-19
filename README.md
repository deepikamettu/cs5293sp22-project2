# Author: Mettu Deepika  
## Project1: Cuisine Predictor  
This project will help us in creating an application that will take a list of ingredients from the user and predicts the type of cuisine and similar meals. The project proceeds as follows:  
- Train (or index for search) the food data in the provided.  
- Ask the user to input all the ingredients that they are interested in (through command-line arguments).  
- Use the model (or search index) to predict the type of cuisine and tell the user.  
- Find the top-N closest foods (N defined with a command-line parameter). Return the IDs of those dishes to the user.  
  
**The command used for running the project:**   
pipenv run python project2.py --N 3 --ingredient rice --ingredient flour  
  
**The command used for running the test scripts:**  
pipenv run python -m pytest
  
**The modules used for the project:**  
NumpyEncoder : pipenv install numpyencoder  
sklearn : pipenv install sklearn  
numpy: pipenv install numpy 
pandas: pipenv install pandas 
  
Running the project with the above given command-line argument will take the list of the ingredients provided by the user and the number  N and produces an output with a prediction of the type of cuisine and displays the top-N closest foods – returns the IDs of the dishes.  
  
The project2.py contains the following functions:  
- ***read(inpdata):***  
In this function, the data file “yummly.json” is read and stored in a variable called input_data which is further used in the program.  
- ***clean_data(input_data):***  
In this function, the input_data returned from the read() function is taken and cleaned. Meaning, in this case, the ingredients in the input file are converted from a list to a string so that it will be easy for us to proceed to further steps of training the model.  
- *result(ingredients,N,input_data):*  
In this function, the columns "ingredients" and "cuisine" are assigned to variables X and y for which train_test_split() is performed. For performing train_test_split(), 70% of the data is considered as train data and remaining 30% is considered as test data. Further "KNN" classifier is used by declaring a pipline which also consists of CountVecktorizer and TfidfTransformer. This pipeline is used to convert the entire tests into numeric format. Then a function dense() is used to convert it to matrix form. In this function .neighbours() function is used to find the distance between the data points. A data frame is created for appeding all the ID's, cuisines and distances to it. Futher a dictionary is initialized and is used for appending cusine along with its scores. Later on appending the closest meal Ids and their scores. Now, the dictionary is converted to json fomart using json.dumps() and then printing it to the console as follows:  
{  
    "Cuisine": "indian",  
    "score": 0.835,  
    "closest": [  
        {  
            "id": 899,  
            "score": 0.966  
        },  
        {  
            "id": 14745,  
            "score": 0.989  
        },  
        {  
            "id": 5192,  
            "score": 0.052  
        }  
    ]  
}    

  
**Test Cases:**  
Test cases are written in tests/test_project2.py.  
- ***test_read():***  
This method is used to test read() function in project2.py. The data file is passed to the read() function and the result is stored in a variable called input_data. This test_read() will assert True when the input_data is not None. Else it asserts False.
- ***test_clean_data():***  
This method is used to test clean_data() function in project2.py. The input_data that is read from the given file is passed as a parameter to clean_data() and the result is stored in a variable called res. This test_clean_data() function asserts True when the res is not None. Else it asserts False.  
- ***test_result():***  
This method is used to test result() function in project2.py. The input file is first read, cleaned, and passed as one of the parameters to the result() function. The result of this is stored in a variable called result. This method test_result() will assert True when the result variable is not None. Else this method will assert False.  
  

***pytest.in***  
This file contains the following code:  
[pytest]  
addopts = -p no:warnings  
This has been added so as to remove the warnings in my pytest.  

**Bugs:**  
- For few wierd combinations,like oil and milk, I am getting closest meals as empty set.  
-  Few scores values of the closest meals are above 1.  

*For running this project, the RAM size has been increased to 8GB.*  

**References:**  
- https://medium.com/nerd-for-tech/predicting-food-cuisine-using-natural-language-processing-and-machine-learning-in-python-a00c859a8ac7  
- https://stackoverflow.com/questions/50916422/python-typeerror-object-of-type-int64-is-not-json-serializable  
