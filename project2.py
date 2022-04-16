from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
import argparse
from sklearn.neighbors import KNeighborsClassifier
import json
import numpy as np
import numpyencoder
from sklearn.metrics.pairwise import cosine_similarity
from numpyencoder import NumpyEncoder
import warnings
warnings.filterwarnings("ignore")

inpdata = "yummly.json"

def read(inpdata):
    input_data=pd.read_json(inpdata)
    return input_data


def clean_data(input_data):
    input_data['ingredients'] = [','.join(map(str, l)) for l in input_data['ingredients']]
    return input_data

def result(ingredients,N,input_data):
    x = input_data.ingredients
    y = input_data.cuisine
    x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.3, random_state = 42)
    knn = Pipeline([('vect', CountVectorizer()),
                    ('tfidf', TfidfTransformer()),
                    ('clf', KNeighborsClassifier(n_neighbors=20)),
                     ])
    knn.fit(x_train, y_train)
    # Training the model
    y_pred1 = knn.predict(x_test) # Predicting on test data
    # Calculating Accuracy
    #print(f"Accuracy is : {accuracy_score(y_pred1,y_test)}")
    ver=knn["vect"].transform(ingredients)
    ver=knn["tfidf"].transform(ver)
    ver=ver.todense()
    cs = []
    sc = []
    dist,index=knn["clf"].kneighbors(ver)
    ing_df=pd.DataFrame()
    ing_df["id"]=index[0]
    ing_df["cuisine"]=y_train.iloc[index[0]].tolist()
    ing_df["dist"]=dist[0]
    #print(dist[0])
    ing_df_subset=ing_df.loc[ing_df.cuisine==ing_df.cuisine[0]]
    #print(ing_df_subset)
    result={"Cuisine":ing_df_subset.cuisine.iloc[0],"score":round(ing_df_subset.dist.iloc[0],3)
            }
    result["closest"]=[]
    if int(N)>ing_df_subset.shape[0]:
        for i in range(1,ing_df_subset.shape[0]):
            x={}
            x["id"]=ing_df_subset.id.iloc[i]
            x["score"]=round(ing_df_subset.dist.iloc[i],3)
            #x["score"]=cs[i]
            result["closest"].append(x)
    else:
        for j in range(1,int(N)+1):
            x={}
            x["id"]=ing_df_subset.id.iloc[j]
            x["score"]=round(ing_df_subset.dist.iloc[j],3)
            #x["score"]=cs[i]
            result["closest"].append(x)            
    #print(result['closest'])
    temp=json.dumps(result,indent=4,sort_keys=False,
                          separators=(', ', ': '),ensure_ascii=False,cls=NumpyEncoder)
    print(temp)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True,help="Number of closest meals")
    parser.add_argument("--ingredient", type=str, required=True,help="Ingredients",action = 'append')
    args = parser.parse_args()
    if args.ingredient and args.N:
        input_data = read(inpdata)
        ingredients=",".join(args.ingredient) 
        #print(ingredients)
        input_data=clean_data(input_data)
        result([ingredients],args.N,input_data)
