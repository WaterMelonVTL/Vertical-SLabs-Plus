package fr.watermelonvtl.bdn.init;

import net.fabricmc.api.EnvType;
import net.fabricmc.api.Environment;

import net.minecraft.client.render.RenderLayer;

import net.minecraft.state.property.Properties;
import net.minecraft.util.math.Direction;

import org.jetbrains.annotations.NotNull;


public class TransparentVerticalSlab extends VerticalSlab {

    public TransparentVerticalSlab(@NotNull Settings settings)
    {
        super(settings);
        setDefaultState(getDefaultState().with(Properties.HORIZONTAL_FACING, Direction.NORTH));
    };

    @Environment(EnvType.CLIENT)
    @Override
    public RenderLayer getRenderLayer() {
        return RenderLayer.TRANSLUCENT;
    }



}





