# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.rfd16


class PlonethemeRfd16Layer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plonetheme.rfd16)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.rfd16:default')


PLONETHEME_RFD16_FIXTURE = PlonethemeRfd16Layer()


PLONETHEME_RFD16_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_RFD16_FIXTURE,),
    name='PlonethemeRfd16Layer:IntegrationTesting'
)


PLONETHEME_RFD16_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_RFD16_FIXTURE,),
    name='PlonethemeRfd16Layer:FunctionalTesting'
)


PLONETHEME_RFD16_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_RFD16_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeRfd16Layer:AcceptanceTesting'
)
