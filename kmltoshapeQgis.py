import os,qgis
path = r"H:\RajeevWork\mncfc\AP & UP KMLs\AP KML"
Location = r"F:\et"

for file in os.listdir(path):
    
    if file.endswith(".kml"):
        
        layer=  QgsVectorLayer(os.path.join(path,file), file, "ogr",)
        
        print(file)
        
        output_shp=os.path.join(Location,file.split(".kml")[0]+".shp")
       
        data_writer = QgsVectorFileWriter.writeAsVectorFormat(layer,output_shp,"utf-8",layer.crs(),"ESRI Shapefile")