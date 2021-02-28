import os
import string
from collections import defaultdict
from ruamel import yaml as yaml

IN_PATH = "../data/lookup_tables"
OUT_PATH = "templates/entities_auto.chatette"


class Entity2Chattete:
    """
    Reads all files from lookup table and converts them into entity list for chatette usage
    """
    def __init__(self):
        pass

    def _get_file_list(self):
        files_details = []
        for root, subFolder, files in os.walk(IN_PATH):
            for item in files:
                # TODO: remove this constrain of "email"
                if item.endswith(".yml") and "email" not in item:
                    fileNamePath = str(os.path.join(root,item))
                    dir_name = os.path.dirname(fileNamePath)
                    higher_entity = ""
                    if dir_name != IN_PATH:
                        higher_entity = dir_name.split('/')[-1]
                    entity_name = fileNamePath.split('/')[-1].split(".")[0]
                    files_details.append((higher_entity, entity_name, fileNamePath))
        return files_details

    def _get_entity(self, filepath):
        with open(filepath) as stream:
            content = stream.read()
        try:
            # | is not supported in YAML spec and hence, needs to be replaced
            # RASA reason: https://rasa.com/docs/rasa/training-data-format/#example
            yaml_dict = yaml.safe_load(content.replace("|", ""))
        except yaml.YAMLError as exc:
            print(exc)
            yaml_dict = {}
        #yaml_dict = read_yaml_file(filepath)
        if yaml_dict:
            nlu_list = yaml_dict['nlu']
            for nlu_data in nlu_list:
                lookup_name = nlu_data['lookup']
                entities = nlu_data['examples']
            return lookup_name, entities

    def _escape_last_penctuation(self, in_str):
        """
        Rasa doesn't expects any punctuations in the end of the training data, including whitespaces;
        if entity happens to be in the end, then it will create problems; hence, we require this method to remove
        last char is removed
        """
        new_str = in_str
        if in_str[-1] in string.punctuation:
            new_str = in_str[:-1]
        return new_str

    def _escape_characters(self, in_str):
        escape_list = ["/", ";", "[", "]", "{", "}", "~", "@", "%", "|", "?", "#", "$", "&"]
        new_str = in_str
        for char in escape_list:
            new_str = new_str.replace(char, "{}{}".format("\\", char))
        return new_str

    def _write(self, original_entity_map):
        out = open(OUT_PATH, "w")
        for entity_name, entity_dict in original_entity_map.items():
            entities = entity_dict["entities"]
            lookup_name = entity_dict["lookup_name"]
            template_str = "@[{}]\n".format(entity_name)
            for ent in entities:
                ent_str = self._escape_characters(str(ent).strip())
                #template_str = "{}\t\\[{}\\]({})\n".format(template_str, str(ent).strip(), lookup_name)
                template_str = "{}\t\\[{}\\]\n".format(template_str, ent_str, lookup_name)
            out.write("{}\n".format(template_str))
        out.close()

    def gen_entity_template(self):
        files_details = self._get_file_list()
        original_entity_map = defaultdict()
        entity_map = defaultdict()
        for entity_file in files_details:
            parent_entity = entity_file[0]
            entity = entity_file[1]
            entity_filename = entity_file[2]
            entity_name = "{}{}".format(parent_entity[0].upper()+parent_entity[1:], entity[0].upper()+entity[1:]) if parent_entity else "{}".format(entity[0].upper()+entity[1:])
            lookup_name, entities = self._get_entity(entity_filename)
            original_entity_map[entity_name] = {"entities": entities, "lookup_name": lookup_name}
        self._write(original_entity_map)


def main():
    entity2chattete = Entity2Chattete()
    entity2chattete.gen_entity_template()


if __name__ == '__main__':
    main()
