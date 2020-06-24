# -*- coding: utf-8 -*-

from imio.restapi.vocabularies import base
from imio.restapi.form.link import get_links


class PSTActionVocabularyFactory(base.RestSearchVocabularyFactory):
    """ Vocabulary that return all the pst actions from the app """
    application_id = "PST"

    @property
    def parameters(self):
        return "portal_type=pstaction&b_size=999"

    def _existing_link(self, obj):
        """ Return the link paths for the given content """
        link = get_links(obj)
        result = []
        if not link:  # This can happen with content created manually
            return result
        for link in get_links(obj):
            if link.back_link is True:
                result.append(link.path)
        return result

    @property
    def _children(self):
        if not hasattr(self, "_context_children"):
            self._context_children = [self.context[k] for k in self.context.keys()]
        return self._context_children

    @property
    def _existing_links(self):
        if not hasattr(self, "_context_links"):
            self._context_links = []
            for child in self._children:
                self._context_links.extend(self._existing_link(child))
        return self._context_links

    def _filter(self, value):
        return value not in self._existing_links


PSTActionVocabulary = PSTActionVocabularyFactory()
