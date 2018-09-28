import requests, time, base64, sys, json

#('-----------------------------------------------------')
#('-------- PureCloud Python Aggregate Report ----------')
#('-----------------------------------------------------')

#Abrir y guardar el Json de configuracion
with open('configuration.edges.json') as config_file:
    config = json.load(config_file)

# Formato fecha y guardo variable de fecha y hora actual
format = "%Y-%m-%dT%H:%M:%S"
tiempo = time


def generarToken():
    # Prepare post token request
    client_auth = config['client_id'] + ":" + config['client_secret']

    tokenHeader = {
        'Authorization': 'Basic ' + base64.b64encode(client_auth.encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    tokenBody = {'grant_type': 'client_credentials'}

    token = requests.post('https://login.' + config['environment'] + '/token', data=tokenBody, headers=tokenHeader)

    # Check response
    if token.status_code == 200:
        print('Token success! ' + str(token.status_code) + ' ' + str(token.reason) + ' ' + tiempo.strftime(format))
    else:
        print('Error al generar token ' + str(token.status_code) + ' ' + str(token.reason) + ' ' + tiempo.strftime(format))
        sys.exit()

    # Get JSON response body
    tokenJson = token.json()
    return tokenJson

def startUp( ):
    #MAIN: Ya se abrio y guardo el Json de configuracion
    #MAIN: Ya se formateo fecha y guardo variable de fecha y hora actual

    #Generar el token
    tokenHeader = generarToken()
    #Headers
    requestHeaders = {
        'Content-Type': 'application/json',
        'Authorization': tokenHeader['token_type'] + ' ' + tokenHeader['access_token']
    }

    resp = requests.get('https://api.mypurecloud.com/api/v2/telephony/providers/edges', headers=requestHeaders)

    if int(resp.status_code) == 200:
        print('Sucesss! ' + str(resp.status_code) + ' ' + str(resp.reason) + ' ' + tiempo.strftime(format))
    else:
        error_msg = 'Error: ' + str(resp.status_code) + ' ' + str(resp.reason) + ' ' + tiempo.strftime(format)
        print(error_msg)
        return error_msg

    print ( resp.json() )


def main():
    return startUp()

if __name__ == "__main__":
    startUp()
