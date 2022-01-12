package com.example.examplemod;

import net.minecraft.init.Blocks;
import net.minecraft.item.Item;
import net.minecraftforge.common.util.EnumHelper;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;
import net.minecraftforge.fml.common.event.FMLPreInitializationEvent;
import org.apache.logging.log4j.Logger;

@Mod(modid = ExampleMod.MODID, name = ExampleMod.NAME, version = ExampleMod.VERSION)
public class ExampleMod
{
    public static final String MODID = "sword";
    public static final String NAME = "McMonkey26's Sword";
    public static final String VERSION = "1.0";

    private static Logger logger;
    public static Item.ToolMaterial myToolMaterial;
    public static Item mySword;

    @EventHandler
    public void preInit(FMLPreInitializationEvent event)
    {
        logger = event.getModLog();

        myToolMaterial = EnumHelper.addToolMaterial("JavaScript", 4, 42069, 69420.0F, 666F, 30);

        mySword = new CustomSword();
    }

    @EventHandler
    public void init(FMLInitializationEvent event)
    {
        // some example code
        logger.info("DIRT BLOCK >> {}", Blocks.DIRT.getRegistryName());
    }
}
