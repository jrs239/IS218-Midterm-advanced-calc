import os
import importlib.util
from calculator.plugin_base import PluginCommand
from calculator.logger import logger

def load_plugins(plugin_dir):
    plugins = {}

    # Check if the plugin directory actually exists
    if not os.path.exists(plugin_dir):
        logger.warning(f"Plugin directory {plugin_dir} does not exist")
        return plugins

    # Loop through all Python files in the plugin folder
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py"):
            path = os.path.join(plugin_dir, filename)
            name = filename[:-3]

            # Dynamically load the module from file
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
            except Exception as e:
                logger.error(f"Failed to load plugin {name}: {e}")
                continue

            # Look through the module for classes that subclass PluginCommand
            for attr in dir(module):
                obj = getattr(module, attr)
                if isinstance(obj, type) and issubclass(obj, PluginCommand) and obj is not PluginCommand:
                    # Found a valid plugin command, instantiate it
                    cmd_instance = obj()
                    plugins[cmd_instance.name()] = cmd_instance
                    logger.info(f"Loaded plugin: {cmd_instance.name()}")

    return plugins
