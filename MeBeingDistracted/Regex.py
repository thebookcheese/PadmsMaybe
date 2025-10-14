import re

def multiple_replacements(text):
    ## Define replacement dictionary
    replacements = {
        r'\bLiberal\b': 'Communism',
        r'\bdemocracies\b': 'utopias',
        r'\bleast\b': 'Regular Expression',
        r'\bin\b' : 'out',
        r'\bsince\b': 'before',
        r'[a]' : 'divide',
        r'[e]' : 'multiply',
        r'[i]' : 'add',
        r'[u]' : 'subtract',
        r'[h]' : 'solve',
        r'[j]' : 'for',
        r'[b]' : 'x',
        r'[c]' : 'truncate',
        r'[s]' : 'round',
        r'a' : 'factorise',
        r'[w]' : 'plot',
        r'[q]' : 'percentage',
        r'[o]' : 'expand',
        r'phot' : ' find '
    }

    ## Apply replacements twice
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    return text


#The search() function returns a Match object:

txt = """Liberal democracies are now the least common regime type in
the world after gradually decreasing in numbers since 2009. The last
time there were only 29 liberal democracies in the world was in 1990
– at the end of the Cold War.

The gradual rise in the number of electoral democracies reflects
that countries who used to be liberal democracies have suffered from backsliding and have lost some of the liberal features.
Some recent examples include Botswana, Cyprus, Greece, Israel, and
Slovenia.

The two sides of the same coin show that the wave of autocratization affects both democracies and autocracies. Over the last decade,
the quality of democracy in democracies has declined, while the
severity of authoritarianism in autocracies has increased – a growth
in the “worst of both worlds.”"""
x = multiple_replacements(txt)
delimiter = "" # Define a delimiter
if x:
	join_str = delimiter.join(x)
	print(join_str)

with open('Regex.txt', 'w') as f:
	f.write(join_str)