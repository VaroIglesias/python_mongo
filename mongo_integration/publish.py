import gridfs


def publish_metadata(collection, metadata):

    """
    :param collection: Collection, instance of the collection where metadata will be stored
    :param metadata: dict [], document to publish
    :return: ObjectID, _id of the inserted document
    """

    metadataID = collection.insert_one(metadata)
    return metadataID.inserted_id


def publish_document(database, namespace, document, filename):
    """
    :param database: Database, instance of the database to be used
    :param namespace: str, namespace (collection) where the file will be stored
    :param document: file (_io.TextIOWrapper), loaded document to be stored
    :param filename: str, name of the file, used to search for specific files
    :return: ObjectID, _id of the published document
    """

    fs = gridfs.GridFS(database, namespace)
    documentID = fs.put(document, filename=filename)
    return documentID
