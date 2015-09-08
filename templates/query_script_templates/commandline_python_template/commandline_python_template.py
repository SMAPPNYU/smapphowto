import os
import argparse
from smappPy.smapp_logging import logging
logger = logging.getLogger(__name__)

class SMaPPError(Exception):
	pass

if __name__ == '__main__':
	logger.info(__name__)
	parser = argparse.ArgumentParser()
	parser.add_argument('-s'
						,'--serveraddress'
						,dest='serveraddress'
						,default='smapp.politics.fas.nyu.edu'
						,help='[smapp.politics.fas.nyu.edu]'
					)
	parser.add_argument('-p'
						,'--port'
						,dest='port'
						,default=27011
						,type=int
						,help='[27011]'
					)
	parser.add_argument('-u'
						,'--dbuser'
						,dest='dbuser'
						,default='smapp_readOnly'
						,help='[smapp_readOnly]'
					)
	parser.add_argument('-w'
						,'--dbpassword'
						,dest='dbpassword'
					)
	parser.add_argument('-db'
						,'--dbname'
						,dest='dbname'
						,help='Database name to get data from. Required.'
					)
	parser.add_argument('-i'
						,'--input'
						,dest='input'
						,default='input/input.csv'
						,help='Path to your keywords file that contains the keywords you want to filter for.'
					)
	parser.add_argument('-o'
						,'--output-directory'
						,default='.'
						,help='Output folder for csvs [.]'
					)
