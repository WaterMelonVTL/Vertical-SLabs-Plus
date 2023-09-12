import os

Vertical="_vertical_slab"
Slab="_slab"

with open("McBlocNames.txt","r") as BlocNames:
    BlockIDList=BlocNames.readlines()
    for BlockID in BlockIDList:
        BlockID=BlockID[:-1]
    
        VerticalBlocID=BlockID+Vertical
        recipe_path = os.path.join("Python","temp","recipe", f"{VerticalBlocID}.json")
        try:
            os.makedirs(os.path.dirname(recipe_path), exist_ok=True)  
            
            with open(recipe_path, "w") as recipejsonFile:
                jsoncontent='{"type": "minecraft:crafting_shaped","pattern": ["X","X","X"],"key": {"X": {"item": "minecraft:'+BlockID+'"}},"result": {"item": "bdn:'+VerticalBlocID+'","count": 6}}'

                recipejsonFile.write(jsoncontent)
                pass
        except Exception as e:
            print(f"Error creating/writing file: {e}")
    
    