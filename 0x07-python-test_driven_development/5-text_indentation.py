#!/usr/bin/python3
"""
5-text_indentation module containing:
text_indentation(text) reprints texts
"""
def text_indentation(text):
    """
    text_indentation('''Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
        Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
        Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
        Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
        Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
        rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
        stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
        cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
        beatiorem! Iam ruinas videres''')
    ...
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for index, i in enumerate(text):
        if i != " " or i == " " and text[index - 1] not in [".", ":", "?"]:
            print(i, end="")
        if i in [".", "?", ":"]:
            print("\n\n", end="")
    print("", end="")
