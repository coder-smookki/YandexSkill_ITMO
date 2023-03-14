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

allDialogs = {
    'exitConfirm': exitConfirm,
    'backDialog': backDialog,
    'generalMenu': generalMenu,
    'forFreshman': forFreshman,
    'studentOffice': studentOffice,
    'studentOfficeAbout': studentOfficeAbout,
    'studentOfficeWhy': studentOfficeWhy,
    'documentOnPreviousEducation': documentOnPreviousEducation,
    'universityWideUndergraduateModules': universityWideUndergraduateModules,
    'library': library,
    'news': news,
    'announces': announces,
    'contests': contests,
    'russianMenu': russianMenu
}
