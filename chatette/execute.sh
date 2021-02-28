echo "Generating Entities from Rasa lookup tables..."
python entity2chatette.py
echo "Generating Chattete Output from Templates..."
# seeded with a number to ensure it generates same dataset everytime
python -m chatette -s 1 -a rasa templates/templates.chatette -f -o chatette_output
echo "Generating Intents from Chattete Output..."
python chatette2rasa.py
