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

Vertical="_stairs"
Slab="_slab"

types=["stairs","inner_stairs","outer_stairs"]
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
            jsoncontent='{ "variants": { "facing=east,half=bottom,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "y": 270, "uvlock": true }, "facing=east,half=bottom,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs" }, "facing=east,half=bottom,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "y": 270, "uvlock": true }, "facing=east,half=bottom,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs" }, "facing=east,half=bottom,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs" }, "facing=east,half=top,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "uvlock": true }, "facing=east,half=top,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "y": 90, "uvlock": true }, "facing=east,half=top,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "uvlock": true }, "facing=east,half=top,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "y": 90, "uvlock": true }, "facing=east,half=top,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs", "x": 180, "uvlock": true }, "facing=north,half=bottom,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "y": 180, "uvlock": true }, "facing=north,half=bottom,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "y": 270, "uvlock": true }, "facing=north,half=bottom,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "y": 180, "uvlock": true }, "facing=north,half=bottom,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "y": 270, "uvlock": true }, "facing=north,half=bottom,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs", "y": 270, "uvlock": true }, "facing=north,half=top,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "y": 270, "uvlock": true }, "facing=north,half=top,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "uvlock": true }, "facing=north,half=top,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "y": 270, "uvlock": true }, "facing=north,half=top,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "uvlock": true }, "facing=north,half=top,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs", "x": 180, "y": 270, "uvlock": true }, "facing=south,half=bottom,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs" }, "facing=south,half=bottom,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "y": 90, "uvlock": true }, "facing=south,half=bottom,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs" }, "facing=south,half=bottom,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "y": 90, "uvlock": true }, "facing=south,half=bottom,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs", "y": 90, "uvlock": true }, "facing=south,half=top,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "y": 90, "uvlock": true }, "facing=south,half=top,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "y": 180, "uvlock": true }, "facing=south,half=top,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "y": 90, "uvlock": true }, "facing=south,half=top,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "y": 180, "uvlock": true }, "facing=south,half=top,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs", "x": 180, "y": 90, "uvlock": true }, "facing=west,half=bottom,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "y": 90, "uvlock": true }, "facing=west,half=bottom,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "y": 180, "uvlock": true }, "facing=west,half=bottom,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "y": 90, "uvlock": true }, "facing=west,half=bottom,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "y": 180, "uvlock": true }, "facing=west,half=bottom,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs", "y": 180, "uvlock": true }, "facing=west,half=top,shape=inner_left": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "y": 180, "uvlock": true }, "facing=west,half=top,shape=inner_right": { "model": "bdn:block/stairs/'+line+'/inner_stairs", "x": 180, "y": 270, "uvlock": true }, "facing=west,half=top,shape=outer_left": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "y": 180, "uvlock": true }, "facing=west,half=top,shape=outer_right": { "model": "bdn:block/stairs/'+line+'/outer_stairs", "x": 180, "y": 270, "uvlock": true }, "facing=west,half=top,shape=straight": { "model": "bdn:block/stairs/'+line+'/stairs", "x": 180, "y": 180, "uvlock": true } } }'
            blockstatejsonFile.write(jsoncontent)
            pass
        
    except Exception as e:
        print(f"Error creating/writing file: {e}")
    
    
        
    try:
        os.makedirs(models_path, exist_ok=True)  # Create folder if it doesn't exist
        for type in types:
            json_file_path = os.path.join(models_path, f"{type}.json")
            with open(json_file_path, "w") as json_file:
                jsoncontent='{"credit": "Made by watermelon python script ", "parent": "minecraft:block/'+type+'", "textures": { "bottom": "block/'+line+'", "top": "block/'+line+'", "side": "block/'+line+'" } }'
                json_file.write(jsoncontent)
                pass
            
            
    except Exception as e:
        print(f"Error creating/writing folder/files: {e}")

    try:
        os.makedirs(os.path.dirname(item_path), exist_ok=True)  # Create directories if they don't exist
        
        with open(item_path, "w") as jsonFile:
            jsoncontent='{"parent":"bdn:block/stairs/'+line+'/stairs"}'
            jsonFile.write(jsoncontent)
            pass
    except Exception as e:
        print(f"Error creating/writing file: {e}")

    

    
    content=('"bloc.bdn.'+VerticalBlocID+'":"'+Item_Name+'",')
    
    all_data.append(content)
            # Write JSON content with indentation
    blockname=line.upper()
    JavaPSFLines.append(f"public static final ModStairsBlock {VerticalVarName} = new ModStairsBloc(Blocks.{blockname}.getDefaultState(),FabricBlockSettings.of(Material.WOOD));\n")
    JavaRegisterLines.append('register_stairs('+VerticalVarName+', new Identifier(BUILDINGNEEDS.MODID,"'+VerticalBlocID+'"));\n')

with open("output.json", "w") as json_file:
    json_file.writelines(all_data)

JavaFinal=JavaPSFLines+JavaRegisterLines
JavaData.writelines(JavaFinal)
