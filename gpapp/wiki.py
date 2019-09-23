#! /usr/bin/env python3
# coding: utf-8

import wikipedia


class Wiki:

    # Get the question as an attribute
    def __init__(self, place):
        wikipedia.set_lang("fr")
        self.place = " " + place

    # Return the first 2 sentence of wiki
    def wiki_quote(self):
        search = wikipedia.search(self.place)
        if search:
            title_page = search[0]
            text = wikipedia.summary(title_page, sentences=2)
            result = ("Hum ... Hum ... Eureka : " + text)

        else:
            result = ("Je t'affiche ce qui me parait le plus proche "
                      "mais nous savons que ce n'est pas ce que tu cherchais. "
                      "Ou alors je t'affiche ma ville de naissance... Hum ..."

                      )
        return result

