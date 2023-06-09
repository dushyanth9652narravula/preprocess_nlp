from preprocess_nlp import utils 

__version__ = '0.0.3'

def get_wordcounts(x):

	return utils._get_wordcounts(x)

def get_charcounts(x):

	return utils._get_charcounts(x)

def get_avg_wordlength(x):

	return utils._get_avg_wordlength(x)

def get_stopwords_counts(x):

	return utils._get_stopwords_counts(x)

def get_hashtag_counts(x):

	return utils._get_hashtag_counts(x)

def get_mention_counts(x):

	return utils._get_mention_counts(x)

def get_digit_counts(x):

	return utils._get_digit_counts(x)

def get_uppercase_counts(x):

	return utils._get_uppercase_counts(x)

def cont_to_exp(x):

	return utils._cont_to_exp(x)

def get_emails(x):

	return utils._get_emails(x)

def remove_emails(x):
	
	return utils._remove_emails(x) 

def get_urls(x):

	return utils._get_urls(x)

def remove_rt(x):

	return utils._remove_rt(x)

def remove_special_chars(x):

	return utils._remove_special_chars(x)


def remove_html_tags(x):

	return utils._remove_html_tags(x)

def remove_accented_chars(x):

	return utils._remove_accented_chars(x)

def remove_stopwords(x):

	return utils._remove_stopwords(x)

def make_base(x):

	return utils._make_base(x)

def get_unique_words(df,col):

	return utils._get_unique_words(df,col)

def remove_common_words(x,freq_comm,n=20):

	return utils._remove_common_words(x,freq_comm,n)

def remove_rare_words(x,n=20):

	return utils._remove_rare_words(x,freq_comm,n)

def spelling_correction(x):

	return utils._spelling_correction(x)