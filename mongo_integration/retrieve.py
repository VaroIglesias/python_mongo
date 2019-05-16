import gridfs


def find_metadata(collection, query):
    """

    :param collection: Collection, instance of the collection where the metadata is stored
    :param query: dict[], dictionary used to query the collection
    :return: pymongo.cursor.Cursor, iterable object with the retrieved metadata documents
    """

    metadata = collection.find(query)
    return metadata


def find_document(database, namespace, filename):
    """

    :param database: Database, instance of the database to be used
    :param namespace: str, name of the namespace (collection) where the files are stored
    :param filename: str, name of the file to be retrieved
    :return: bytes, retrieved document
    """

    fs = gridfs.GridFS(database, namespace)
    collection = database[namespace]
    f_id = collection.files.find_one({"filename": filename})['_id']
    document = fs.get(f_id).read()
    return document

