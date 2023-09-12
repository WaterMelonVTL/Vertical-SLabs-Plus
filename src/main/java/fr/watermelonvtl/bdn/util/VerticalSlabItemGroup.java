package fr.watermelonvtl.bdn.util;

import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.util.registry.Registry;

public class VerticalSlabItemGroup extends ItemGroup {
    public static final VerticalSlabItemGroup instance= new VerticalSlabItemGroup(ItemGroup.GROUPS.length, "vertical_slabs");
    private VerticalSlabItemGroup(int index, String label){super(index,label);}
    @Override
    public ItemStack createIcon(){return new ItemStack(Registry.ITEM.get(12));}
    }

