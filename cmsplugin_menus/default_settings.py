"""
Default menu settings, are applied if there isn't value defined in project
settings. 
All available settings are listed here - override them in your project settings.
"""
import constants
gettext = lambda s: s

CMSPLUGIN_MENUS_TEXT_ENABLED = False

CMSPLUGIN_MENUS_PLACEHOLDER_CONF = {
        constants.CMSPLUGIN_MENUS_LINK_BLOCK_PLACEHOLDER: {
                'plugins': ('LinkPlugin', 'SnippetPlugin'),
                'name': gettext("links")
}}
