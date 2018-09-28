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
	  "client_id": "a3303c1d-cb8e-4c7c-ab30-..........",
	  "client_secret": "UGtBIZhan1hVyaercPTKYUz2FICmw........",
	  "environment": "mypurecloud.com",
	  "api": "api.mypurecloud.com"
	}

  The instance of a listening app is deployed locally as:

		python agentStatus.py 8446

	Or you can use the hosted version in :

		http://bbvaarmaster.arg.igrupobbva:8446/

  invoking a sample "poc@bbva.com" agente e-mail , to check if it is available:

	GET http://bbvaarmaster.arg.igrupobbva:8446/agentStatus/poc@bbva.com/

  or locally :
	
	GET http://localhost:8446/agentStatus/poc@bbva.com/

Result
------
	<agentStatus.retrieveAgentStatus instance at 0x7f18a457c200>
	poc@bbva.com/
	Token success! 200 OK 2018-09-18T12:12:03
	Users sucesss! 200 OK 2018-09-18T12:12:04
	Agente POC BBVA
	Users status sucesss! 200 OK 2018-09-18T12:12:04
	1
	Users status sucesss! 200 OK 2018-09-18T12:12:04 status_code=1
	127.0.0.1:56408 - - [18/Sep/2018 12:12:04] "HTTP/1.1 GET /agentStatus/poc@bbva.com/" - 200 OK

Install as a service in systemd
-------------------------------

	- Copy the "purecloudapi.service" to the systemd script folder, as "/etc/systemd/system/purecloudapi.service"
	- Enable it, "systemctl enable purecloudapi.service"
	- Start the service, "systemctl start purecloudapi.service" : its bash script is installed in "/usr/share/nginx/html/api" as default in Centos7 with Nginx.

	

