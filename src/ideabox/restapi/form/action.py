# -*- coding: utf-8 -*-

from imio.restapi.form.action import RESTAction
from zope.component import adapter
from zope.publisher.interfaces.browser import IBrowserRequest
from ideabox.policy.content.campaign import ICampaign


@adapter(ICampaign, IBrowserRequest)
class PSTActionImportAction(RESTAction):
    title = u"Import PST Actions"
    application_id = u"PST"
    schema_name = None
    view_name = "pstaction-import-form"
