import factory

from sotmjp.tests.factories import SotMTutorialProposalFactory
from symposion.conference.tests.factories import SectionFactory
from symposion.speakers.tests.factories import SpeakerFactory

from ..models import Presentation


class PresentationFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Presentation

    title = 'Presentation'
    description = 'Description'
    abstract = 'Abstract'
    speaker = factory.SubFactory(SpeakerFactory)
    proposal_base = factory.SubFactory(SotMTutorialProposalFactory)
    section = factory.SubFactory(SectionFactory)
