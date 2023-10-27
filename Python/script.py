import os
import json


temp_path_BN =os.path.join("Python", "Temp","McBlocNames.txt")
temp_path_JVD=os.path.join("Python", "Temp","JavaData.txt")
BlocNames = open("McBlocNames.txt","r")
JavaData = open("JavaData.txt","w")
Lines=BlocNames.readlines()
JavaFinal=[]
JavaRegisterLines=[]
JavaPSFLines=[]

Vertical="_vertical_slab"
Slab="_slab"

directions = ["north", "south", "east", "west"]
all_data = []
for line in Lines:
    line=line[:-1]
    
    
    VerticalVarName=line.upper()+Vertical.upper()
    ##SlabVarName=line.upper()+Slab.upper
    VerticalBlocID=line+Vertical
    #SlabBlocID=line+Vertical
    Item_Name = VerticalBlocID.replace("_", " ").title()
    
    
    
    
    blockstate_path = os.path.join("Python", "Temp", "Blockstates", f"{VerticalBlocID}.json")
    models_path = os.path.join("Python", "Temp", "models", line)
    item_path = os.path.join("Python","temp","items", f"{VerticalBlocID}.json")
    
    langUpdate = []
    
    
    
    
    
    
    try:
        os.makedirs(os.path.dirname(blockstate_path), exist_ok=True)  # Create directories if they don't exist
        
        with open(blockstate_path, "w") as blockstatejsonFile:
            jsoncontent='{"variants": {"facing=north": {"model": "bdn:block/verticalslabs/'+line+'/north"},"facing=south": {"model": "bdn:block/verticalslabs/'+line+'/south"},"facing=east": {"model": "bdn:block/verticalslabs/'+line+'/east"},"facing=west": {"model": "bdn:block/verticalslabs/'+line+'/west"},"facing=double": {"model": "block/'+line+'"}}}'
            blockstatejsonFile.write(jsoncontent)
            pass
    except Exception as e:
        print(f"Error creating/writing file: {e}")
    
    
        
    try:
        os.makedirs(models_path, exist_ok=True)  # Create folder if it doesn't exist
        
        for direction in directions:
            json_file_path = os.path.join(models_path, f"{direction}.json")
            with open(json_file_path, "w") as json_file:
                jsoncontent='{"credit": "Made by watermelon python script ","parent": "bdn:block/verticalslabs/'+direction+'","textures": {"side": "block/'+line+'"}}'
                json_file.write(jsoncontent)
                pass
    except Exception as e:
        print(f"Error creating/writing folder/files: {e}")

    try:
        os.makedirs(os.path.dirname(item_path), exist_ok=True)  # Create directories if they don't exist
        
        with open(item_path, "w") as jsonFile:
            jsoncontent='{"parent":"bdn:block/verticalslabs/'+line+'/west"}'
            jsonFile.write(jsoncontent)
            pass
    except Exception as e:
        print(f"Error creating/writing file: {e}")

    

    
    content=('"bloc.bdn.'+VerticalBlocID+'":"'+Item_Name+'",')
    
    all_data.append(content)
            # Write JSON content with indentation
    
    JavaPSFLines.append(f"public static final VerticalSlab {VerticalVarName} = new VerticalSlab(FabricBlockSettings.of(Material.WOOD));\n")
    JavaRegisterLines.append('register('+VerticalVarName+', new Identifier(BUILDINGNEEDS.MODID,"'+VerticalBlocID+'"));\n')

with open("output.json", "w") as json_file:
    json_file.writelines(all_data)

JavaFinal=JavaPSFLines+JavaRegisterLines
JavaData.writelines(JavaFinal)
