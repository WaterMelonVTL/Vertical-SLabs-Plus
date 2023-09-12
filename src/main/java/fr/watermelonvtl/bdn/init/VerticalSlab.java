package fr.watermelonvtl.bdn.init;

import net.minecraft.block.Block;
import net.minecraft.block.BlockState;

import net.minecraft.block.HorizontalFacingBlock;
import net.minecraft.entity.EntityContext;
import net.minecraft.item.ItemPlacementContext;
import net.minecraft.state.StateManager;
import net.minecraft.state.property.BooleanProperty;
import net.minecraft.state.property.EnumProperty;

import net.minecraft.state.property.Properties;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.Direction;
import net.minecraft.util.shape.VoxelShape;

import net.minecraft.util.shape.VoxelShapes;
import net.minecraft.world.BlockView;
import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;


public class VerticalSlab extends HorizontalFacingBlock {
    public static final EnumProperty<VerticalSlabType> TYPE ;

    protected static final VoxelShape BOTTOM_SHAPE;
    protected static final VoxelShape TOP_SHAPE;
    protected static final VoxelShape EAST_SHAPE;
    protected static final VoxelShape WEST_SHAPE;
    protected static final VoxelShape NORTH_SHAPE;
    protected static final VoxelShape SOUTH_SHAPE;


    public VerticalSlab(@NotNull Settings settings)
    {
        super(settings);
        setDefaultState(getDefaultState().with(Properties.HORIZONTAL_FACING, Direction.NORTH));
    };

    @Override
    protected void appendProperties(StateManager.@NotNull Builder<Block, BlockState> builder) {
        builder.add(Properties.HORIZONTAL_FACING);
    }
    @Override
    public boolean hasSidedTransparency(BlockState state) {
        return true;
    }
    @Override
    public VoxelShape getOutlineShape(@NotNull BlockState state, BlockView view, BlockPos pos, EntityContext context) {

        Direction dir= state.get(FACING);
        switch (dir) {
            case EAST:
                return EAST_SHAPE;
            case WEST:
                return WEST_SHAPE;
            case NORTH:
                return NORTH_SHAPE;
            case SOUTH:
                return SOUTH_SHAPE;
            default:
                return VoxelShapes.fullCube();
        }
    }

    @Override
    @Nullable
    public BlockState getPlacementState( ItemPlacementContext ctx) {
        return super.getPlacementState(ctx).with(Properties.HORIZONTAL_FACING, ctx.getPlayerFacing());
    }

    static {
        TYPE = EnumProperty.of("type", VerticalSlabType.class);

        BOTTOM_SHAPE = Block.createCuboidShape(0.0, 0.0, 0.0, 16.0, 8.0, 16.0);
        TOP_SHAPE = Block.createCuboidShape(0.0, 8.0, 0.0, 16.0, 16.0, 16.0);
        EAST_SHAPE = Block.createCuboidShape(8, 0, 0.0, 16.0, 16.0, 16.0);
        WEST_SHAPE = Block.createCuboidShape(0, 0, 0.0, 8, 16.0, 16.0);
        NORTH_SHAPE = Block.createCuboidShape(0, 0, 0.0, 16, 16.0, 8);
        SOUTH_SHAPE = Block.createCuboidShape(0, 0, 8, 16, 16.0, 16);
    }

}





