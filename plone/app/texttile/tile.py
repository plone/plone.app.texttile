from zope.schema import Text
from zope.i18nmessageid import MessageFactory
from plone.directives import form
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone.tiles.tile import PersistentTile

_ = MessageFactory('plone')


class ITextTile(form.Schema):

    form.widget(text=WysiwygFieldWidget)
    text = Text(title=_("Tile text"))


class TextTile(PersistentTile):
    """ A text tile """
