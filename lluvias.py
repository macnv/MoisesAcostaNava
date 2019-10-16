import xlrd
from arrays import *
def main():
    a3=Array3D(34,33,14)
    for anio in range(1985,2019,1):
        ruta="./Precipitacion/"+str(anio)+"Precip.xls"
        archivo=xlrd.open_workbook(filename=ruta)
        hoja=archivo.sheet_by_index(0)
        for r in range(1,34,1):
            for c in range(0,14,1):
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r,c))
    """a=int(input("anio(1985-2019)"))
    e=int(input("estado(1-32)"))
    m=int(input("mes(1-12)"))"""
    a=2005
    e=7
    m=3
    #tarea1
    print("En el año",a,"en el mes de",a3.get_item(a-1985,0,m),"en el estado",a3.get_item(a-1985,e,0),"promedio",a3.get_item(a-1985,e,m))
    print()
    #tarea2
    suma=0.0
    for i in range(1985,2019,1):
        #print("año",i,"    ",a3.get_item(i-1985,e,m))
        suma+=a3.get_item(i-1985,e,m)
    print("promedio: ",suma/34)
    print()
    #tarea3 estado
    suma=0.0
    for j in range(1985,2019,1):
        for i in range(0,13,1):
            #print("anio",j,"mes",i,a3.get_item(j-1985,e,i))
            if i!=0:
                suma+=a3.get_item(j-1985,e,i)
        #print()
    print("promedio",suma/408)
    #tarea4 todo
    suma=0.0
    for k in range(1985,2019,1):
        for i in range(1,33,1):
            for j in range(0,13,1):
                if j!=0:
                    #print("en el año",k,"en el mes",a3.get_item(k-1985,0,j),"en el estado",a3.get_item(a-1985,i,0),"precipitacion",a3.get_item(k-1985,i,j))
                    suma+=a3.get_item(k-1985,i,j)
    print(suma/13056)
                    
main()
    

