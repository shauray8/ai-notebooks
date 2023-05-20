## compile a meaningful readme here 

###ToDo
gather the dataset from different websites (initially a few datapoints)
create an embeddings model (maybe miniLM or something)
store all the embeddings in a vector database and 
write a function that compares the embeddings with the prompt 

--- 
Do I have to train a model for embeddings or similarity search or maybe I can leverage the use of FAISS and get this done. 

20 - import minilm as the embeddings model, create embeddings 
21 - gather dataset and store it into json
22 - gather more data, make a website, compile all of it together, deploy on google cloud run
23 - make an youtube video, write readme, document and comment well


All of this can be done pretty easily with chatgpt actually ! Only thing I have to do is to compile all of it together and get all the parsing done which would take most of the time !

---
Create a network <br>

main --> contains all of it with arguments (train, test) with train we first call "gather.py" then after the data is parsed it goes to "embedd.py" and gets converted to embeddings which then gets stored to a JSON file with all the embeddings and the URL ! and then its stored into FAISS for better similarity search. now when test is called it checks for similarity into the faiss database and then it searches for the same embedding in the json file to return the url !


<br><br>


Explain everything piece by piece and explain the possibility of using a normal charset for embeddings 

