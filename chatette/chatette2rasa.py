import json
from collections import defaultdict


class GenTrainDataset:
    """
    Generates the training dataset based on Chatitio templates
    """
    _format = "rasa"

    def __init__(self, template_path, chatette_path, intents_path):
        self._template_path = template_path
        self._chatette_path = chatette_path
        self._intents_path = intents_path

    def _get_intents_map(self, chattete_dict):
        intents_dict = defaultdict(list)
        data = chattete_dict['rasa_nlu_data']['common_examples']
        for intent_example in data:
            intents_dict[intent_example['intent']].append(intent_example['text'])
        return intents_dict

    def _write_to_yaml(self):
        with open(self._chatette_path) as f:
          data = json.load(f)
        intents_data_dict = self._get_intents_map(data)
        for intent, intent_data in intents_data_dict.items():
            first_line = "version: \"2.0\"\nnlu:\n- intent: {}\n  examples: |\n".format(intent)
            with open("{}/{}.yml".format(self._intents_path, intent), 'w') as f:
                f.write(first_line)
                for i in intent_data:
                    if not i: continue
                    f.write('   - {}\n'.format(i))

    def write_intents(self):
        self._write_to_yaml()


def main():
    template_path = "templates"
    train_chatette_path = "chatette_output/train/output.json"
    test_chatette_path = "chatette_output/test/output.json"
    nlu_intents_path = "../data/nlu"
    gen_train = GenTrainDataset(template_path, train_chatette_path, nlu_intents_path)
    gen_train.write_intents()
    nlu_test_intents_path = "../tests/nlu_auto"
    gen_test = GenTrainDataset(template_path, test_chatette_path, nlu_test_intents_path)
    gen_test.write_intents()


if __name__ == '__main__':
    main()
