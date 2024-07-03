from modello.model import Model
myModel=Model()
myModel.buildGraph(120+60*1000)
print(myModel.getGraphDeails())
print(myModel.getNode(261))
myModel.getSetAlbum()