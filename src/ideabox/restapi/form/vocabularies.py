# -*- coding: utf-8 -*-

from imio.restapi.vocabularies import base
from imio.restapi.form.link import get_links


class PSTActionVocabularyFactory(base.RestSearchVocabularyFactory):
    """ Vocabulary that return all the pst actions from the app """
    application_id = "PST"

    @property
    def parameters(self):
        return "portal_type=pstaction&b_size=999"

    def _existing_link(self, id, obj):
        """ Verify if the given id is defined in a link on the object """
        for link in get_links(obj):
            if link.back_link is True:
                if link.path == id:
                    return True
        return False

    @property
    def _children(self):
        if not hasattr(self, "_context_children"):
            self._context_children = [self.context[k] for k in self.context.keys()]
        return self._context_children

    def _filter(self, value):
        for child in self._children:
            if self._existing_link(value["@id"], child):
                return False
        return True


PSTActionVocabulary = PSTActionVocabularyFactory()
