package fr.watermelonvtl.bdn.init;

import fr.watermelonvtl.bdn.BUILDINGNEEDS;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.util.Identifier;
import net.minecraft.util.registry.Registry;

public class ModItems {
    public static final Item MagicWand = new Item(new Item.Settings().group(ItemGroup.TOOLS).maxCount(1));
    public static void registerAll()
    {
        Registry.register(Registry.ITEM, new Identifier(BUILDINGNEEDS.MODID, "magic_wand"), MagicWand);
    }

}
