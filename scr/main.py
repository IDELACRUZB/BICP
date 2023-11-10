from web_scraper import descargaReportes
from isdb import TablaValidacion2
import datetime
import json
import time
import subprocess


#Rango de fechas para descarga de Reportes
D0 =  datetime.date.today()
D_1 =  D0 + datetime.timedelta(days=-1)
inicio = str(D_1) #'2023-08-04'
fin = None#'2023-08-08'

user = 'E8237327'
password = '8p&5_!2xD1BT'

tablaValidacion = TablaValidacion2()
tablaValidacion.crearBD()
tablaValidacion.crearTabla()
tablaValidacion.truncateTable()

descarga = descargaReportes()
def logueo():
    descarga.login()
    descarga.inicioSesion(user, password)
    descarga.validaSesionActiva()
    hayCookie = descarga.validaSiExisteCookie()

    while hayCookie:
        descarga.gameOver()
        descarga.reiniciar()
        descarga.login()
        descarga.inicioSesion(user, password)
        descarga.validaSesionActiva()
        hayCookie = descarga.validaSiExisteCookie()
    else:
        pass

logueo()

contador_descargas = 1
#  ===== 1. Campaña 1259 =====
pathjson1259 = 'parametro_campana/bicp1259.json'
with open(pathjson1259, 'r') as json1259:
    parametros1259 = json.load(json1259)

for campana, parametros in parametros1259.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    campaignXpath = parametros["campaignXpath"]
    idCampaign = '1259'
    #desarga, renombra y reubica
    def descarga_1259():
        try:
            descarga.reporte1259(bpoXpath, campaignXpath, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_1259()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_1259()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)

# ===== 2. Campaña 401 =====
pathjson401 = 'parametro_campana/bicp401.json'
with open(pathjson401, 'r') as json401:
    parametros401 = json.load(json401)

for campana, parametros in parametros401.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    txtCampana = parametros["txtCampana"]
    campaignXpath = parametros["campaignXpath"]
    xpathAgentWorkgroup = parametros["xpathAgentWorkgroup"]
    #desarga, renombra y reubica
    idCampaign = '401'
    def descarga_401():
        try:
            descarga.reporte401(bpoXpath, txtCampana, campaignXpath, xpathAgentWorkgroup, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_401()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_401()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)

# ===== 3. Campaña 112 =====
pathjson112 = 'parametro_campana/bicp112.json'
with open(pathjson112, 'r') as json112:
    parametros112 = json.load(json112)

for campana, parametros in parametros112.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    #desarga, renombra y reubica
    idCampaign = '112'
    def descarga_112():
        try:
            descarga.reporte112(bpoXpath, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_112()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_112()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)

# ===== 4. Campaña 1261 =====
pathjson1261 = 'parametro_campana/bicp1261.json'
with open(pathjson1261, 'r') as json1261:
    parametros1261 = json.load(json1261)

for campana, subCampanas in parametros1261.items():
    nombreCampa = campana
    for subCampana, parametros in subCampanas.items():
        nameSubCampa = subCampana
        bpoXpath = parametros["bpoXpath"]
        activityXpath = parametros["activityXpath"]
        campaignXpath = parametros["campaignXpath"]
        textoC = parametros["textoC"]
        #desarga, renombra y reubica
        idCampaign = '1261'
        def descarga_1261():
            try:
                descarga.reporte1261(bpoXpath, activityXpath, campaignXpath, textoC, fechaInicial=inicio, fechaFinal=fin)
                nombreAsignado = nameSubCampa + f'_bicp_{idCampaign}_'
                nombreReporte = descarga.nombreReporte(nombreAsignado, True)
                partesSubC = nameSubCampa.split('_')
                if len(partesSubC) > 1:
                    destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}' + "_" + partesSubC[1]
                else:
                    destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
                descarga.renombrarReubicar(nombreReporte, destino)

                datos=[(contador_descargas, campana, nombreAsignado, 1)]
                tablaValidacion.agregarVariosDatos(datos)

            except Exception as e:
                nombreAsignado = nameSubCampa + f'_bicp_{idCampaign}_'
                datos=[(contador_descargas, campana, nombreAsignado, 0)]
                tablaValidacion.agregarVariosDatos(datos)
                pass
        
        descarga_1261()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]

        while descargo == 0:
            tablaValidacion.deleteTable(contador_descargas)

            descarga.reiniciar()
            logueo()

            descarga_1261()
            ultimoRegistro = tablaValidacion.leerDatos()
            descargo = ultimoRegistro[0][3]
        else:
            contador_descargas += 1
            pass
        print("descargo reporte ", idCampaign, " ", nombreCampa)         

# ===== 5. Campaña 90 =====
pathjson90 = 'parametro_campana/bicp90.json'
with open(pathjson90, 'r') as json90:
    parametros90 = json.load(json90)

