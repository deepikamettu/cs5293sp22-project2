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
  
Running the project with the above given command-line argument will take the list of the ingredients provided by the user and the number  N and produces an output with a prediction of the type of cuisine and displays the top-N closest foods – returns the IDs of the dishes.  
  
The project2.py contains the following functions:  
- ***read(inpdata):***  
In this function, the data file “yummly.json” is read and stored in a variable called input_data which is further used in the program.  
- ***clean_data(input_data):***  
In this function, the input_data returned from the read() function is taken and cleaned. Meaning, in this case, the ingredients in the input file are converted from a list to a string so that it will be easy for us to proceed to further steps of training the model.  
- *result(ingredients,N,input_data):*
In this function, I am initializing the columns "ingredients" and "cuisine" to variables X and y for which I am performing train_test_split().For train_test_split(), I am using 70% of data as train data and rest 30% as test data.Then I am using a classifier "KNN" for which I am declaring a pipeline which consists of CountVectorizer and TfidfTransformer to convert the entire texts into numeric format.Then I am using a function called todense() to convert it to a matrix form.I am using a function called .kneighbours() to find out the nearest possible distance's and index's.I am declaring a dataFrame and appending all the Id's,Cuisine and Distances to that DataFrame with the index 0.Then I am initializing a dictonary and using it for the appending of values cuisine along with its score.Then for the closest of Id's I am checking a condition for user given N value, for which I am appending ID's along with their Scores.I am converting the appended dictonary to a JSON format by using the function json.dumps() and then printing it to the console in the following format:  
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

I have increased the RAM size in VM to 8GB, as am getting killed with my previous instance size.  

**References:**  
- https://medium.com/nerd-for-tech/predicting-food-cuisine-using-natural-language-processing-and-machine-learning-in-python-a00c859a8ac7  
- https://stackoverflow.com/questions/50916422/python-typeerror-object-of-type-int64-is-not-json-serializable  
