from .generalMenu.generalMenu import generalMenu
from .russianMenu.russianMenu import russianMenu
from .forFreshman.forFreshman import forFreshman
from .studentOffice.studentOffice import studentOffice
from .studentOfficeAbout.studentOfficeAbout import studentOfficeAbout
from .studentOfficeWhy.studentOfficeWhy import studentOfficeWhy
from .universityWideUndergraduateModules.universityWideUndergraduateModules import universityWideUndergraduateModules
from .documentOnPreviousEducation.documentOnPreviousEducation import documentOnPreviousEducation
from .library.library import library
from .news.news import news
from .announces.announces import announces
from .contests.contests import contests
from .exitConfirm.exitConfirm import exitConfirm
from .backDialog.backDialog import backDialog
from .educationalPublications.educationalPublications import educationalPublications
from .educationalPublicationsFind.educationalPublicationsFind import educationalPublicationsFind

allDialogs = {
    'generalMenu': generalMenu,
    'exitConfirm': exitConfirm,
    'backDialog': backDialog,
    'forFreshman': forFreshman,
    'studentOffice': studentOffice,
    'studentOfficeAbout': studentOfficeAbout,
    'studentOfficeWhy': studentOfficeWhy,
    'documentOnPreviousEducation': documentOnPreviousEducation,
    'universityWideUndergraduateModules': universityWideUndergraduateModules,
    'educationalPublications': educationalPublications,
    'educationalPublicationsFind': educationalPublicationsFind,
    'library': library,
    'news': news,
    'announces': announces,
    'contests': contests,
    'russianMenu': russianMenu
}
