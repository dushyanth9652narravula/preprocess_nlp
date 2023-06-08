import setuptools

with open('README.md','r') as file:

	long_desription = file.read()


setuptools.setup(

		name = 'preprocess_nlp', # This should be unique
		version = '0.0.3',
		author = 'N.Dushyanth Sai Chowdary',
		author_email = 'narravula.dushyanthsai@gmail.com',
		description = 'This is preprocessing package',
		long_desription = long_desription,
		long_description_content_type = 'text/markdown',
		packages = setuptools.find_packages(),
		classifiers = [
		'Programming Language  :: Python :: 3',
		'License :: OSI Aproved :: MIT License',
		'Operating System :: OS Independent' 
		],
		python_requires = '>=3.0'
	)