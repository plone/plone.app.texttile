from zope.schema import Text
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory
from plone.tiles.tile import PersistentTile


_ = MessageFactory('plone')


class ITextTile(Interface):
    text = Text(title=_("Tile text"))


class TextTile(PersistentTile):
    """ A text tile """

