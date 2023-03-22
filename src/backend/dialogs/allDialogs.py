from .chooseLanguage.chooseLanguage import chooseLanguage
from .mainMenu.mainMenu import mainMenu
from .forFreshman.forFreshman import forFreshman
from .studentOffice.studentOffice import studentOffice
from .studentOfficeAbout.studentOfficeAbout import studentOfficeAbout
from .studentOfficeWhy.studentOfficeWhy import studentOfficeWhy
from .universityWideUndergraduateModules.universityWideUndergraduateModules import (
    universityWideUndergraduateModules,
)
from .universityWideMagistracyModules.universityWideUndergraduateModules import (
    universityWideMagistracyModules,
)
from .documentOnPreviousEducation.documentOnPreviousEducation import (
    documentOnPreviousEducation,
)
from .library.library import library
from .news.news import news
from .announces.announces import announces
from .contests.contests import contests
from .exitConfirm.exitConfirm import exitConfirm
from .backDialog.backDialog import backDialog
from .educationalPublications.educationalPublications import educationalPublications
from .howToCheckRelevance.howToCheckRelevance import howToCheckRelevance
from .howToConnectWithDevelopers.howToConnectWithDevelopers import (
    howToConnectWithDevelopers,
)
from .whoIsCreator.whoIsCreator import whoIsCreator
from .help.help import help
from .randomFact.randomFact import randomFact
from .timeTable.timeTable import timeTable
from .timeTableFind.timeTableFind import timeTableFind
from .toAForeignStudent.toAForeignStudent import toAForeignStudent, toAForeignStudentDocum, toAForeignStudentAdd, toAForeignStudentBench, toAForeignStudentInter, toAForeignStudentMag
from .educationalPublicationsFind.educationalPublicationsFind import (
    educationalPublicationsFind,
)
from .scholarships.scholarships import scholarships
from .chessGame.chessGame import chessGame
from .chessMain.chessMain import chessMain
from .start_quiz.start_quiz import start_quiz
from .general_quiz.general_quiz import general_quiz
from .OfficeConsultation.OfficeConsultation import OfficeConsultation
from .officeOtherFeatures.officeOtherFeatures import officeOtherFeatures
from .repeat.repeat import repeat
from .whatYouCan.whatYouCan import whatYouCan
from .learnMoreAboutTheSkill import learnMoreAboutTheSkill

allDialogs = {
    "exitConfirm": exitConfirm,
    "repeat": repeat,
    "chooseLanguage": chooseLanguage,
    "whatYouCan": whatYouCan,
    "backDialog": backDialog,
    "forFreshman": forFreshman,
    "studentOfficeAbout": studentOfficeAbout,
    "officeOtherFeatures": officeOtherFeatures,
    "OfficeConsultation": OfficeConsultation,
    "studentOfficeWhy": studentOfficeWhy,
    "whoIsCreator": whoIsCreator,
    "howToConnectWithDevelopers": howToConnectWithDevelopers,
    "howToCheckRelevance": howToCheckRelevance,
    "learnMoreAboutTheSkill": learnMoreAboutTheSkill,
    "documentOnPreviousEducation": documentOnPreviousEducation,
    "UniversityWideMagistracyModules": universityWideMagistracyModules,
    "UniversityWideUndergraduateModules": universityWideUndergraduateModules,
    "educationalPublications": educationalPublications,
    "library": library,
    "news": news,
    "studentOffice": studentOffice,
    "announces": announces,
    "contests": contests,
    "randomFact": randomFact,
    "timeTable": timeTable,
    "timeTableFind": timeTableFind,
    "toAForeignStudentMigrDocs": toAForeignStudentDocum,
    "toAForeignStudentAddOprts": toAForeignStudentAdd,
    "toAForeignStudentIntMag": toAForeignStudentInter,
    "toAForeignStudentMag": toAForeignStudentMag,
    "toAForeignStudentBech": toAForeignStudentBench,
    "toAForeignStudent": toAForeignStudent,
    "educationalPublicationsFind": educationalPublicationsFind,
    "scholarships": scholarships,
    "start_quiz": start_quiz,
    "general_quiz": general_quiz,
    "help": help,
    "chessGame": chessGame,
    "chessMain": chessMain,
    "mainMenu": mainMenu,
}
