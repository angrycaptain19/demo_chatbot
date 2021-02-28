## Guide lines to write templates

1. All aliases should be introduced in aliases.chatette file
2. All manually generated entities should be introduced in entities_manual.chatette
3. entities_auto.chatette is generated using files under lookup_tables
4. Use common.chatette file to define rasa format entity. 
    Ex- to define \[Abhishek\](person), define entity "Abhishek" in entities_manual.chatette  
    ```
        @[Person]
            \[Abhishek\]
    ```
    and then define "(person)" in aliases.chatette as 
    ```
    ~[PersonEntityName]
        (person)
    ```
TODO: Currently, output is written inside chatette folder (in intents folder). 
Ideally, it should be directly written to data folder, with each intent having 
its own file.

## To Generate dataset

1. Update template.chatette file
2. Generate: bash execute.sh 