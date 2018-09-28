import requests, time, base64, sys, json

#('-----------------------------------------------------')
#('-------- PureCloud Python Aggregate Report ----------')
#('-----------------------------------------------------')

#Abrir y guardar el Json de configuracion
with open('configuration.json') as config_file:
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

def startUp( searchUName ):
    #MAIN: Ya se abrio y guardo el Json de configuracion
    #MAIN: Ya se formateo fecha y guardo variable de fecha y hora actual

    #Generar el token
    tokenHeader = generarToken()
    #Headers
    requestHeaders = {
        'Content-Type': 'application/json',
        'Authorization': tokenHeader['token_type'] + ' ' + tokenHeader['access_token']
    }

    users = requests.get('https://api.' + config['environment'] + '/api/v2/users?pageSize=100', headers=requestHeaders)

    if int(users.status_code) == 200:
        print('Users sucesss! ' + str(users.status_code) + ' ' + str(users.reason) + ' ' + tiempo.strftime(format))
    else:
        error_msg = 'Error al obtener usuarios ' + str(users.status_code) + ' ' + str(users.reason) + ' ' + tiempo.strftime(format)
        print(error_msg)
        return error_msg

    #Logg DEBUG-level: print full list of entities
    #print ( users.json()['entities'] )

    #Chequeo de parametro presente, sino se asume argumento de linea de comando
    if (not searchUName):
        searchUName = sys.argv[1]

    usuario = {}
    for entity in users.json()['entities']:
        #Se busca el username (el correo) en el listado de usuarios, si se quiere buscar por nombre de usuario cambiar el if entity['username'] por if entity['name']
        if entity['username'] == str( searchUName ):
            usuario['id'] = entity['id']
            usuario['name'] = entity['name']
            usuario['username'] = entity['username']
            usuario['state'] = entity['state']
            print(usuario['name'])

    if usuario != {}:
        usersStatus = requests.get('https://api.' + config['environment'] + '/api/v2/users/' + usuario['id'] + '/routingstatus', headers=requestHeaders)
        if int(usersStatus.status_code) == 200:
            success_msg = 'Users status sucesss! ' + str(usersStatus.status_code) + ' ' + str(usersStatus.reason) + ' ' + tiempo.strftime(format)
            print(success_msg)
        else:
            error_msg = 'Error al obtener usuarios ' + str(usersStatus.status_code) + ' ' + str(usersStatus.reason) + ' ' + tiempo.strftime(format)
            print(error_msg)
            return error_msg

        if usersStatus.json()['status'] == 'IDLE':
            # Existe el usuario y esta disponible para atender interacciones
            status_code = '2'
            print(status_code)
            return success_msg + ' status_code=' + status_code
        else:
            # Existe el usuario pero no esta disponible
            status_code = '1'
            print(status_code)
            return success_msg + ' status_code=' + status_code
    else:
        # El usuario no existe
        status_code = '0'
        error_msg = 'Error, el usuario no existe, ' + ' status_code=' + status_code
        print(error_msg)
        return error_msg

def main( searchUName ):
    return startUp( searchUName )

if __name__ == "__main__":
    startUp()
