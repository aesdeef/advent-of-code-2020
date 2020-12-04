from document import Document


def parse_line(line):
    """
    Parses the given line and returns a dict with given keys and values.
    A line that only contains whitespace will return an empty dict.
    """
    return dict(element.split(":") for element in line.split())


def parse_input():
    """
    Parses the puzzle input and returns a list of Documents
    """
    documents = []
    with open("input_04.txt", "r") as f:
        current_document = {}
        for line in f:
            if partial_document := parse_line(line):
                current_document.update(partial_document)
            else:
                documents.append(Document(current_document))
                current_document = {}
        documents.append(Document(current_document))
    return documents


def count_valid_documents(documents, validate_fields=False):
    """
    Counts the number of valid documents
    """
    count = 0
    for document in documents:
        if document.has_all_fields() and (
            not validate_fields or document.all_fields_valid()
        ):
            count += 1
    return count


if __name__ == "__main__":
    documents = parse_input()
    print(count_valid_documents(documents))
    print(count_valid_documents(documents, validate_fields=True))