for campana, parametros in parametros90.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    campaignXpath = parametros["campaignXpath"]
    xpathAgentWorkgroup = parametros["xpathAgentWorkgroup"]
    #desarga, renombra y reubica
    idCampaign = '90'
    def descarga_90():
        try:
            descarga.reporte90(campaignXpath, bpoXpath, xpathAgentWorkgroup, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_90()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_90()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)

# ===== 6. Campaña 43 =====
pathjson43 = 'parametro_campana/bicp43.json'
with open(pathjson43, 'r') as json43:
    parametros43 = json.load(json43)

for campana, parametros in parametros43.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    #desarga, renombra y reubica
    idCampaign = '43'
    def descarga_43():
        try:
            descarga.reporte43(bpoXpath, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_43()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_43()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)


# ===== 7. Campaña 26 =====
pathjson26 = 'parametro_campana/bicp26.json'
with open(pathjson26, 'r') as json26:
    parametros26 = json.load(json26)

for campana, parametros in parametros26.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    campaignXpath = parametros["campaignXpath"]
    #desarga, renombra y reubica
    idCampaign = '26'
    def descarga_26():
        try:
            descarga.reporte26(campaignXpath, bpoXpath, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_26()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_26()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)

# ===== 8. Campaña 194 =====
pathjson194 = 'parametro_campana/bicp194.json'
with open(pathjson194, 'r') as json194:
    parametros194 = json.load(json194)

for campana, parametros in parametros194.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    #desarga, renombra y reubica
    idCampaign = '194'
    def descarga_194():
        try:
            descarga.reporte194(bpoXpath, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_194()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_194()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)

# ===== 9. Campaña 192 =====
pathjson192 = 'parametro_campana/bicp192.json'
with open(pathjson192, 'r') as json192:
    parametros192 = json.load(json192)

for campana, parametros in parametros192.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    xpathAgentWorkgroup = parametros["xpathAgentWorkgroup"]
    #desarga, renombra y reubica
    idCampaign = '192'
    def descarga_192():
        try:
            descarga.reporte192(bpoXpath, xpathAgentWorkgroup, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_192()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_192()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)


# ===== 10. Campaña 1392 =====
pathjson1392 = 'parametro_campana/bicp1392.json'
with open(pathjson1392, 'r') as json1392:
    parametros1392 = json.load(json1392)

for campana, parametros in parametros1392.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    campaignXpath = parametros["campaignXpath"]
    #desarga, renombra y reubica
    idCampaign = '1392'
    def descarga_1392():
        try:
            descarga.reporte1392(campaignXpath, bpoXpath, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_1392()
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_1392()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)

# 11. Campaña 418
pathjson418 = 'parametro_campana/bicp418.json'
with open(pathjson418, 'r') as json418:
    parametros418 = json.load(json418)

for campana, parametros in parametros418.items():
    nombreCampa = campana
    bpoXpath = parametros["bpoXpath"]
    campaignXpath = parametros["campaignXpath"]
    xpathAgentWorkgroup = parametros["xpathAgentWorkgroup"]
    #desarga, renombra y reubica
    idCampaign = '418'
    def descarga_418():
        try:
            descarga.reporte418(campaignXpath, bpoXpath, xpathAgentWorkgroup, fechaInicial=inicio, fechaFinal=fin)
            nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
            nombreReporte = descarga.nombreReporte(nombreAsignado, True)
            destino = descarga.directoryPath + r'/carga/' + nombreCampa + rf'/bicp/{idCampaign}'
            descarga.renombrarReubicar(nombreReporte, destino)
            print(f'Descarga exitosa Reporte {idCampaign}, Campaña ', nombreCampa)

            datos=[(contador_descargas, campana, nombreAsignado, 1)]
            tablaValidacion.agregarVariosDatos(datos)

        except Exception as e:
            datos=[(contador_descargas, campana, nombreAsignado, 0)]
            tablaValidacion.agregarVariosDatos(datos)
            pass
    
    descarga_418()
    nombreAsignado = nombreCampa + f'_bicp_{idCampaign}_'
    ultimoRegistro = tablaValidacion.leerDatos()
    descargo = ultimoRegistro[0][3]

    while descargo == 0:
        tablaValidacion.deleteTable(contador_descargas)

        descarga.reiniciar()
        logueo()

        descarga_418()
        ultimoRegistro = tablaValidacion.leerDatos()
        descargo = ultimoRegistro[0][3]
    else:
        contador_descargas += 1
        pass
    print("descargo reporte ", idCampaign, " ", nombreCampa)


descarga.cerrarSesion()
descarga.gameOver()
print("Descarga exitosa de Reportes del ", inicio, " al ", fin )

# Paso 2: Carga la base de datos al servidor
subprocess.call(['python', './importador/controller.py'])
