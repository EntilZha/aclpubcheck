from setuptools import setup

install_requires = [
	"tqdm",
	"termcolor",
	"pandas",
	"pdfplumber",
	"rebiber",
	"pybtex",
	"pylatexenc",
	"Unidecode",
	"tsv"
]


setup(
	name="aclpubcheck",
	install_requires=install_requires,
	version="0.2",
	scripts=[]
)
