package fr.watermelonvtl.bdn.init;

import fr.watermelonvtl.bdn.BUILDINGNEEDS;
import net.fabricmc.fabric.api.client.itemgroup.FabricItemGroupBuilder;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.item.Items;
import net.minecraft.util.Identifier;

public class ModItemGroup {
    public static final ItemGroup VERTICAL_SLABS = FabricItemGroupBuilder.build(new Identifier(BUILDINGNEEDS.MODID,"vertical_slabs"),
                ()-> new ItemStack(ModBlocks.GLOWSTONEVERTICALSLAB));
}
