def search(docs, str_to_find):
    docs_ans = []
    for d in docs:
        if d.get("text").__contains__(" " + str_to_find + " "):
            docs_ans.append(d.get("id"))

    return docs_ans

# docs = [
#     {"id": "doc1", "text": "I can't shoot straight unless I've had a pint!"},
#     {"id": "doc2", "text": "Don't shoot shoot shoot that thing at me."},
#     {"id": "doc3", "text": "I'm your shooter."}
# ]
#
# d = search(docs, "shoot")
# print(d)
