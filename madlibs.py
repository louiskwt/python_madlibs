import anime_quotes

# String concatenation

verb1 = input("Enter a verb: ")

verb2 = input('Ener another verb: ')

adj = input('Enter an adjective: ')

noun = input("Enter a noun: ")

quotes = anime_quotes.quotes

quote = anime_quotes.get_random_quote(quotes)


print(quote.format(verb1=verb1, verb2=verb2, adjective=adj, noun=noun))
