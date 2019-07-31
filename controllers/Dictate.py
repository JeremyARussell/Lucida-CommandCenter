from flask import *
from Database import database
from AccessManagement import login_required
from ThriftClient import thrift_client
from Utilities import log, check_image_extension
import Config
import os
import json

dictate = Blueprint('dictate', __name__, template_folder='templates')

@login_required
def generic_dictate_route():
	options = {}
	if os.environ.get('ASR_ADDR_PORT'):
		options['asr_addr_port'] = os.environ.get('ASR_ADDR_PORT')
	else:
		options['asr_addr_port'] = 'ws://localhost:' + port_dic["cmd_port"]

	return options

@dictate.route('/dictate', methods=['GET', 'POST'])
@login_required
def dictate_route():
	options = {}
	if os.environ.get('ASR_ADDR_PORT'):
		options['asr_addr_port'] = os.environ.get('ASR_ADDR_PORT')
	else:
		options['asr_addr_port'] = 'ws://localhost:' + port_dic["cmd_port"]
	if request.method == 'POST':
		options = generic_dictate_route()
	return render_template('dictate.html', **options)

@dictate.route('/api/dictate', methods=['POST'])
def api_dictate_route():
	session['username'] = database.get_username(request.form['interface'], request.form['username'])
	if session['username'] == None:
		abort (403)

	session['logged_in'] = True
	print 'Logged in as: ', session['username']

	options = generic_dictate_route(request.form, request.files['file'] if 'file' in request.files else None)

	if 'errno' in options:
		return json.dumps(options), options['errno']
	return json.dumps(options), 200
