web.py : a Python framework for web pages and services
------------------------------------------------------

	Based upon the Reddit.com solution "web.py", using 'CherryPy/3.2.0 Server', a Minimalist Python Web Framework.

	Visit http://webpy.org/ for more information.
	Visit https://cherrypy.org/ for more information.


Getting Started
---------------

	web.py 0.39 is the latest released version of web.py. You can install it by running:

		- pip install web.py		
		- pip install --upgrade pip

	The above version only supports Python 2. If you looking for Python 3 support, try the experimental version.


Use cases : Purecloud App Token
-------------------------------

  Once PURECLOUD is configured with the corresponding Aplication Token , as stated:

	"PureCloudCalls - RemoteManager (AR) agent status" :

	{
	  "client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	  "client_secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	  "environment": "mypurecloud.com",
	  "api": "api.mypurecloud.com"
	}

  The instance of a listening app is deployed locally as:

		python agentStatus.py 8446

  invoking a sample "poc@mail.com" agente e-mail , to check if it is available:

	GET http://<server>:8446/agentStatus/poc@mail.com/

  or locally :
	
	GET http://localhost:8446/agentStatus/poc@mail.com/

Result
------
	<agentStatus.retrieveAgentStatus instance at 0x7f18a457c200>
	poc@mail.com/
	Token success! 200 OK 2099-09-18T12:12:03
	Users sucesss! 200 OK 2099-09-18T12:12:04
	Agent POC 
	Users status sucesss! 200 OK 2099-09-18T12:12:04
	1
	Users status sucesss! 200 OK 2099-09-18T12:12:04 status_code=1
	127.0.0.1:56408 - - [18/Sep/2099 12:12:04] "HTTP/1.1 GET /agentStatus/poc@mail.com/" - 200 OK


	

