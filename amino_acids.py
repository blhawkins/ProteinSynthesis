#The objective of this program is to scrape relevant amino acid information from Wikipedia's "Table of Standard Amino Acid Abbreviations and Properties".
#Target URL: https://en.wikipedia.org/wiki/Amino_acid

#Import dependencies
import pandas as pd

#Define the target URL
url = 'https://en.wikipedia.org/wiki/Amino_acid'

#Use Pandas to pull the desired amino acid table from the website's HTML code
amino_acid_df = pd.read_html(url)[1]

#Remove the extra header row from amino_acid_df
amino_acid_df.columns = amino_acid_df.columns.droplevel(0)

#Remove unneeded columns from amino_acid_df
amino_acid_df.drop(columns = ['Wavelength, λmax (nm)', 'Coefficient, ε (mM−1·cm−1)', 'Standard genetic coding, IUPAC notation'], inplace = True)

#Rename columns of amino_acid_df
amino_acid_df.columns = ['name', 'three_letter_abbr', 'one_letter_abbr', 'class', 'polarity', 'charge', 'hydropathy', 'molecular_mass', 'abundance']

#Convert amino_acid_df to a Python dictionary object
amino_acid_dict = amino_acid_df.to_dict('records')

#Correct a formatting issue in one of the entries
amino_acid_dict[8]['charge'] = 'Primarily Neutral'