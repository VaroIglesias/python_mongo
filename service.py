from mongo_integration.mongo_manager import MongoManager
from core.managed import register_managed
from core.reader import read_yaml_file


def main():
    config = read_yaml_file('config.yml')

    mongo_resource = MongoManager(config["mongodb"])
    register_managed(mongo_resource)

    print("starting...")
    query = {"hola": "jeje"}
    my_met = mongo_resource.retrieve_metadata(query)
    for x in my_met:
        print(x)

    mydict = {"hola": "jeje"}
    published = mongo_resource.store_metadata(mydict)
    print("published metadata: ", published)

    with open(r'fz7U6Nve.jpg', 'rb') as document:
        my_publication = mongo_resource.store_document(document, document.name)

    print('published document id: ', my_publication)

    retrieved = mongo_resource.retrieve_document(document.name)

    print("retrieved document: ", retrieved)


if __name__ == "__main__":
    main()

