from zope.schema import Text
from zope.i18nmessageid import MessageFactory
from plone.autoform import directives as form
from plone.tiles.tile import PersistentTile
from plone.app.tiles.interfaces import ITileBaseSchema

_ = MessageFactory('plone')


class ITextTile(ITileBaseSchema):

    form.widget(text='plone.app.z3cform.wysiwyg.WysiwygFieldWidget')
    text = Text(
        title=_("Tile text"),
        )


class TextTile(PersistentTile):
    """ A text tile """
