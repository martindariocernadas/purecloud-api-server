#('-------------------------------------------------------')
#('-------- PureCloud API via Web Python router ----------')
#('-------------------------------------------------------')

import web
import os
import helloWorld
import byeBye
import estadoAgente

#URLs supported and the mapping of corresponding methods
urls = (
    '/agentStatus/(.*)' , 'retrieveAgentStatus',
    '/hello/(.*)' , 'sayHello' ,
    '/byebye/(.*)', 'sayByebye',
    '/'     , 'index',
    '/(.*)' , 'index'
)

#WebApp instance : parametrized with supported URLS and global config (:8080)
app = web.application(urls, globals())

class retrieveAgentStatus:
    def GET(self, name):
        if not name:
            name = 'agentStatus'

        #Input parameters : self route and names
        print( self )
        print( name )

        #Split parameter after route "/agentStatus/"...
        mailbox = name.split("@")[0] # Gather mailbox from : "mailbox@domain.ext"
        domain = name.split("@")[-1] #  Gather domain from : "mailbox@domain.ext"
        ext = name.split(".")[-1] # Gather extension (".com", ".ie")
        slash = name.split("/")[0] # Gather final slash from "mailbox@domain.ext/"

        if( not slash ):
            userName = mailbox + '@' + domain
        else:
            userName = slash

        result = estadoAgente.main(userName)
        print(result)

        #Optional: Return status_code in header, upon result
        if( result ):
            status_code = result.split("status_code=")[-1] # Gather status_code
            web.header('Status-code', status_code)
            web.header('Result', result)

        web.header('Cache-control', 'no-cache')
        return result

class sayHello:
    def GET(self, name):
        if not name:
            name = 'sayHello'
        return helloWorld.salute()

class sayByebye:
    def GET(self, name):
        if not name:
            name = 'sayByebye'
        return byeBye.salute()

class index:
    def GET(self, name):
        if not name:
            name = 'Index'
        return 'Index'

#MAIN : entry point
if __name__ == "__main__":
    # web.py app run!
    app.run()
