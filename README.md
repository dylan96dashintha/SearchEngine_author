# IR_Project-Authors_Search_Engine
Author Search Engine using ElasticSearch and Python for IR Project(CS4642)

## Getting Start
### Settign up the Environment
- Download and Install the ElasticSearch
- Install the ICU_Tokenizer plugin on the ElasticSearch
- Install the python3 with pip3
- git clone https://github.com/dylan96dashintha/SearchEngine_authorList.git
- cd Search_eng_asg
- python -m venv env
- env/Scripts/activate
- pip install -r requirements.txt  

### Running the Project
1. First start the ElasticSearch locally on port 9200.
2. Then run index_creation.py file to create the index and insert data.
3. Next run the main.py to start the search engine
4. Then visit http://localhost:5000/ for see the user interface.
5. Finally add your search query in the search box for searching

### File structure
- data - Folder contains scraped data with python code used for format the json
- templates - Folder contains Html user interface of the search engine
- documents - Folder contains project proposal & project report
- images - Folder contains diagrams used in README.md
- index_creation.py - Python code for index creating and data inserting
- search_function.py - Python code use for process search query
- advanced_queries.py - Elastic Search queries
- requirements.txt - python requirements

### Details of Author Data
formatted_authors.json file contains 103 author records with following data
1. author_name - name of the author in Sinhala
2. author_name_english - name of the author in  English
3. date_of_birth - Birth date of the author
4. birth_place - Birth place of the author in Sinhala
5. birth_place_english - Birth place of the author in English
6. school - Schools attended by the author
7. book_list - List of books written by the author
8. about_author - paragraph about the author
9. language - Language wriiten by the author
10. category - Book categories written by the author

### Basic Functionalities
- It supports searching by the author_name, author_name_english, date_of_birth, birth_place, birth_place_english,
school, book_list,about_author, language, category

  eg: ගුණදාස අමරසේකර, මිරිඟුව ඇල්ලීම,නවකතා
 
 - Search Engine can identify synonyms related to specific fields like රචකයා(author), ලියපු(author), උපන්ගම(place of birth)
 and search based on the identified fields
 
    eg: මාර්ටින් වික්‍රමසිංහ රචකයා, උපන්ගම කොග්ගල
 
 - Search Engine supports both Sinhala and English Language queries (Bilingual Support only for the seaching by author name and authors birthplace)
 
    eg: ගුණදාස අමරසේකර රචකයා, author gunadasa amarasekara
 
 - Search Engine also support to the query phrases which is a mix of Sinhala and English languages
 
    eg: Gunadasa රචකයා, Martin වික්‍රමසිංහ, author වික්‍රමසිංහ
 
 ### Following figure shows the example search result of the UI.
 
 
![BASE ui2](https://user-images.githubusercontent.com/47697151/142927562-473eb5b1-37c9-4e9a-9b97-0d99e7bf89c6.PNG)

### Project Architecture
Following figure shows how the search engine works through teh flask server

![BASE archi](https://user-images.githubusercontent.com/47697151/142927743-d76d5f5d-b689-4a94-b8fe-5cb7985f44ac.PNG)

### Indexing and Query techniques