from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from bs4 import BeautifulSoup
import requests
import pandas as pd
from medi.models import Medicamento
# Create your views here.


def get_medi(request):
   

    base_url = "https://www.medicamentosplm.com"
    url = base_url + "/Home/Medicamento/A/1"
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')

    #medicamentos
    enlaces_medi = soup.find_all('div',class_='nombrePrducto')

    for enlace in enlaces_medi:
        href_medi = enlace.find("a")
        try:
            medi = Medicamento.objects.get(medicamento=href_medi.text.strip())
            
            """ if (medi):
                print("si esta")
            else: 
                m = Medicamento(medicamento= href_medi.text.strip(), marca="0",sustancia="0",forma="0",composicion="0",indicaciones="0",propiedades="0",contraindicaciones="0",restricciones="0",reacciones="0",interacciones="0",hallazgos="0",precauciones="0",dosis="0",manifestaciones="0",presentacion="0")
                m.save() """
        except Medicamento.DoesNotExist:
            # entrará aqui cuando no exista ningun elemento
            # que coincida con la busqueda
            """ print(href_medi.text) """
            print(href_medi.get('href'))
            indicaciones="0"
            propiedades="0"
            contraindicaciones="0"
            restricciones="0"
            reacciones="0"
            interacciones="0"
            hallazgos="0"
            precauciones="0"
            dosis="0"
            manifestaciones="0"
            presentacion="0"

            url2 = base_url + href_medi.get('href')
            page2 = requests.get(url2)
            soup2 = BeautifulSoup(page2.content,'html.parser')
            info_principal = soup2.find("div",class_='info-ipp-pricipal')
            info = info_principal.find_all("p")
            marca = info[0].text.strip()
            sustancia = info[1].text.strip()
            forma = info[2].text.strip()
            info_composicion = soup2.find(id='rubro-0')
            composicion = info_composicion.find_all("p")
            all_info = soup2.find_all("div",class_="attribute-tracking")
            for header in all_info:
                href = header.get('href')
                rubro = href.replace('#','')
                info_header = header.find("a").text.strip()
                """ print(info_header.text.strip())
                print(rubro) """

                if info_header == 'INDICACIONES TERAPÉUTICAS':
                    print(rubro)
                    info_indicaciones = soup2.find(id=rubro)
                    indicaciones = info_indicaciones.find_all("p")
                    print(info_indicaciones)
                    print(indicaciones)
                elif info_header == 'PROPIEDADES FARMACÉUTICAS':
                    info_propiedades = soup2.find(id=rubro)
                    propiedades = info_propiedades.find_all("p")
                elif info_header == 'CONTRAINDICACIONES':
                    info_contra = soup2.find(id=rubro)
                    contraindicaciones = info_contra.find_all("p")
                elif info_header == 'RESTRICCIONES DE USO DURANTE EL EMBARAZO Y LA LACTANCIA':
                    info_restricciones = soup2.find(id=rubro)
                    restricciones = info_restricciones.find_all("p")
                elif info_header == 'REACCIONES ADVERSAS':
                    info_reacciones = soup2.find(id=rubro)
                    reacciones = info_reacciones.find_all("p")
                elif info_header == 'INTERACCIONES MEDICAMENTOSAS Y DE OTRO GÉNERO':
                    info_interacciones = soup2.find(id=rubro)
                    interacciones = info_interacciones.find_all("p")
                elif info_header == 'HALLAZGOS DE LABORATORIO CLÍNICO':
                    info_hallazgos = soup2.find(id=rubro)
                    hallazgos = info_hallazgos.find_all("p")
                elif info_header == 'PRECAUCIONES Y ADVERTENCIAS':
                    info_precauciones = soup2.find(id=rubro)
                    precauciones = info_precauciones.find_all("p")
                elif info_header == 'DOSIS Y VÍA DE ADMINISTRACIÓN':
                    info_dosis = soup2.find(id=rubro)
                    dosis = info_dosis.find_all("p")
                elif info_header == 'MANIFESTACIONES Y MANEJO DE LA SOBREDOSIFICACIÓN O INGESTA ACCIDENTAL':
                    info_manifestaciones = soup2.find(id=rubro)
                    manifestaciones = info_manifestaciones.find_all("p")
                elif info_header == 'PRESENTACIÓN':
                    info_presentacion = soup2.find(id=rubro)
                    presentacion = info_presentacion.find_all("p")
                else:
                    if(indicaciones == None):
                        indicaciones="0"
                    if(propiedades == None):
                        propiedades="0"
                    if(contraindicaciones == None):
                        contraindicaciones="0"
                    if(restricciones == None):
                        restricciones="0"
                    if(reacciones == None):
                        reacciones="0"
                    if(interacciones == None):
                        interacciones="0"
                    if(hallazgos == None):
                        hallazgos="0"
                    if(precauciones == None):
                        precauciones="0"
                    if(dosis == None):
                        dosis="0"
                    if(manifestaciones == None):
                        manifestaciones="0"
                    if(presentacion == None):
                        presentacion="0"

            """ info_indicaciones = soup2.find(id='rubro-1')
            indicaciones = info_indicaciones.find_all("p")
            info_propiedades = soup2.find(id='rubro-2')
            propiedades = info_propiedades.find_all("p") """
            """ print(all_info) """
            m = Medicamento(medicamento= href_medi.text.strip(), marca=marca,sustancia=sustancia,forma=forma,composicion=composicion,indicaciones=indicaciones,propiedades=propiedades,contraindicaciones=contraindicaciones,restricciones=restricciones,reacciones=reacciones,interacciones=interacciones,hallazgos=hallazgos,precauciones=precauciones,dosis=dosis,manifestaciones=manifestaciones,presentacion=presentacion)
            m.save()
        except Persona.MultipleObjectsReturned:
            # entrará aqui cuando se haya encontrado más de un
            # objeto que coincida
            pass
       





    return HttpResponse('Hello world!')