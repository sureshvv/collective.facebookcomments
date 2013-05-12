from zope.interface import implements
from zope.viewlet.interfaces import IViewlet
from zope.publisher.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from collective.facebookcomments.interfaces import IFacebookCommentsSettings

class FacebookComments(BrowserView):
    """Facebook comments
    """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        self.context = context
        self.request = request
        self.__parent__ = view
        self.manager = manager
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IFacebookCommentsSettings)


    def update(self):
        pass

    def available(self):
        return self.settings.portal_types and self.context.portal_type in self.settings.portal_types

    def url(self):
        url1 = self.context.absolute_url()
        if not url1.endswith('/view'):
            url1 += '/view'
        url1 = url1.replace('image_', 'leadImage_')
        return url1

    render = ViewPageTemplateFile("facebook_comments.pt")

class Metatag(BrowserView):
    """Facebook comments metatag
    """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        self.context = context
        self.request = request
        self.__parent__ = view
        self.manager = manager
        registry = getUtility(IRegistry)
        self.settings = registry.forInterface(IFacebookCommentsSettings)

    def update(self):
        pass

    def getAppID(self):
        return self.settings.facebook_appid

    render = ViewPageTemplateFile("facebook_comments_metatag.pt")

