package fr.watermelonvtl.bdn.init;



import net.minecraft.util.StringIdentifiable;

public enum VerticalSlabType implements StringIdentifiable {
    EAST("east"),
    WEST("west"),
    NORTH("north"),
    SOUTH("south"),
    DOUBLE("double");

    private final String name;

    private VerticalSlabType(String name) {
        this.name = name;
    }

    public String toString() {
        return this.name;
    }

    public String asString() {
        return this.name;
    }
}